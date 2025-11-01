import requests

from bs4 import BeautifulSoup

import re


informatica_ifes=requests.get('https://mooc.cefor.ifes.edu.br/v/')

url_curso_ifes='/course/view.php?'

curso_informatica_ifes=BeautifulSoup(informatica_ifes.text,'html.parser')

#Curso de Informática - IFES *deve arrumar para pegar o nome certo*

print("\nCurso de Informática - IFES\n")

for link in curso_informatica_ifes.find_all('h6'):
    nome_curso=link.get_text()
    for link in curso_informatica_ifes.find_all('a'):
        url=link.get('href')
        if  url and url_curso_ifes in url:
            url_completa=url+"\n"
print(nome_curso)
print(url_completa)