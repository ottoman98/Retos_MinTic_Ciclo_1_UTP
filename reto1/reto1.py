
def CDT(usuario, capital, tiempo):

    if(tiempo <= 2):
        perdida = capital-(0.02*capital)
        return f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {perdida}'
    elif(tiempo > 2):
        ganancia = capital+((capital*0.03*tiempo)/12)
        return f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {ganancia}'


print(CDT('AB1012', 1000000, 3))
