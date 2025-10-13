import requests

#responsavel por fazer a requisição ao endereço da internet e obter o conteudo da pagina

from bs4 import BeautifulSoup

#'-> resposável por pegar o codigo HTML
# que o requests obteve da pagina e transformar em um objeto python

import re

ciencia_computacao_usp=requests.get('https://eaulas.usp.br/portal/profession.action?profession=Ci%C3%AAncia+da+Computa%C3%A7%C3%A3o+e+Inform%C3%A1tica')

url_curso_usp='/course.action'

curso_ciencia_computacao=BeautifulSoup(ciencia_computacao_usp.text,'html.parser')

#Ciencia da computação usp *duplicadando url*
print("\nCurso de Ciencia da Computação - USP\n")

for link in curso_ciencia_computacao.find_all('a'):
    url=link.get('href')
    nome=link.get_text()
    if  url and url_curso_usp in url:
        print(nome)
        print("https://eaulas.usp.br/"+url)
