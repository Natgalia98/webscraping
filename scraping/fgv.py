import requests
from bs4 import BeautifulSoup
import re

tecnologia_fgv=requests.get('https://educacao-executiva.fgv.br/cursos/gratuitos?sort_by=field_oferta_data_inicio_turma_value&items_per_page=10&field_curso_serie_target_id_entityreference_filter=All&area-conhec%5B%5D=571')

url_curso_fgv='online/curta-media-duracao-online/'
curso_tecnologia_fgv=BeautifulSoup(tecnologia_fgv.text,'html.parser')

urls_unicas = set()
cursos_encontrados = []
#tecnologia fgv *recebendo curso não relacionados*
print("\nCurso de Tecnologia - FGV\n")


for link in curso_tecnologia_fgv.find_all('a'):
    url=link.get('href')
    nome_curso=link.get_text().strip()
    if url and url_curso_fgv in url and nome_curso:
        url_completa = "https://educacao-executiva.fgv.br/" + url
        if url_completa not in urls_unicas:
            urls_unicas.add(url_completa)
            cursos_encontrados.append((nome_curso, url_completa))
for nome_curso,url_completa in cursos_encontrados:
        print(nome_curso)
        print(url_completa)
        print() 