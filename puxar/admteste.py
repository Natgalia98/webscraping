from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# URLs pré-definidas
URLS_PREDEFINIDAS = {
    "moodle_unesp": {
        "nome": "Moodle UNESP",
        "url": "https://moodle.unesp.br",
        "filtro_sugerido": "/course/view.php"
    },
    "coursera": {
        "nome": "Coursera",
        "url": "https://www.coursera.org",
        "filtro_sugerido": "/learn/"
    },
    "edx": {
        "nome": "edX",
        "url": "https://www.edx.org",
        "filtro_sugerido": "/course/"
    }
}

@app.route('/urls-predefinidas', methods=['GET'])
def get_urls_predefinidas():
    return jsonify(URLS_PREDEFINIDAS)

@app.route('/buscar', methods=['POST'])
def buscar_cursos():
    try:
        data = request.get_json()
        url = data.get('url')
        filtro_url = data.get('filtro_url', '')
        area_conhecimento = data.get('area_conhecimento', '').lower()
        
        # Se for uma chave pré-definida, usar a URL correspondente
        if url in URLS_PREDEFINIDAS:
            url_info = URLS_PREDEFINIDAS[url]
            url = url_info['url']
            if not filtro_url:
                filtro_url = url_info.get('filtro_sugerido', '')
        
        if not url:
            return jsonify({"success": False, "error": "URL não fornecida"})
        
        cursos = extrair_cursos_da_url(url, filtro_url, area_conhecimento)
        
        return jsonify({
            "success": True,
            "total": len(cursos),
            "cursos": cursos
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

def extrair_cursos_da_url(url, filtro_url='', area_conhecimento=''):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        urls_unicas = set()
        cursos_encontrados = []
        
        parsed_url = urlparse(url)
        dominio_base = f"{parsed_url.scheme}://{parsed_url.netloc}"
        
        # Encontrar todos os links
        for link in soup.find_all('a'):
            url_relativa = link.get('href')
            nome_curso = link.get_text().strip()
            
            if not url_relativa or not nome_curso or len(nome_curso) < 3:
                continue
            
            # Aplicar filtro de URL
            if filtro_url and filtro_url not in url_relativa:
                continue
            
            # Construir URL completa
            if url_relativa.startswith('http'):
                url_completa = url_relativa
            else:
                url_completa = urljoin(dominio_base, url_relativa)
            
            # Aplicar filtro de área de conhecimento
            if area_conhecimento and area_conhecimento not in nome_curso.lower():
                continue
            
            # Adicionar à lista se for única
            if url_completa not in urls_unicas:
                urls_unicas.add(url_completa)
                cursos_encontrados.append({
                    "nome": nome_curso,
                    "url": url_completa
                })
        
        return cursos_encontrados
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro ao acessar a URL: {e}")
    except Exception as e:
        raise Exception(f"Erro inesperado: {e}")

if __name__ == '__main__':
    app.run(debug=True)