import requests

#responsavel por fazer a requisição ao endereço da internet e obter o conteudo da pagina

from bs4 import BeautifulSoup

#resposavel por pegar o codigo HTML
# que o requsts obteve da pagina e transformar em u m objeto python

import re
pagina = requests.get('https://moodle.ifrs.edu.br/course/index.php?categoryid=79&browse=courses&page=1')

dados_pagina= BeautifulSoup(pagina.text,'html.parser')



todos_cursos=dados_pagina.findall('div',class_="coursename")
#palavra 'class' no python é restrita por que ela foi utilizada
#dentro da estrutura interna do código

for div in todos_cursos:
    texto=div.find('a',class_="coursename")
    print(texto)