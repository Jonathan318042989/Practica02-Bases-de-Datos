import csv
import os.path
import pandas as pd
import sys
import datetime
import re
from Sucursal import Sucursal


class ArchivoSucursal:
    
    global archivo
    sucursalPath = "CSV/Sucursales.csv"
    def __init__(self):
        global archivo

    def verificaExistenciaSucursales(self):
        """
        Verificamos la existencia del archivo inicial
        """
        if(os.path.isfile("CSV/Sucursales.csv")):
            self.archivo = open("CSV/Sucursales.csv", "a")
        else:
            self.archivo = open("CSV/Sucursales.csv", "a", newline='')
            self.inicializaSucursales(self.archivo)

    
    def inicializaSucursales(self, archivo):
        """
        Inicializamos el archivo
        """
        writer = csv.writer(archivo)
        writer.writerow(["ID", "NOMBRE", "COLONIA", "CALLE", "NUMERO", "CODIGO POSTAL", "TELEFONOS", "FECHA DE APERTURA"])
        archivo.close()

    def agregarSucursal(self, sucursal):
        """
        Agregamos una nueva sucursal
        """
        with open(self.sucursalPath, 'a', newline='') as archivo:
            writer = csv.writer(archivo)
            nuevaSucursal = [sucursal.getID(), sucursal.getNombre(),
                        sucursal.getColonia(), sucursal.getCalle(),
                            sucursal.getNumero(), sucursal.getCodigoPostal(),
                            sucursal.getTelefono(), sucursal.getFechaApertura()]
            writer.writerow(nuevaSucursal)
        
        archivo.close()

    def consultarSucursal(self, id):
        """
        Consultamos una sucursal con un id
        """
        data = pd.read_csv(self.sucursalPath, index_col= 'ID')
        sucursal = data.loc[id]
        return sucursal
    
    def eliminarSucursal(self, id):
        """
        Eliminamos una sucursal con un id
        """
        if(self.existeIDSucursal(id)):
            data = pd.read_csv(self.sucursalPath)
            print(id)
            indice = data.index[data["ID"] == id]
            data.drop(indice, inplace=True)
            data.to_csv(self.sucursalPath, index= False) 
        else:
            print("No se encontro el ID") 

    def editarDato(self, id,columna, datoNuevo):
        """
        Editamos una sucursal con un id
        """
        if(self.existeIDSucursal(id)):
            data = pd.read_csv(self.sucursalPath, index_col= 'ID')
            data.loc[id, columna]  = datoNuevo
            data.to_csv(self.sucursalPath)
        else:
            print("No se encontro el ID")

    def editarListaTelefonos(self, id, opcion, datoNuevo):
        """
        Editamos la lista de telefonos de una sucursal
        """
        if(self.existeIDSucursal(id)):
            if(opcion == 1):
                data = pd.read_csv(self.sucursalPath, index_col= 'ID')
                datoActual = data.loc[id, "TELEFONOS"]
                listaActual = datoActual.strip('][').split(', ')
                listaActual = list(map(int, listaActual))
                if(type(datoNuevo == int)):
                    listaActual.append(datoNuevo)

                    data.loc[id, "TELEFONOS"]  = str(listaActual)
                    data.to_csv(self.sucursalPath)
                else:
                    print("El telefono debe ser un numero")
            elif(opcion == 2):
                data = pd.read_csv(self.sucursalPath, index_col= 'ID')
                datoActual = data.loc[id, "TELEFONOS"]
                listaActual = datoActual.strip('][').split(', ')
                listaActual = list(map(int, listaActual))
                del listaActual[datoNuevo]
                data.loc[id, "TELEFONOS"]  = str(listaActual)
                data.to_csv(self.sucursalPath)
        else:
            print("No se encontro el ID")

    def existeIDSucursal(self,id):
        """
        Verificamos que exista una sucursal con cierto id
        """
        with open(self.sucursalPath) as archivo:
            reader = csv.reader(archivo, delimiter=',')
            for row in reader:
                if (row[0] == id):
                    return True
            return False
        
    def imprimirOpciones(self):
        print("\t\tBienvenido al gestor de Sucursales.")
        print("\n\tOpciones:")
        print("A) Agregar sucursal")
        print("B) Consultar sucursal")
        print("C) Eliminar sucursal")
        print("D) Editar sucursal")
        print("E) Salir")
        print("Seleccione una opción:")

    id = ''
    nombre = ''
    colonia = ''
    calle = ''
    codigoPostal = 0 
    numero = 0
    telefonos = []
    direccion = ''
    fecha = ''

    def pedirFecha(self):
        fecha_valida = False
        while not fecha_valida:
            fecha_str = input("Introduce la fecha de apertura en formato dd/mm/aaaa: ")
            try:
                dia, mes, anio = map(int, fecha_str.split('/'))
                fecha = datetime.date(anio, mes, dia)
                fecha_valida = True
            except ValueError:
                print("La fecha introducida no es válida. Inténtalo de nuevo.")
        return fecha

    def pedirDatos(self):
        while True:
            try:
                
                self.nombre = input("Ingrese nombre de la sucursal: ")
                self.colonia = input("Ingrese la colonia donde se ubica la sucursal: ")
                self.calle = input("Ingrese la calle donde se ubica la sucursal: ")
                self.numero = int(input("Ingrese el numero de edificio donde se ubica la sucursal: "))
                self.codigoPostal = input("Ingrese el codigo postal de donde se ubica la sucursal: ")
                self.telefonos = int(input("Ingrese un telefono de la sucursal: "))
                if not self.colonia or not self.calle or not self.nombre or not self.codigoPostal or not self.numero:
                    print("ERROR: El nombre, colonia o calle son obligatorios.")
                    continue
                if self.numero < 0:
                    print("ERROR: El numero debe ser sin signos")
                    continue
                if self.telefonos < 0:
                    print("ERROR: El telefono debe ser un número sin signos")
                    continue
                
                
                break
            except ValueError:
                print("ERROR: Se esperaba un número entero para Numero de edificio o telefono")
            
    def pedir_id(self):
        while True:
            try:
                id = input("Ingrese el ID de la sucursal: ")
                if len(id) != 8:
                    print("ERROR: El ID debe tener 8 caracteres.")
                    continue
                break
            except ValueError:
                print("ERROR: Se esperaba un ID de logitud 8.")
        return str(id)


    def validar_columna(self, columna):
        opciones_validas = ["ID", "NOMBRE", "COLONIA", "CALLE", "NUMERO", "CODIGO POSTAL", "TELEFONOS", "FECHA DE APERTURA"]
        while columna not in opciones_validas:
            columna = input("Entrada inválida. Por favor, ingrese una columna válida: ").upper()
        return columna
    



    def validar_dato_nuevo(self,  columna):
        while True:
            datoNuevo = input("Ingrese el dato nuevo: ")
            if isinstance(datoNuevo, str) and (columna == 'NOMBRE' or
                                            columna == 'COLONIA' or columna == 'CALLE' or columna == 'CODIGO POSTAL'
                                            or columna == 'ID') :
                return datoNuevo
            elif isinstance(datoNuevo, int) and columna == 'TELEFONOS':
                return datoNuevo
            elif isinstance(datoNuevo, int) and columna == 'NUMERO':
                return datoNuevo
            elif isinstance(datoNuevo, str) and re.match(r'\d{2}/\d{2}/\d{4}', datoNuevo) and (columna== 'FECHA DE APERTURA'):
                return datoNuevo
            else:
                datoNuevo = input("Entrada inválida. Por favor, ingrese un dato válido: ")
        

    def menuSucursal(self):
        try:
            while True:
                self.imprimirOpciones()
                opcion = input("Ingrese la opción que desea ejecutar: ").upper()
                if opcion == "A":
                    print('\nAgregar sucursal')
                    self.verificaExistenciaSucursales()
                    self.pedirDatos()
                    self.id = self.pedir_id()
                    self.fecha = self.pedirFecha()
                    sucursal = Sucursal(self.id, self.nombre, self.colonia, self.calle, self.numero, self.codigoPostal, self.telefonos, self.fecha)
                    self.agregarSucursal(sucursal)
                elif opcion == "B":
                    print('\n Consultar')
                    self.verificaExistenciaSucursales()
                    id = self.pedir_id()
                    print(self.consultarSucursal(id))
                elif opcion == "C":
                    print('\n Eliminar')
                    self.verificaExistenciaSucursales()
                    id = self.pedir_id()
                    self.eliminarSucursal(id)
                elif opcion == "D":
                    print('\n Editar')
                    print("\n\tOpciones:")
                    print("A) Editar Telefonos")
                    print("B) Editar cualquier otro dato")
                    opcion = input("Ingrese la opción que desea ejecutar: ").upper()
                    self.verificaExistenciaSucursales()
                    if(opcion == 'A'):
                        print("\n\tOpciones:")
                        print("1) Agregar telefono")
                        print("2) Eliminar telefono")
                        opcion = int(input("Ingrese la opción que desea ejecutar: "))
                        id = self.pedir_id()
                        if(opcion == 1):
                            tel = int(input("Ingrese un numero de telefono"))
                            self.editarListaTelefonos(id, opcion, tel)
                        elif(opcion == 2):
                            indice = int(input("Ingrese el indice del telefono a eliminar"))
                            self.editarListaTelefonos(id, opcion, indice)
                    elif(opcion == 'B'):
                        column = input("Ingrese la columna a editar: ").upper()
                        column = self.validar_columna(column)
                        id = self.pedir_id()
                        datoNuevo = self.validar_dato_nuevo(column)
                        self.editarDato(id, column, datoNuevo)
                elif opcion == "E":
                    print("\n¡Hasta luego!")
                    return
                else:
                    print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("ERROR: Algo paso!!")