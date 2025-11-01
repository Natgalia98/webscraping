import requests
from bs4 import BeautifulSoup

def extrair_cursos_codecademy():
    print("\n🎓 Extraindo Cursos da Codecademy\n")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get('https://www.codecademy.com/catalog', headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print("📚 Cursos Encontrados:\n")
        
        cursos_encontrados = []
        
        for link in soup.find_all('a', href=True):
            url = link.get('href', '')
            nome = link.get_text().strip()
            
            # Filtro mais específico para cursos
            if ('catalog' in url.lower() or 'learn' in url.lower()) and len(nome) > 5:
                # Completar URL se for relativa
                if url.startswith('/'):
                    url = 'https://www.codecademy.com' + url
                
                cursos_encontrados.append((nome, url))
        
        # Remover duplicatas
        cursos_unicos = []
        urls_vistas = set()
        
        for nome, url in cursos_encontrados:
            if url not in urls_vistas and nome:
                cursos_unicos.append((nome, url))
                urls_vistas.add(url)
        
        # Exibir resultados
        for i, (nome, url) in enumerate(cursos_unicos[:90], 1): 
            print(f"{i:2d}. {nome}")
            print(f"    🔗 {url}\n")
            
        print(f"Total de cursos encontrados: {len(cursos_unicos)}")
        
    else:
        print(f"❌ Erro {response.status_code} ao acessar o site")

# Executar
extrair_cursos_codecademy()