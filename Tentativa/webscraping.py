import requests

#responsavel por fazer a requisição ao endereço da internet e obter o conteudo da pagina

from bs4 import BeautifulSoup

#resposavel por pegar o codigo HTML
# que o requsts obteve da pagina e transformar em u m objeto python

import re


dados = requests.get('https://www.ev.org.br/areas-de-interesse/analise-de-dados',)


soup= BeautifulSoup(dados.text,'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
