# Importamos la librería para hacer peticiones http
import requests
# Importamos la librería para "enterder" el html
from bs4 import BeautifulSoup


# Definimos la url que queremos pedir
url_page = 'https://iol.invertironline.com/mercado/cotizaciones'

# tarda 480 milisegundos
page = requests.get(url_page).text
soup = BeautifulSoup(page, "lxml")

# Hacemos la petición
tabla = soup.find('table', attrs={'id': 'cotizaciones'})
# tabla = soup.find('tr', attrs={'td': ''})
# print(tabla)

nombre = tabla.select('b')

# print(nombre)

maximoPorAccion = soup.find_all('td', attrs={'data-field': 'Maximo'})

maxAcci = []
maxAcciFloat = []

nameAcc = []

for i in range(0, len(maximoPorAccion)):
    maxAcci.append(((((maximoPorAccion[i].text).replace('\r\n', "")).replace(' ', '')).replace('.', '')).replace(',', '.'))
    maxAcciFloat.append(float(maxAcci[i]))

    nameAcc.append(((nombre[i].text).replace('\r\n', '')).replace(' ', ''))

ind = maxAcciFloat.index(max(maxAcciFloat))
print(max(maxAcciFloat))
print(nameAcc[ind])