import requests

from bs4 import BeautifulSoup

import re

tecnologia_programiz=requests.get('https://www-programiz-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc')

Tutorials='Tutorials'

curso_tecnologia_programiz=BeautifulSoup(tecnologia_programiz.text,'html.parser')

#Curso de Tecnologia- Programiz *deve arrumar para pegar apenas o necessario*

print("\nCurso de Tecnologia - Programiz\n")
urls_unicas = set()
cursos_encontrados = []
for link in curso_tecnologia_programiz.find_all('a'):
    url=link.get('href')
    nome_curso=link.get_text().strip()
    if  url and Tutorials in nome_curso:
        url_completa="https://www-programiz-com.translate.goog/"+url
        if url_completa not in urls_unicas:
            urls_unicas.add(url_completa)
            cursos_encontrados.append((nome_curso, url_completa))
for nome, url_completa in cursos_encontrados:
    print(nome)
    print(url_completa)