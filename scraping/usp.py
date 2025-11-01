import requests

from bs4 import BeautifulSoup

import re

ciencia_computacao_usp=requests.get('https://eaulas.usp.br/portal/profession.action?profession=Ci%C3%AAncia+da+Computa%C3%A7%C3%A3o+e+Inform%C3%A1tica')

url_curso_usp='/course.action'

curso_ciencia_computacao=BeautifulSoup(ciencia_computacao_usp.text,'html.parser')

#Ciencia da computação usp *duplicadando url*
print("\nCurso de Ciencia da Computação - USP\n")
urls_unicas = set()
cursos_encontrados = []

for link in curso_ciencia_computacao.find_all('a'):
    url=link.get('href')
    nome=link.get_text().strip()

    if  url and url_curso_usp in url and nome:
        url_completa="https://eaulas.usp.br/"+url
        if url_completa not in urls_unicas:
            urls_unicas.add(url_completa)
            cursos_encontrados.append((nome, url_completa))
for nome, url_completa in cursos_encontrados:
    print(nome)
    print(url_completa)
    print()