import requests

#responsavel por fazer a requisição ao endereço da internet e obter o conteudo da pagina

from bs4 import BeautifulSoup

#'-> resposável por pegar o codigo HTML
# que o requests obteve da pagina e transformar em um objeto python

import re

#request e BeautifulSoup
# variaveis que requisitam o que procuram no site

informatica_learncafe=requests.get('https://www.learncafe.com/cursos-gratis/informatica-e-internet')

url_curso_learncafe='cursos/'

curso_informatica_learncafe=BeautifulSoup(informatica_learncafe.text,'html.parser')

#Curso de Informática - LearnCafe *deve arrumar para pegar o nome certo*

print("\nCurso de Informática - LearnCafe\n")

for link in curso_informatica_learncafe.find_all('a'):
    url=link.get('href')
    nome_curso=link.get_text()
    if  url and url_curso_learncafe in url:
        print(nome_curso)
        print(url+"\n")