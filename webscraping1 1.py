from selenium import webdriver

from selenium.webdriver.common.by import By

import os
from time import sleep

driver=webdriver.Chrome()

driver.get('https://www.ev.org.br/areas-de-interesse/analise-de-dados')


sleep(5)
#XPATH(identitificador de elementos no site)
# //tag[@atributos='valor']
#//a[@class='coursename']
curso_dados=driver.find_elements(By.XPATH,"//a[@class='m-card_link']")

for curso in curso_dados:
    with open('curso.cvs','a',encoding='utf-8') as arquivo:
        arquivo.write(f'{curso.text}{os.linesep}')

input('')
#12