from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000').text
soup = BeautifulSoup(html_text, 'lxml')
accion = soup.find_all('table', class_='TblPort')
print(accion)
