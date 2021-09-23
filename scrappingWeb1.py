# scrapping de url de la pagina
from bs4 import BeautifulSoup
import sys
import urllib.request
datos = urllib.request.urlopen(
    'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000').read().decode()
soup = BeautifulSoup(datos)
tags = soup('a')
for tag in tags:
    print(tag.get('href'))
