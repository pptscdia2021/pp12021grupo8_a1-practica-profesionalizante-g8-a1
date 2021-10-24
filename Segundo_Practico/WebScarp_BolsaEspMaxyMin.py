# Importamos la librería para hacer peticiones http
import requests
import pandas as pd
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
#tabla = soup.find('tr', attrs={'td': ''})

#print(tabla)

name=[]
price=[]

max =[]
min =[]
date =[]

nroFila=0
for fila in tabla.find_all("tr"):
    for i in range (77):
        if nroFila==i:
            nroCelda=i-1
            for celda in fila.find_all('td'):
                if nroCelda==i-1:
                    name.append(celda.text)

                    #print("Indice:", name[i-1])
                if nroCelda==i+1:
                    # Quito el "." del valor para cambiar a float
                    valorS = (celda.text).replace(".","")
                    # le saco los 3 caracteres al valor q son la ,00 y lo convierto a Entero
                    valorFloat = int(valorS[slice(-3)])
                    # agrego a la lista precio el valor
                    price.append(valorFloat)
                    # muestro por pantalla el valor de la accion recorrida
                    #print("Valor Último:", price[i-1])
                if nroCelda==i+3:
                    max.append(celda.text)
                    #print("Maximo: "+celda.text)
                if nroCelda==i+4:
                    min.append(celda.text)
                   # print("Minimo: "+celda.text)
                if nroCelda==i+5:
                    date.append(celda.text)
                  #  print("Fecha: ",celda.text)
                nroCelda=nroCelda+1
    nroFila=nroFila+1

# Imprimo el nombre de la accion a cual pertenece el precio maximo
#print(max(price))
#Ordeno de menor a mayor para obtener el primero y el último
maximum = 0
minimum = price[0]
accionmin = ""
accionmax = ""
for i in range(len(price)):
    if price[i] > maximum:
        maximum = price[i]
        accionmax = name[i]

for i in range(len(price)):
    if price[i] < minimum:
        minimum = price[i]
        accionmin = name[i]

#use dos for porque me seguia tirando el error de list object is not callable
print("El precio máximo es: ", maximum, "La acción correspondiente es: ",accionmax)
print("El precio mínimo es: ", minimum, "La acción correspondiente es: ",accionmin)

#indN = price.index(min(price))
#print("La acción a quien le corresponde el precio maximo es: ",name[len(price)-1])
# imprimo el precio maximo
#print("precio máximo: ", (price[len(price)-1]))

#print("La accion a quien le corresponde el precio minimo es: ",name[0])
#print("precio maximo: ", price[0])

# Sobreescribimos el csv

#listDetalle = [["Accion", "Precio minimo del dia", "Precio Maximo del dia" ], [name[indN], min(price), ''], [name[indM], '', max(price)]]
listDetalle2 = {'Nombre':name,'Precio último':price,'Máximo':max,'Mínimo':min,'Fecha':date}

#crear dataframe

df_accio = pd.DataFrame(listDetalle2)
print("DATA FRAME_---_-----------------------------------------------------------")
print(df_accio)
df_accio.to_csv('preciosacciones.csv', index=False)

#myFile = open('./Segundo_Practico/preciosacciones.csv', 'w')

#for row in listDetalle2:
 #   for column in row:
  #      myFile.write('%s;' % column)
   # myFile.write('\n')
#myFile.close()

print("Writing complete")

