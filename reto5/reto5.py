import pandas as pd
rutaFileCsv = 'https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv'


def listaPeliculas(ruta):
    if(ruta[-4:] == '.csv'):
        try:
            read = pd.read_csv(ruta)
            df = read.pivot_table(index=['Country', 'Language'], values='Gross Earnings')
            return df.head(10)
        except:
            return 'Error al leer el archivo de datos.'
    else:
        return'Extensión inválida.'


print(listaPeliculas(rutaFileCsv))
