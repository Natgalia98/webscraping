import requests

#responsavel por fazer a requisição ao endereço da internet e obter o conteudo da pagina

from bs4 import BeautifulSoup

#'-> resposável por pegar o codigo HTML
# que o requests obteve da pagina e transformar em um objeto python

import re

#request e BeautifulSoup
# variaveis que requisitam o que procuram no site
analise_dados_bradesco = requests.get('https://www.ev.org.br/areas-de-interesse/analise-de-dados')

inteligencia_artificial_bradesco=requests.get('https://www.ev.org.br/areas-de-interesse/inteligencia-artificial')

programacao_bradesco=requests.get('https://www.ev.org.br/areas-de-interesse/programacao')

#condicional especificada para encontrar o que é necessário
url_curso_bradesco='/cursos/'

# é analisado pelo html.parser
cursos_analise_dados_br= BeautifulSoup(analise_dados_bradesco.text,'html.parser')
cursos_inteligencia_artificial_br= BeautifulSoup(inteligencia_artificial_bradesco.text,'html.parser')
cursos_programacao_br=BeautifulSoup(programacao_bradesco.text,'html.parser')

#analise de dados bradesco
print("\nCurso de Análise de Dados - Bradesco\n")

for link in cursos_analise_dados_br.find_all('a'):
    url=link.get('href')
    nome_curso=link.get_text()
    if  url and url_curso_bradesco in url:
        print(nome_curso)
        print("https://www.ev.org.br"+url)

# print("2,'"+nome_curso+"'" +",'"+"https://www.ev.org.br"+url+"'")

#inteligencia arifical bradesco
print("\nCurso de Inteligência Artificial - Bradesco\n")

for link in cursos_inteligencia_artificial_br.find_all('a'):
    url=link.get('href')
    nome_curso=link.get_text()
    if  url and url_curso_bradesco in url:
        print(nome_curso)
        print("https://www.ev.org.br"+url)
    
#programacao bradesco
print("\nCurso de Programação - Bradesco\n")

for link in cursos_programacao_br.find_all('a'):
    url=link.get('href')
    nome_curso=link.get_text()
    if  url and url_curso_bradesco in url:        
        print(nome_curso)
        print("https://www.ev.org.br"+url)
