import pandas as pd
import yfinance as yf
#funciones para manipular fechas y horas
import datetime
import time
#enviar solicitudes HTTP
import requests
#para manejar cadenas
import io

#defino el marco de tiempo del cual quier extraer información
start = datetime.datetime(2021,8,30)
end = datetime.datetime(2021,9,30)

#si quiero extraer las cotizaciones de una acción, utilixo el simbolo de la misma, yo quiero todas las cotizaciones de acciones que hay listadas, voy a usar un archivo csv con el listado.
#uso esto para convertirlo en un data frame
url="https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/7665719fb51081ba0bd834fde71ce822/nasdaq-listed_csv.csv"
s = requests.get(url).content
companies = pd.read_csv(io.StringIO(s.decode('utf-8')))


#extraigo los simbolos y los transformo en una lista, espero que funcione ;)
Symbols = companies['Symbol'].tolist()

# creamos el dataframe -sin datos/vacio-
stock_final = pd.DataFrame()
#vamos a repetir esta acción sobre cada simbolo con el -for-
for i in Symbols:
    #queremos imprimir el simbolo que supuestamente se está descargando-
    print( str(Symbols.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)
    #Descargamos el precio de la acciones - de las que se pueda y encuentre coincidencia-
    try:
        stock = []
        stock = yf.download(i,start=start, end=end, progress=False)
        #sumamos al df el precio individual de las acciones - esta parte literal la saque de un ejemplo- voy a añadir el link por el chat 
        if len(stock) == 0:
            None
        else:
            stock['Name']=i
            stock_final = stock_final.append(stock,sort=False)
    except Exception:
        None
stock_final.head()

#hasta este paso solo cree la tabla de cotizaciones de las acciones para luego poder trabajar con ellas
stock_final.to_csv('data_yfinance.csv')
