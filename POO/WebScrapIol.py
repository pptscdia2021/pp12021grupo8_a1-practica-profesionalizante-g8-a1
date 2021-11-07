# Importamos la librería para hacer peticiones http
import requests
# Importamos la librería para "enterder" el html
from bs4 import BeautifulSoup

class acciones:
    def __init__(self):
        # Definimos la url que queremos pedir
        self.url_page = 'https://iol.invertironline.com/mercado/cotizaciones'


    def scrap_iol(self, url_page):
        # Llamo la variable de otra funcion que utilizare en esta
        self.url_page
        # tarda 480 milisegundos
        page = requests.get(self.url_page).text
        soup = BeautifulSoup(page, "lxml")

        # Hacemos la petición
        tabla = soup.find('table', attrs={'id': 'cotizaciones'})
        nombre = tabla.select('b')

        maximoPorAccion = soup.find_all('td', attrs={'data-field': 'Maximo'})

        maxAcci = []
        maxAcciFloat = []

        nameAcc = []

        for i in range(0, len(maximoPorAccion)):
            maxAcci.append(((((maximoPorAccion[i].text).replace('\r\n', "")).replace(
                ' ', '')).replace('.', '')).replace(',', '.'))
            maxAcciFloat.append(float(maxAcci[i]))

            nameAcc.append(((nombre[i].text).replace('\r\n', '')).replace(' ', ''))

        b = int(len(maximoPorAccion))
        a = int(b - 2)
        Max_ind1 = maxAcciFloat.index(max(maxAcciFloat))
        Max_ind2 = maxAcciFloat.index(maxAcciFloat[-1])
        ind1 = maxAcciFloat.index(min(maxAcciFloat))
        ind2 = maxAcciFloat.index((maxAcciFloat[a]))
        return print(max(maxAcciFloat), "maxima accion", max(maxAcciFloat), nameAcc[Max_ind1], "segunda accion mas alta", (maxAcciFloat[-1]), nameAcc[Max_ind2], "accion mas baja", min(maxAcciFloat), nameAcc[ind1], "segunda accion mas baja", maxAcciFloat[a], nameAcc[ind2])


acciones = acciones()
url = acciones.scrap_iol('https://iol.invertironline.com/mercado/cotizaciones')