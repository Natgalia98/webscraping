import requests

#responsavel por fazer a requisição ao endereço da internet e obter o conteudo da pagina

from bs4 import BeautifulSoup

#'-> resposável por pegar o codigo HTML
# que o requests obteve da pagina e transformar em um objeto python

import re

#request e BeautifulSoup
# variaveis que requisitam o que procuram no site

informatica_ifrs=requests.get('https://moodle.ifrs.edu.br/course/index.php?categoryid=79&browse=courses&perpage=30&page=0')

url_curso_ifrs='/course/view.php?id='

curso_informatica=BeautifulSoup(informatica_ifrs.text,'html.parser')

print("\nCurso de Informática - IFRS\n")

for link in curso_informatica.find_all('a'):
    url=link.get('href')
    nome_curso=link.get_text()
    if  url and url_curso_ifrs in url and nome_curso:
        print(nome_curso)
        print(url)