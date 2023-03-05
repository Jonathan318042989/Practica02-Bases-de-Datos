class Sucursal:
    #Definimos los datos que lleva una Sucursal
    id = ''
    nombre = ''
    colonia = ''
    calle = ''
    codigoPostal = 0 
    numero = 0
    telefonos = []
    direccion = ''
    def __init__(self):
        """
        Se asignan valores iniciales de las variables
        """
        self.id = ''
        self.nombre = ''
        self.colonia = ''
        self.calle = ''
        self.codigoPostal = '' 
        self.numero = 0
        self.telefonos = []
        self.direccion = ''

    def setNombre(self, nombre):
            """
            Se le asigna nombre a una sucursal
            :param str nombre: Nombre de la sucursal
            """
            self.nombre = nombre
        
    def setDireccion(self, colonia, calle, codigoPostal, numero):
            """
            Se asigna la direccion de la sucursal
            :param str colonia: Colonia donde se ubica la sucursal
            :param str calle: Calle donde se encuentra la sucursal
            :param str codigoPostal: Codigo Postal de donde se encuentra la sucursal
            :param int numero: Numero del edificio de la sucursal
            """
            self.setColonia(self, colonia)
            self.setCalle(self, calle)
            self.setCodigoPostal(self, codigoPostal)
            self.setNumero(self, numero)
            self.direccion = colonia + ', ' + calle + ', ' +  self.getNumero(self) + ', ' + self.setCodigoPostal()

    def setColonia(self, colonia):
            """
            Se asigna la colonia de la sucursal
            :param str Colonia: Colonia donde se ubica la sucursal
            """
            self.colonia = colonia

    def setCalle(self, calle):
            """
            Se asigna la calle de la sucursal
            :param str calle: Calle donde se ubica la sucursal
            """
            self.calle = calle

    def setCodigoPostal(self, codigoPostal):
            """
            Se asigna el Codigo Postal de la sucursal
            :param str codigoPostal: Codigo postal de la sucursal
            """
            self.codigoPostal = codigoPostal

    def setNumero(self, numero):
            """
            Se asigna el numero de edificio de la sucursal
            :param int numero: Numero del edificio de la sucursal
            """
            if type(numero) != int:
                print('El numero de edificio debe ser un numero, no una cadena')
            else:
                self.numero = '#' + str(numero)

    def setTelefono(self, telefono):
            """
            Se asigna un numero de telefono a la sucursal (esta puede tener varios)
            :param str telefono: Telefono que utiliza la sucursal
            """
            if type(telefono) != int:
                print('El numero de telefono debe ser un numero, no una cadena')
            else:
                self.telefonos.append(telefono)       
                
    def setID(self, id):
            """
            Se asigna un ID único a la sucursal
            :param str id: ID único de la sucursal
            """
            self.id = id

    def getNombre(self):
            """
            Devuelve el nombe de la sucursal
            """
            return self.nombre
        
    def getDireccion(self):
            """
            Devuelve la direccion de la sucursal
            """
            return self.direccion
        
    def getColonia(self):
            """
            Devuelve el nombre de la colonia donde se encuentra la sucursal
            """
            return self.colonia

    def getCalle(self):
            """
            Devuelve el nombre de la calle donde se encuentra la sucursal
            """
            return self.calle

    def getCodigoPostal(self):
            """
            Devuelve el codigo postal de donde se encuentra la sucursal
            """
            return self.codigoPostal

    def getNumero(self):
            """
            Devuelve el numero del edificio donde se encuentra la sucursal
            """
            return self.numero

    def getTelefono(self):
            """
            Devuelve los numeros de telefono registrados para la sucursal
            """
            return self.telefonos
        
    def getID(self):
            """
            Devuelve el ID de la sucursal
            """
            return self.id