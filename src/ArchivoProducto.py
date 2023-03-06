import pandas as pd
import csv
import os.path
import sys
from Producto import Producto



"""Data frame que almacenara los productos existentes"""
df_producto = pd.DataFrame(columns=['ID', 'Nombre','Stock', 'Marca','Presentacion',
                                    'Precio', 'Refrigeracion', 'FechaCad', 'FechaLab'])

""" 
Verifica si el archivo existe
:param str archivo: nombre del archivi a verficar existencia.
:return true si el archivo existe, false en otro caso.
"""
def exist_file( archivo):
    if(os.path.exists(archivo +".csv")):
        return True
    else:
        #En otro caso lo escribe
        return False




""" Lee un archivo csv y lo convierte a un dataframe
:param str archivo: Nombre del archivo a leer
:return dataframe con los datos del archiv"""    
def readCSV(archivo):
    df = pd.read_csv(archivo + ".csv",index_col=0) 
    return df



"""
Agrega producto a un dataframe existente y actualiza el archivo
csv
:param Producto producto: objeto producto a agregar.
:param str file : nombre del archivo que llevara cuando se guarde en csv.
:return dataframe con la informacion actualizada.
        
 """
def agregarProducto(producto, file):   
    global df_producto
    dataProducto =[  producto.get_id(),producto.get_nombre(),
                     producto.get_stock(), producto.get_marca(),
                     producto.get_presentacion(),
                     producto.get_precio(),
                     producto.get_refrigeracion(),
                     producto.get_fechCad(),
                     producto.get_fechLab()]
    #df_producto = readCSV(file )
   
    df_producto=pd.concat([df_producto,pd.DataFrame([dataProducto],columns=df_producto.columns)], ignore_index=True)#Añade en la ultima posicion
    #df.set_index('ID', inplace=True)
    df_producto.to_csv(file+".csv")
    
    
    return df_producto
    
"""
Incializa el archivo productos desde 0:
si no hay productos.

:param Producto producto: Objeto de la clase producto, el cual
será el primero en almacenar.
:param str archivoName: nombre que llevara el archivo csv cuando se 
genere.
:return dataframe inicializado.
"""    
def inicializaProducto(producto,archivoName):
    global df_producto
    dataProducto = [ producto.get_id(),producto.get_nombre(),
                     producto.get_stock(), producto.get_marca(),
                     producto.get_presentacion(),
                     producto.get_precio(),
                     producto.get_refrigeracion(),
                     producto.get_fechCad(),
                     producto.get_fechLab()]
    new_df= pd.DataFrame([dataProducto], columns=df_producto.columns)
    df_producto = pd.concat([df_producto, new_df],ignore_index=True)
    #df.reset_index(drop = True)
    #df.set_index('ID', inplace=True)
    #print(df)
    #genernando el archivo
    df_producto.to_csv(archivoName+'.csv')
    return df_producto

producto = Producto('XX1', 'Verduras', 34, 'Barcel', 'Bolsa', 24, False, '02-04-2023', '04-09-2019')
producto1 = Producto('XX2', 'Verduras', 54, 'Barcel', 'Lata', 64, False, '02-04-2023', '04-09-2019')



if exist_file('productosSuc102' ):
    df_producto = readCSV('productosSuc102')
    #df_producto.set_index('ID', inplace=True)
    df_producto =agregarProducto(producto1, 'productosSuc102')
    df_producto.to_csv('productosSuc102'+'.csv')
    print(df_producto)
else:
    df_producto = inicializaProducto(producto,'productosSuc102')
    print(df_producto)




#df_producto = agregarProducto(producto1,'productosSuc102')
#print(df_producto)
