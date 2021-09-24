# Importamos la librería para hacer peticiones http
import requests
# Importamos la librería para "enterder" el html
from bs4 import BeautifulSoup

import csv
from datetime import datetime


# Definimos la url que queremos pedir
url_page = 'http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'

# tarda 480 milisegundos
page = requests.get(url_page).text
soup = BeautifulSoup(page, "lxml")

# Hacemos la petición
tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblÍndices'})
# tabla = soup.find('tr', attrs={'td': ''})
# print(tabla)

name=[]
price=[]
nroFila=0
for fila in tabla.find_all("tr"):
    for i in range (77):
        if nroFila==i:
            nroCelda=i-1
            for celda in fila.find_all('td'):
                if nroCelda==i-1:
                    name.append(celda.text)
                    print("Indice:", name[i-1])
                if nroCelda==i+1:
                    # Quito el "." del valor para cambiar a float
                    valorS = (celda.text).replace(".","")
                    # le saco los 3 caracteres al valor q son la ,00 y lo convierto a Entero
                    valorFloat = int(valorS[slice(-3)])
                    print(valorFloat)
                    # agrego a la lista precio el valor
                    price.append(valorFloat)
                    # muestro por pantalla el valor de la accion recorrida
                    print("Valor:", price[i-1])
                nroCelda=nroCelda+1
    nroFila=nroFila+1

# Imprimo el nombre de la accion a cual pertenece el precio maximo
ind = price.index(max(price))
print("La accion a quien le corresponde el precio maximo es: ",name[ind])
# imprimo el precio maximo
print("precio maximo: ", max(price))