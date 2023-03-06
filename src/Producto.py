class Producto:
    
    
    """
    Constructor de Producto
    :param str id: Identificador unico del producto.
    :param str nombre: Nombre del producto.
    :param int stock: Numero de productos disponibles en el inventario.
    :param str marca: Marca correspondiente al profducto
    :param str presentacion: presentacion del producto : lata, bolsa, botella, etc.
    :param: int precio: Valor del producto.
    :param: Bool refrigeracion: valor booleano, true si el producto requiere
    de refrigeración, false en otro caso.
    :param str fechaCad: fecha de caducidad.
    :param str fechaLab : fecha de elaboración.
    
    """
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
        """ Devuelve el nombre del producto"""
        return self.__nombre
    
    def get_id(self):
        """Devuelve id de producto"""
        return self.__id
    
    def get_stock(self):
        """Devuelve stock de producto"""
        return self.__stock
    
    def get_precio(self):
        """Devuelve precio de producto"""
        return self.__precio
    
    def get_marca(self):
        """Devuelve marca de producto"""
        return self.__marca
    
    def get_presentacion(self):
        """Devuelve presenación de producto"""
        return self.__presentacion
    
    
    def get_refrigeracion(self):
        """Devuelve true si el producto necesita refrigeracion, 
        false en otro caso"""
        return self.__refrigeracion
    
    def get_fechCad(self):
        """Devuelve fecha de caducidad"""
        return self.__fechCad
    
    def get_fechLab(self):
        """ Devuelve fecha de elaboracion"""
        return self.__fechLab
    
    #setters
    
    def set_id(self, id):
        """Se asigna otro id al producto
        :paran str id: Nuevo id"""
        self.__id = id
        
    def set_nombre(self, nombre):
        """Se modifica el nombre del producto
        :param str nombre: Nuevo nombre del producto"""
        self.__nombre = nombre

