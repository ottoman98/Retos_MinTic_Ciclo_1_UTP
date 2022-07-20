
def AutoPartes(ventas):
    object_array = []

    for x in ventas:
        obj = {     }
        obj['IdProducto'] = x[0]
        obj['dProducto'] = x[1]
        obj['pnProducto'] = x[2]
        obj['cvProducto'] = x[3]
        obj['sProducto'] = x[4]
        obj['nComprador'] = x[5]
        obj['cComprador'] = x[6]
        obj['fVenta'] = x[7]

        object_array.append(obj)

    return object_array


def consultaRegistro(ventas, idProducto):
    callback = ventas
    filter_array = []
    for c in callback:
        if(c['IdProducto'] == idProducto):
            string = f'''Producto consultado : {c['IdProducto']}  Descripción  {c['dProducto']}  #Parte  {c['pnProducto']}  Cantidad vendida  {c['cvProducto']}  Stock  {c['sProducto']}  Comprador {c['nComprador']}  Documento  {c['cComprador']}  Fecha Venta  {c['fVenta']}'''
            filter_array.append(string)

            print(string)
    if(len(filter_array)<=0):
        print('No hay registro de venta de ese producto')


consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 234234)

