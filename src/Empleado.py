class Empleado:
    #Definimos los datos que tiene un empleado
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

    def __init__(self, id, nombres, apellidoMaterno, apellidoPaterno, colonia, calle, numero, codigoPostal, telefonos, correo, fechaNacimiento):
            """
            Se asignan valores iniciales de las variables
            """
            self.setID(id)
            self.setNombre(nombres, apellidoMaterno, apellidoPaterno)
            self.setDireccion(colonia, calle, codigoPostal, numero)
            self.setNumero(numero)
            self.correos = []
            self.setCorreo(correo)
            self.telefonos = []
            self.setTelefono(telefonos)
            self.setFechaDeNacimiento(fechaNacimiento)

    def setNombre(self, nombres, apellidoMaterno, apellidoPaterno):
            """
            Se asigna el nombre del empleado
            :param str nombre: Nombre del empleado
            """
            self.setNombres(self, nombres)
            self.setApellidoMaterno(self, apellidoMaterno)
            self.setApellidoPaterno(self, apellidoPaterno)
            self.nombreCompleto = nombres + ' ' + apellidoMaterno + ' ' +  apellidoPaterno
            
    def setNombres(self, nombres):
            """
            Se asigna el nombre o nombres del empleado
            :param str nombres: Nombre(s) del empleado
            """
            self.nombres = nombres
     
    def setApellidoMaterno(self, apellidoMaterno):
            """
            Se asigna el apellido materno del empleado
            :param str apellidoMaterno: Apellido materno del empleado
            """
            self.apellidoMaterno = apellidoMaterno
            
    def setApellidoPaterno(self, apellidoPaterno):
            """
            Se asigna el apellido paterno del empleado
            :param str apellidoPaterno: Apellido paterno del empleado
            """
            self.apellidoPaterno = apellidoPaterno

    def setDireccion(self, colonia, calle, codigoPostal, numero):
            """
            Se asigna la direccion del empleado
            :param str colonia: Colonia de la direccion del empleado
            :param str calle: Calle de la direccion del empleado
            :param str codigoPostal: Codigo postal de la direccion del empleado
            :param int numero: Numero de la direccion del empleado
            """
            self.setColonia(self, colonia)
            self.setCalle(self, calle)
            self.setCodigoPostal(self, codigoPostal)
            self.setNumero(self, numero)
            self.direccion = colonia + ', ' + calle + ', ' +  str(numero) + ', ' + codigoPostal

    def setColonia(self, colonia):
            """
            Se asigna la colonia de la direccion del empleado
            :param str colonia: Colonia de la direccion del empleado
            """
            self.colonia = colonia

    def setCalle(self, calle):
            """
            Se asigna la calle de la direccion del empleado
            :param str calle: Calle de la direccion del empleado
            """
            self.calle = calle

    def setCodigoPostal(self, codigoPostal):
            """
            Se asigna el codigo postal de la direccion del empleado
            :param str codigoPostal: Codigo postal de la direccion del empleado
            """
            self.codigoPostal = codigoPostal

    def setNumero(self, numero):
            """
            Se asigna el numero de la direccion del empleado
            :param str numero: Numero de la direccion del empleado
            """
            if type(numero) != int:
                print('El numero de edificio debe ser un numero, no una cadena')
            else:
                self.numero = '#' + str(numero)

    def setTelefono(self, telefono):
            """
            Se asigna un numero de telefono al empleado (este puede tener varios)
            :param str telefono: Telefono que utiliza el empleado
            """
            if type(telefono) != int:
                print('El numero de telefono debe ser un numero, no una cadena')
            else:
                self.telefonos.append(telefono) 

    def setCorreo(self, correo):
            """
            Se asigna un correo electrónico al empleado (este puede tener varios)
            :param str correo: Telefono que utiliza el empleado
            """
            if type(correo) != str:
                print('El correo debe ser una cadena')
            else:
                self.correos.append(correo) 
                
    def setID(self, id):
            """
            Se asigna un ID único al empleado
            :param str id: ID unico del empleado
            """
            self.id = id
    
    def setFechaDeNacimiento(self, fechaDeNacimiento):
            """
            Se asigna la fecha de nacimiento del empleado
            :param str fechaDeNacimiento: Fecha de nacimiento del empleado
            """
            self.fechaDeNacimiento = fechaDeNacimiento

    def setPuesto(self, puesto):
            """
            Se asigna el puesto del empleado
            :param str puesto: Puesto en el que trabaja el empleado
            """
            self.puesto = puesto

    def setSucursal(self, sucursal):
            """
            Se asigna el sucursal del empleado
            :param str sucursal: Sucursal donde trabaja el empleado
            """
            self.sucursal = sucursal

    def getNombreCompleto(self):
            """
            Devuelve el nombre completo del empleado
            """
            return self.nombreCompleto
        
    def getNombres(self):
            """
            Devuelve el nombre del empleado
            """
            return self.nombres
        
    def getApellidoMaterno(self):
            """
            Devuelve el apellido materno del empleado
            """
            return self.apellidoMaterno
        
    def getApellidoPaterno(self):
            """
            Devuelve el apellido paterno del empleado
            """
            return self.apellidoPaterno
    
    def getDireccion(self):
            """
            Devuelve la direccion de domicilio del empleado
            """
            return self.direccion
    
    def getColonia(self):
            """
            Devuelve la colonia de la direccion
            """
            return self.colonia

    def getCalle(self):
            """
            Devuelve la calle de la direccion
            """
            return self.calle
    
    def getCodigoPostal(self):
            """
            Devuelve la calle de la direccion
            """
            return self.codigoPostal
    
    def getNumero(self):
           """
           Devuelve el numero de la direccion
           """
           return self.numero
    
    def getTelefono(self):
           """
           Devuelve los numeros de telefono registrados para el empleado
           """
           return self.telefonos
    
    def getID(self):
            """
            Devuelve el ID del empleado
            """
            return self.id
    
    def getCorreo(self):
           """
           Devuelve el correo del empleado
           """
           return self.correos
    
    def getPuesto(self):
           """
           Devuelve el puestp del empleado
           """
           return self.puesto
    
    def getSucursal(self):
           """
           Devuelve la sucursal donde trabaja el empleado
           """
           return self.sucursal
