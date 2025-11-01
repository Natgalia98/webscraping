import requests

#responsavel por fazer a requisição ao endereço da internet e obter o conteudo da pagina

from bs4 import BeautifulSoup

#'-> resposável por pegar o codigo HTML
# que o requests obteve da pagina e transformar em um objeto python

import re

#request e BeautifulSoup
# variaveis que requisitam o que procuram no site

informatica_ifmg=requests.get('https://mais.ifmg.edu.br/maisifmg/course/index.php?categoryid=10')

url_curso_ifmg='/course/view.php?id='

curso_tecnologia_ifmg=BeautifulSoup(informatica_ifmg.text,'html.parser')


print("\nCurso de Tecnologia - IFMG\n")

for link in curso_tecnologia_ifmg.find_all('a'):
    url=link.get('href')
    nome_curso=link.get_text()
    if  url and url_curso_ifmg in url:
        print(nome_curso)
        print(url+"\n")