import pandas as pd 

yamete = [
    [1201, ("5464", 4, 25842.99), ("7854", 18, 23254.99), ("8521", 9, 48951.95)],
    [1202, ("8756", 3, 115362.58), ("1112", 18, 2354.99)],
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20),
     ("1254", 1, 13645.20), ("9965", 5, 1645.20)],
    [1204, ("9635", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 390.95)]
]
def ordenes(rutinaContable):

    obj = {}
    for i in rutinaContable:
        sum = 0
        for j in i:
            if (type(j) == tuple):
                sum += j[2]*j[1]
        obj[i[0]] = sum

    print('------------------------ Inicio Registro diario ---------------------------------')
    for k in obj:
        if obj[k] < 600000:
            obj[k] += 25000
        print(
            f'La factura {k} tiene un total en pesos de {"{:,.2f}".format(obj[k])}')
    print('-------------------------- Fin Registro diario ----------------------------------')
    
    



ordenes(yamete)