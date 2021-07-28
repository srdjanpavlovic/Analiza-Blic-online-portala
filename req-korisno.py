import requests
from bs4 import BeautifulSoup

blic = requests.get('https://www.blic.rs/')
informer = requests.get('https://informer.rs/')
soup_blic = BeautifulSoup(blic.text, 'lxml')
soup_informer = BeautifulSoup(informer.text, 'lxml')

brojac_blic = 0
brojac_informer = 0
rec1 = 'Đilas'
rec2 = 'ĐILAS'

for heading in soup_blic.find_all(["h3"]):
    # print(heading.name + ' ' + heading.text.strip())
    if rec1 in heading.text.strip() or rec2 in heading.text.strip():
        brojac_blic += 1

for heading in soup_informer.find_all(["h2"]):
    # print(heading.name + ' ' + heading.text.strip())
    if rec1 in heading.text.strip() or rec2 in heading.text.strip():
        brojac_informer += 1
print()
print(f'Broj reči "{rec1}" na današnjoj naslovnoj strani Blica     : {brojac_blic}')
print(f'Broj reči "{rec1}" na današnjoj naslovnoj strani Informera : {brojac_informer}')
