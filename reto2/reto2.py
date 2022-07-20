def cliente(informacion):
    x_treme = 20000
    carros_chocones = 5000
    sillas_voladoras = 10000
    x_treme_descuento = 0.05
    carros_chocones_descuento = 0.07
    sillas_voladoras_descuento = 0.05
    status = {
        'nombre': None,
        'edad': None,
        'atraccion': None,
        'apto': None,
        'primer_ingreso': None,
        'total_boleta': None}
    status['nombre'] = informacion['nombre']
    status['edad'] = informacion['edad']
    status['primer_ingreso'] = informacion['primer_ingreso']
# x-treme
    if(status['edad'] > 18):
        status['atraccion'] = 'X-Treme'
        status['apto'] = True
        if(informacion['primer_ingreso'] == True):
            status['total_boleta'] = x_treme*(1-x_treme_descuento)
        else:
            status['total_boleta'] = x_treme
# carros chocones
    elif(15 <= status['edad'] <= 18):
        status['atraccion'] = 'Carros chocones'
        status['apto'] = True
        if(informacion['primer_ingreso'] == True):
            status['total_boleta'] = carros_chocones * (1-carros_chocones_descuento)               
        else:
            status['total_boleta'] = carros_chocones
# sillas voladoras
    elif(7 <= status['edad'] < 15):
        status['atraccion'] = 'Sillas voladoras'
        status['apto'] = True
        if(informacion['primer_ingreso'] == True):
            status['total_boleta'] = sillas_voladoras*(1-sillas_voladoras_descuento)               
        else:
            status['total_boleta'] = sillas_voladoras
    else:
        status['atraccion'] = 'N/A'
        status['apto'] = False
        status['total_boleta'] = 'N/A'
    return status


informacion = {
    'id_cliente': 4,
    'nombre': 'Johana Fernandez',
    'edad': 14,
    'primer_ingreso': True
}

print(cliente(informacion))
