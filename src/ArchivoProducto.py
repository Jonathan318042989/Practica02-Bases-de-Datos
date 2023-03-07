import pandas as pd
import os.path
from Producto import Producto
import uuid
import numpy as np
import datetime
import re

#Nombre del archivo csv que guardara los productos
filePath = "src/CSV/Productos.csv"


df_producto = pd.DataFrame(columns=['ID', 'NOMBRE','STOCK', 'MARCA','PRESENTACION','PRECIO', 'REFRIGERACION', 'FECHACAD', 'FECHAELAB'])


def exist_file():
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




def generar_id():
    """ 
    Genera un id numero de 8 elementos.
    :return id generado
    """
    uid = uuid.uuid4().int & (10**8 - 1)
    return str(uid).zfill(8)

#Considerando  que df ya esta cargado
def existe_id(id):
    """Determina si el id que pasa como parametro 
       ya existe en los productos registrados en el dataframe
    Args:
        id (str): Id a verficar existencia

    Returns:
        bool: true si existe, false en otro caso
    """
    global df_producto
    df_producto.index = df_producto.index.astype(str)
    return id in df_producto.index
    

def generar_id_unico():
    """ 
    Genera un id unico
    :retunr: str id unico
    """
    id_unico = generar_id()
    while existe_id(id):
        id_unico =generar_id()
    return id_unico
        
    
def agregarProducto(producto):
    """
    Agrega producto a un dataframe existente y actualiza el archivo
    csv
    :param Producto producto: objeto producto a agregar.
    :return dataframe con la informacion actualizada.
    """   
    global df_producto
    global filePath
    # Asignar id unico a producto 
    producto.set_id(generar_id_unico())
    dataProducto =[  producto.get_id(),producto.get_nombre(),
                     producto.get_stock(), producto.get_marca(),
                     producto.get_presentacion(),
                     producto.get_precio(),
                     producto.get_refrigeracion(),
                     producto.get_fechCad(),
                     producto.get_fechLab()]
   
   
    df_producto=pd.concat([df_producto,pd.DataFrame([dataProducto] , index = [producto.get_id()],columns=df_producto.columns)], ignore_index=False)#Añade en la ultima posicion
    df_producto.to_csv(filePath, index_label='ID')
    return df_producto
    

def inicializaProducto():
    """
    Incializa el archivo productos desde 0:
    si no hay productos.
    Genera el archivo Producto.csv
    """    
    global df_producto
    global filePath
    
    df_producto.to_csv(filePath,index_label='ID', header=True)
    return df_producto

#El archivo ya debe estar cargado con los IDS como indices


def consultaProducto(id):
    """
    Consulta un producto proporcionando ID
    :param str id: Id del producto.
    :return : regresa el producto corrrespondiente al id.
    """
    
    if existe_id(id):
        df_producto.index = df_producto.index.astype(str)
        print(df_producto.loc[id])
    else:
        print('\nEl producto no existe en el registro')
    
    

#El archivo ya debe estar cargado

def eliminarProducto(id):
    """ 
    Eliminia un producto dado el id
    :param str id: Id del producto
    """
    global df_producto
    if existe_id(id):
        df_producto.drop(index=id, inplace=True)
        df_producto.to_csv(filePath, index_label='ID')
        print('\nProducto eliminado exitosamente!!')
    else:
        print('\nEl producto con el id:' +  id + ' no existe.' )


#El archivo ya debe estar cargado con el Id como indice
def editarDato(id, columna, datoNuevo):
    """ Edita el dato de la celda dada su columna e id
    :param str id: id del producto
    :param  str columna: columna de la celda a modificar
    :para nuevo dato: nuevo dato con el que se reemplazará"""
    global df_producto
    if existe_id(id):
        df_producto.loc[df_producto.index == id, columna] = datoNuevo
        df_producto.to_csv(filePath, index_label='ID')
        print('\nEdicion de dato completada')
    else:
        print('\nEl producto con ese id no existe')
    
    

def agregar_producto(producto):
    """ Auxiliar para  el menu :agregar producto
    :param Producto  a agregar"""
    global df_producto
    #verficar si el producto existe
    if existe_id(producto.get_id()):
        print('Ese producto ya existe en el  registro')
        return 
    else: #Si no existe
        if exist_file():#si el archivo existe leer y agregar producto
            df_producto = readCSV()
            df_producto = agregarProducto(producto)
            print("\n\t El producto se agrego exitosamente!!\n ")
            print(df_producto)
        else: 
            df_producto=  inicializaProducto() #Si no, incializar y agregar
            df_producto = agregarProducto(producto)
            print("\n\t El producto se agrego exitosamente!! \n")
            print(df_producto)
        
    

#---------------------------------------------------------------





def imprimir_opciones():
    """ Imprime opciones del menu"""
    print("\t\tBienvenido al gestor de productos.")
    print("\n\tOpciones:")
    print("A) Agregar producto")
    print("B) Consultar producto")
    print("C) Eliminar producto")
    print("D) Editar producto")
    print("E) Salir")
    print("Seleccione una opción:")

#Datos de producto del usuario

nombre = ''
apellido_paterno = ''
apellido_materno  = ''
stock = -1
precio = 0
refrigeracion = False
marca = ''
presentacion = ''

def pedirFecha(nameFecha):
    """ Solicita cadena con formato de fecha
    :param str que indica si es la fecha de caducidad o elaboracion
    :return datetime.date fecha valida"""
    
    fecha_valida = False
    while not fecha_valida:
        fecha_str = input("Introduce la fecha de " + nameFecha+ " en formato dd/mm/aaaa: ")
        try:
            dia, mes, anio = map(int, fecha_str.split('/'))
            fecha = datetime.date(anio, mes, dia)
            fecha_valida = True
        except ValueError:
            print("La fecha introducida no es válida. Inténtalo de nuevo.")
    return fecha



def pedirDatos():
    """ 
    Solicita los datos atributos para producto
    
    """
    global nombre
    global stock
    global precio
    global refrigeracion
    global marca
    global presentacion
    while True:
        try:
            
            nombre = input("Ingrese nombre del producto: ").upper()
            stock = int(input("Ingrese el stock disponible: "))
            precio = float(input("Ingrese el precio: "))
            marca = input("Ingrese la marca del producto: ").upper()
            presentacion = input("Ingrese presentacion del producto: ").upper()
            refrigeracion = input("¿Tiene refrigeración? (S/N): ").upper() == "S"
            # Verificar que el apellido paterno, materno y nombre no estén vacíos
            if not marca or not presentacion or not nombre:
                print("ERROR: La marca, presentacion y nombre son obligatorios.")
                continue
            # Verificar que el stock sea un número entero positivo
            if stock < 0:
                print("ERROR: El stock debe ser un número entero positivo.")
                continue
            # Verificar que el precio sea un número float positivo
            if precio < 0:
                print("ERROR: El precio debe ser un número positivo.")
                continue
            # Verificar que la opción de refrigeración sea válida
            if refrigeracion not in [True, False]:
                print("ERROR: La opción de refrigeración debe ser 'S' o 'N'.")
                continue
            
            
            # Si todos los datos son válidos, salir del bucle
            break
        except ValueError:
            # Si se produce un error al convertir los datos a los tipos correctos, mostrar un mensaje de error y volver a solicitar los datos.
            print("ERROR: Se esperaba un número entero para stock, un número decimal para precio y 'S' o 'N' para refrigeración.")
           
def pedir_id():
    """ 
    Solicita id valido al usuario
    :return str id valido
    """
    while True:
        try:
            id = input("Ingrese el ID del producto: ")
            # Verificar que la longitud del ID sea 8
            if len(id) != 8:
                print("ERROR: El ID debe tener 8 dígitos.")
                continue
            # Verificar que el ID sea numérico
            if not id.isnumeric():
                print("ERROR: El ID debe ser numérico.")
                continue
            # Si todos los datos son válidos, salir del bucle
            break
        except ValueError:
            # Si se produce un error al convertir los datos a los tipos correctos, mostrar un mensaje de error y volver a solicitar los datos.
            print("ERROR: Se esperaba un ID numérico de 8 dígitos.")
    return str(id)


def validar_columna():
    """ 
    Valida  que la columna sea valida
    :return str columna valida
    """
    while True:
        try:
            columna = input("Ingrese columna a modificar dato:").upper()
            opciones_validas = ['NOMBRE', 'STOCK', 'MARCA', 'PRESENTACION', 'PRECIO', 'REFRIGERACION', 'FECHACAA', 'FECHAELAB']
            if columna in opciones_validas:
                return columna.upper()
        except Exception:
            print('\nAlgo hiciste mal, intenta otra vez.')



import re

def validar_dato_nuevo(columna):
    """ Valida el dato nuevo para editarDato()
    :param str columna: columna a la que pertence el dato nuevo
    :return dato nuevo correspondiente a la columna
    """
    while True:
        datoNuevo = input(f"Ingrese el dato nuevo para la columna "+ columna + ": ")
        try:
            if columna in ['NOMBRE', 'MARCA', 'PRESENTACION']:
                datoNuevo = str(datoNuevo)
            elif columna == 'STOCK':
                datoNuevo = int(datoNuevo)
            elif columna == 'PRECIO':
                datoNuevo = float(datoNuevo)
            elif columna == 'REFRIGERACION':
                datoNuevo = bool(datoNuevo)
            elif columna  =='FECHACAD':
                datoNuevo = pedirFecha('caducidad')
            elif columna == 'FECHAELAB':
                datoNuevo = pedirFecha('elaboracion')   
            else:
                raise ValueError
            return datoNuevo
        except ValueError:
            print(f"Entrada inválida para {columna}. Por favor, ingrese un dato válido.")


def auxEditData():
    global df_producto
    df_producto = readCSV()
    id = pedir_id()
    col = validar_columna()
    data = validar_dato_nuevo(col)
    
    editarDato(id, col, data)
    

def menuProductos():
    try:
        while True:
            imprimir_opciones()
            opcion = input("Ingrese la opción que desea ejecutar: ").upper()
            if opcion == "A":
                # Código para agregar producto
                # ##pedir datos
                print('\nAgregar producto:')
                pedirDatos()
                fechaCad = pedirFecha('caducidad')
                fechaElab = pedirFecha('Elaboracion')
                #Crear producto
                producto = Producto(' ', nombre, stock, precio, marca,presentacion, refrigeracion, fechaCad,fechaElab)
              
                #Añadir
                agregar_producto(producto)
                break
            elif opcion == "B":
                # Código para consultar producto
                print('\nConsultar:')
                id = pedir_id()
                df_producto = readCSV()
                consultaProducto(id)
                break
            elif opcion == "C":
                # Código para eliminar producto
                print('\nEliminar:')
                df_producto = readCSV()
                id = pedir_id()
                eliminarProducto(id)
                
                break
            elif opcion == "D":
                print('\nEditar: \n\tPara editar refrigeracion debe ingresar True (Si) o False (No)')
                auxEditData()
                break 
            elif opcion == "E":
                print("\n¡Hasta luego!")
                return
            else:
                print("Opción inválida. Intente de nuevo.")
    except Exception as e:
        # Si se produce un error al convertir los datos a los tipos correctos, mostrar un mensaje de error y volver a solicitar los datos.
        print("ERROR: Algo paso!!\t" + e)
    


menuProductos()

   
    
