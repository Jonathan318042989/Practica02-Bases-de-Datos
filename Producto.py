class Producto:
    
    def __init__(self, id, nombre, stock, precio, marca, presentacion, refrigeracion, fechaCad, fechaElab  ):
        self.__nombre = nombre
        self.__id = id
        self.__stock = stock
        self.__precio = precio
        self.__marca =marca
        self.__presentacion =presentacion
        self.__refrigeracion = refrigeracion
        self.__fechCad =fechaCad
        self.__fechLab = fechaElab 
    
    #getters
    def get_nombre(self):
        return self.__nombre
    
    def get_id(self):
        return self.__id
    
    def get_stock(self):
        return self.__stock
    
    def get_precio(self):
        return self.__precio
    
    def get_marca(self):
        return self.__marca
    
    def get_presentacion(self):
        return self.__presentacion
    
    
    def get_refrigeracion(self):
        return self.__refrigeracion
    
    def get_fechCad(self):
        return self.__fechCad
    
    def get_Nombre(self):
        return self.__fechLab

