import requests
from bs4 import BeautifulSoup
import re

tecnologia_aprenda_mais=requests.get('https://aprendamais.mec.gov.br/course/index.php?categoryid=8')

url_curso_aprenda_mais='course/view.php?id='

curso_tecnologia_aprenda_mais=BeautifulSoup(tecnologia_aprenda_mais.text,'html.parser')

#tecnologia aprenda masi gov*

print("\nCurso de Tecnologia - Aprenda Mais\n")

for link in curso_tecnologia_aprenda_mais.find_all('a'):
    url=link.get('href')
    nome_curso=link.get_text()
    if  url and url_curso_aprenda_mais in url:
        print(nome_curso)
        print(url+"\n")