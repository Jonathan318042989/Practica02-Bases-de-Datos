import csv
import os.path
import pandas as pd
import sys
import datetime
import re
from Empleado import Empleado


class ArchivoEmpleado:
    
    global archivo
    dfEmpleado = pd.DataFrame(columns=["ID", "Nombres", "Apellido Materno", "Apellido Paterno", "Colonia", "Calle", "Numero", "CodigoPostal", "Telefonos", "Correo electronico", "Fecha de Nacimiento", "Puesto", "IDSucursal"])
    empleadoPath = "CSV/Empleados.csv"
    def __init__(self):
        global archivo

    def verificaExistenciaEmpleados(self):
        """
        Verificamos la existencia del archivo inicial
        """
        if(os.path.isfile("CSV/Empleados.csv")):
            return
        else:
            self.archivo = open("CSV/Empleados.csv", "a", newline='')
            self.inicializaEmpleados(self.archivo)

    
    def inicializaEmpleados(self, archivo):
        """
        Inicializamos el archivo
        """
        writer = csv.writer(archivo)
        writer.writerow(["ID", "Nombres", "Apellido Materno", "Apellido Paterno", "Colonia", "Calle", "Numero", "CodigoPostal", "Telefonos", "Correo electronico", "Fecha de Nacimiento", "Puesto", "IDSucursal"])
        archivo.close()

    def agregarEmpleado(self, empleado):
        """
        Agregamos un nuevo empleado
        """
        with open(self.empleadoPath, 'a', newline='') as archivo:
            writer = csv.writer(archivo)
            nuevoEmpleado =  [empleado.getID(), 
                             empleado.getNombres(), empleado.getApellidoMaterno(), empleado.getApellidoPaterno(), 
                             empleado.getColonia(), empleado.getCalle(), 
                             empleado.getNumero(), empleado.getCodigoPostal(),
                             empleado.getTelefono(), empleado.getCorreo(), empleado.getFechaDeNacimiento(), 
                             empleado.getPuesto(), empleado.getSucursal()]
            writer.writerow(nuevoEmpleado)
        
        archivo.close()

    def consultarEmpleado(self, id):
        """
        Consultamos un empleado con un id
        """
        data = pd.read_csv(self.empleadoPath, index_col= 'ID')
        sucursal = data.loc[id]
        return sucursal
    
    def eliminarEmpleado(self, id):
        """
        Eliminamos un empleado con un id
        """
        if(self.existeIDEmpleado(id)):
            data = pd.read_csv(self.empleadoPath)
            print(id)
            indice = data.index[data["ID"] == id]
            data.drop(indice, inplace=True)
            data.to_csv(self.empleadoPath, index= False) 
        else:
            print("No se encontro el ID") 

    def editarDato(self, id,columna, datoNuevo):
        """
        Editamos un empleado con un id
        """
        if(self.existeIDEmpleado(id)):
            data = pd.read_csv(self.empleadoPath, index_col= 'ID')
            data.loc[id, columna]  = datoNuevo
            data.to_csv(self.empleadoPath)
        else:
            print("No se encontro el ID")

    def editarListaTelefonos(self, id, opcion, datoNuevo):
        """
        Editamos la lista de telefonos de un empleado con un id
        """
        if(self.existeIDEmpleado(id)):
            if(opcion == 1):
                data = pd.read_csv(self.empleadoPath, index_col= 'ID')
                datoActual = data.loc[id, "Telefonos"]
                listaActual = datoActual.strip('][').split(', ')
                listaActual = list(map(int, listaActual))
                if(type(datoNuevo == int)):
                    listaActual.append(datoNuevo)
                    data.loc[id, "Telefonos"]  = str(listaActual)
                    data.to_csv(self.empleadoPath)
                else:
                    print("El telefono debe ser un numero")
            elif(opcion == 2):
                data = pd.read_csv(self.empleadoPath, index_col= 'ID')
                datoActual = data.loc[id, "Telefonos"]
                listaActual = datoActual.strip('][').split(', ')
                listaActual = list(map(int, listaActual))
                del listaActual[datoNuevo]
                data.loc[id, "Telefonos"]  = str(listaActual)
                data.to_csv(self.empleadoPath)
        else:
            print("No se encontro el ID")

    def editarListaCorreos(self, id, opcion, datoNuevo):
        """
        Editamos la lista de correos de un empleado con un id
        """
        if(self.existeIDEmpleado(id)):
            if(opcion == 1):
                data = pd.read_csv(self.empleadoPath, index_col= 'ID')
                datoActual = data.loc[id, "Correo electronico"]
                listaActual = datoActual.strip('][').split(', ')
                listaActual = list(map(str, listaActual))
                listaActual.append(datoNuevo)
                data.loc[id, "Correo electronico"]  = str(listaActual)
                data.to_csv(self.empleadoPath)
            elif(opcion == 2):
                data = pd.read_csv(self.empleadoPath, index_col= 'ID')
                datoActual = data.loc[id, "Correo electronico"]
                listaActual = datoActual.strip('][').split(', ')
                listaActual = list(map(str, listaActual))
                del listaActual[datoNuevo]
                data.loc[id, "Correo electronico"]  = str(listaActual)
                data.to_csv(self.empleadoPath)
        else:
            print("No se encontro el ID")
    
    def existeIDEmpleado(self,id):
        """
        Verificamos la existencia de un empleado con un id
        """
        with open(self.empleadoPath) as archivo:
            reader = csv.reader(archivo, delimiter=',')
            for row in reader:
                if (row[0] == id):
                    return True
            return False
        
    def imprimirOpciones(self):
        print("\t\tBienvenido al gestor de Sucursales.")
        print("\n\tOpciones:")
        print("A) Agregar empleado")
        print("B) Consultar empleado")
        print("C) Eliminar empleado")
        print("D) Editar empleado")
        print("E) Salir")
        print("Seleccione una opción:")

    id = ''
    nombreCompleto = ''
    nombres = ''
    apellidoMaterno = ''
    apellidoPaterno = ''
    direccion = ''
    telefonos = []
    fechaDeNacimiento = ''
    correos = []
    puesto = ''
    sucursal = ''

    def pedirFecha(self):
        fecha_valida = False
        while not fecha_valida:
            fecha_str = input("Introduce la fecha de nacimiento en formato dd/mm/aaaa: ")
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
                
                self.nombres = input("Ingrese nombre del empleado: ")
                self.apellidoMaterno = input("Ingrese el apellido materno del empleado: ")
                self.apellidoPaterno = input("Ingrese el apellido paterno del empleado: ")
                self.colonia = input("Ingrese la colonia de la direccion del empleado: ")
                self.calle = input("Ingrese la calle de la direccion del empleado: ")
                self.numero = int(input("Ingrese el numero de edificio de la direccion del empleado: "))
                self.codigoPostal = input("Ingrese el codigo postal de la direccion del empleado: ")
                self.telefonos = int(input("Ingrese un telefono del empleado: "))
                self.correos = input("Ingrese un correo del empleado: ")
                self.puesto = input("Ingrese el puesto del empleado: ")
                self.sucursal = input("Ingrese el id de la sucursal donde trabaja el empleado: ")
                if not self.colonia or not self.calle or not self.nombres or not self.codigoPostal or not self.apellidoMaterno or not self.apellidoPaterno :
                    print("ERROR: El nombre, apellidos, colonia o calle son obligatorios.")
                    continue
                if self.numero < 0:
                    print("ERROR: El numero de edificio debe ser un número entero positivo.")
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
                id = input("Ingrese el ID del empleado: ")
                if len(id) != 8:
                    print("ERROR: El ID debe tener 8 caracteres.")
                    continue
                break
            except ValueError:
                print("ERROR: Se esperaba un ID de logitud 8.")
        return str(id)


    def validar_columna(self, columna):
        opciones_validas = ["ID", "Nombres", "Apellido Materno", "Apellido Paterno", "Colonia", "Calle", "Numero", "CodigoPostal", "Telefonos", "Correo electronico", "Fecha de Nacimiento", "Puesto", "IDSucursal"]
        while columna not in opciones_validas:
            columna = input("Entrada inválida. Por favor, ingrese una columna válida: ")
        return columna
    



    def validar_dato_nuevo( columna):
        while True:
            datoNuevo = input("Ingrese el dato nuevo: ")
            if isinstance(datoNuevo, str) and (columna == 'Nombre' or
                                            columna == 'Colonia' or columna == 'Calle' or columna == 'CodigoPostal'
                                            or columna == 'ID' or columna == 'Apellido Materno' or columna == 'Apellido Paterno') :
                return datoNuevo
            elif isinstance(datoNuevo, int) and columna == 'Telefonos':
                return datoNuevo
            elif isinstance(datoNuevo, int) and columna == 'Numero':
                return datoNuevo
            elif isinstance(datoNuevo, str) and re.match(r'\d{2}/\d{2}/\d{4}', datoNuevo) and (columna== 'Fecha de Nacimiento'):
                return datoNuevo
            else:
                datoNuevo = input("Entrada inválida. Por favor, ingrese un dato válido: ")
        

    def menuEmpleado(self):
        try:
            while True:
                self.imprimirOpciones()
                opcion = input("Ingrese la opción que desea ejecutar: ").upper()
                if opcion == "A":
                    print('\nAgregar empleado')
                    self.verificaExistenciaEmpleados()
                    self.pedirDatos()
                    self.id = self.pedir_id()
                    self.fecha = self.pedirFecha()
                    empleadoNuevo = Empleado(self.id, self.nombres, self.apellidoMaterno, self.apellidoPaterno, self.colonia, self.calle, self.numero, self.codigoPostal, self.telefonos, self.correos, self.fecha, self.puesto, self.sucursal)
                    self.agregarEmpleado(empleadoNuevo)
                    break
                elif opcion == "B":
                    print('\n Consultar')
                    self.verificaExistenciaEmpleados()
                    id = self.pedir_id()
                    self.consultarEmpleado(id)
                elif opcion == "C":
                    print('\n Eliminar')
                    self.verificaExistenciaEmpleados()
                    id = self.pedir_id()
                    self.eliminarEmpleado(id)
                elif opcion == "D":
                    print('\n Editar')
                    print("\n\tOpciones:")
                    print("A) Editar Telefonos")
                    print("B) Editar cualquier otro dato")
                    print("C) Editar Correos")
                    opcion = input("Ingrese la opción que desea ejecutar: ").upper()
                    self.verificaExistenciaEmpleados()
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
                        column = input("Ingrese la columna a editar: ")
                        id = self.pedir_id()
                        datoNuevo = self.validar_dato_nuevo()
                        self.editarDato(id, column, datoNuevo)
                    elif(opcion == 'C'):
                        print("\n\tOpciones:")
                        print("1) Agregar correo")
                        print("2) Eliminar correo")
                        opcion = int(input("Ingrese la opción que desea ejecutar: "))
                        id = self.pedir_id()
                        if(opcion == 1):
                            tel = int(input("Ingrese un correo"))
                            self.editarListaCorreos(id, opcion, tel)
                        elif(opcion == 2):
                            indice = int(input("Ingrese el indice del correo a eliminar"))
                            self.editarListaCorreos(id, opcion, indice)
                    
                    
                elif opcion == "E":
                    print("\n¡Hasta luego!")
                    return
                else:
                    print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("ERROR: Algo paso!!")