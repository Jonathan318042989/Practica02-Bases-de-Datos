import pandas as pd
import os.path
from Producto import Producto



#Nombre del archivo csv que guardara los productos
filePath = "src/CSV/Productos.csv"


df_producto = pd.DataFrame(columns=['Id', 'Nombre','Stock', 'Marca','Presentacion',
                                    'Precio', 'Refrigeracion', 'FechaCad', 'FechaLab'])


#df_producto.set_index('Id')

def exist_file( ):
   """ 
   Verifica si el archivo existe
   :return true si el archivo existe, false en otro caso.
   """
   return os.path.exists(filePath)





def readCSV():
    """ Lee un archivo csv y lo convierte a un dataframe
    :return dataframe con los datos del archiv"""    
    global filePath
    df = pd.read_csv(filePath, index_col=0) 
    return df




def agregarProducto(producto):
    """
    Agrega producto a un dataframe existente y actualiza el archivo
    csv
    :param Producto producto: objeto producto a agregar.
    :return dataframe con la informacion actualizada.
    """   
    global df_producto
    global filePath
    dataProducto =[  producto.get_id(),producto.get_nombre(),
                     producto.get_stock(), producto.get_marca(),
                     producto.get_presentacion(),
                     producto.get_precio(),
                     producto.get_refrigeracion(),
                     producto.get_fechCad(),
                     producto.get_fechLab()]
   
   
    df_producto=pd.concat([df_producto,pd.DataFrame([dataProducto] , index = [producto.get_id()],columns=df_producto.columns)], ignore_index=False)#Añade en la ultima posicion
   
    df_producto.to_csv(filePath, index_label='Id')
    
    
    return df_producto
    

def inicializaProducto():
    """
    Incializa el archivo productos desde 0:
    si no hay productos.
    Genera el archivo Producto.csv
    """    
    global df_producto
    global filePath
    
    df_producto.to_csv(filePath)

#El archivo ya debe estar cargado con los IDS como indices


def consultaProducto(id):
    """
    Consulta un producto proporcionando ID
    :param str id: Id del producto.
    :return : regresa el producto corrrespondiente al id.
    """
    producto = df_producto.loc[id]
    return producto
    


#El archivo ya debe estar cargado

def eliminarProducto(id):
    """ 
    Eliminia un producto dado el id
    :param str id: Id del producto
    """
    global df_producto
    df_producto.drop(index=id, inplace=True)
    df_producto.to_csv(filePath, index_label='Id')
    


#El archivo ya debe estar cargado con el Id como indice
def editarDato(id, columna, datoNuevo):
    df_producto.loc[id, columna] = datoNuevo
    df_producto.to_csv(filePath,index_label='Id')
    
    


#---------------------------------------------------------------

producto = Producto('XX1', 'Verduras', 34, 'Barcel', 'Bolsa', 24, False, '02-04-2023', '04-09-2019')
producto1 = Producto('XX2', 'Verduras', 54, 'Barcel', 'Lata', 64, False, '02-04-2023', '04-09-2019')
producto3 = Producto('XX3', 'Leche', 75, 'Santa Clara', 'Carton', 34, False, '02-04-2023', '04-09-2019')


"""
if exist_file():
    df_producto = readCSV()
    df_producto = agregarProducto(producto3)
    print(df_producto)
   
    
    print(df_producto.shape[1])
else: 
    inicializaProducto()
    print(df_producto)
    
    
"""    

#Probando consulta
"""
df_producto = readCSV()
print('Consulta producto XX3')
print(consultaProducto('XX3'))
"""



#Probando eliminar filas
"""
df_producto = readCSV()
print(df_producto)
print('Eliminando XX2')
print(eliminarProducto('XX2'))

"""

#Probando editar datos
""""
df_producto = readCSV()
print(df_producto)
editarDato('XX1', 'Nombre', 'Papas fritas')
print(df_producto)
"""