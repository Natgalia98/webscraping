import requests

#responsavel por fazer a requisição ao endereço da internet e obter o conteudo da pagina

from bs4 import BeautifulSoup

#'-> resposável por pegar o codigo HTML
# que o requests obteve da pagina e transformar em um objeto python

import re

#request e BeautifulSoup
analise_dados_bradesco = requests.get('https://www.ev.org.br/areas-de-interesse/analise-de-dados')

inteligencia_artificial_bradesco=requests.get('https://www.ev.org.br/areas-de-interesse/inteligencia-artificial')

programacao_bradesco=requests.get('https://www.ev.org.br/areas-de-interesse/programacao')
#'-> variaveis que requisitam o que procuram no site 
tecnologia_fgv=requests.get('https://educacao-executiva.fgv.br/cursos/gratuitos?sort_by=field_oferta_data_inicio_turma_value&items_per_page=10&field_curso_serie_target_id_entityreference_filter=All&area-conhec%5B%5D=571')

informatica_ifrs=requests.get('https://moodle.ifrs.edu.br/course/index.php?categoryid=79&browse=courses&perpage=30&page=0')

curso_bradesco='/cursos/'#condicional especificada para encontrar o que é necessário
curso_fgv='online/curta-media-duracao-online/'
curso_ifrs='/course/info'


cursos_analise_dados_br= BeautifulSoup(analise_dados_bradesco.text,'html.parser')
cursos_inteligencia_artificial_br= BeautifulSoup(inteligencia_artificial_bradesco.text,'html.parser')
cursos_programacao_br=BeautifulSoup(programacao_bradesco.text,'html.parser')
curso_tecnologia_fgv=BeautifulSoup(tecnologia_fgv.text,'html.parser')
curso_informatica=BeautifulSoup(informatica_ifrs.text,'html.parser')
#nova variavel que recebe, através do BeautifulSoup, o que procuram e oque requistaram anteriormente, além disso 
# é analisado pelo html.parser

#analise de dados bradesco
for link in cursos_analise_dados_br.find_all('a'):
    url=link.get('href')
    if  url and curso_bradesco in url:
        print("https://www.ev.org.br"+url)
   
'''#inteligencia arifical bradesco
for link in cursos_inteligencia_artificial_br.find_all('a'):
    url=link.get('href')
    if  url and curso in url:
        print("https://www.ev.org.br"+url)

#programacao bradesco
for link in cursos_programacao_br.find_all('a'):
    url=link.get('href')
    if  url and curso in url:
        print("https://www.ev.org.br"+url)

for link in curso_tecnologia_fgv.find_all('a'):
    url=link.get('href')
    if  url and curso_fgv in url:
        print("https://educacao-executiva.fgv.br/"+url)

for link in curso_informatica.find_all('a'):
    url=link.get('href')
    if  url and curso_ifrs in url:
        print(url)'''

