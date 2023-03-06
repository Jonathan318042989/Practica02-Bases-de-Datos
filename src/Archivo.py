import csv
import os.path
import pandas as pd
import sys
from Sucursal import Sucursal
from Empleado import Empleado
from Producto import Producto

class Archivo:
    
    global archivo
    def __init__(self):
        global archivo

    def verificaExistenciaSucursales(self, archivo):
        if(os.path.isfile("CSV/" + archivo +".csv")):
            self.archivo = open("CSV/"+ archivo + ".csv", "a")
        else:
            self.archivo = open("CSV/"+archivo + ".csv", "w")
            self.inicializaSucursales(self.archivo)

    
    def inicializaSucursales(self, archivo):
        writer = csv.writer(archivo)
        writer.writerow(["ID", "Nombre", "Colonia", "Calle", "Numero", "CodigoPostal", "Telefonos", "Fecha de apertura"])
        archivo.close()

    def agregarSucursal(self, archivo, sucursal):
        with open('CSV/Sucursales.csv', 'a', newline='') as archivo:

            writer = csv.writer(archivo)
            nuevaSucursal = [sucursal.getID(), sucursal.getNombre(),
                        sucursal.getColonia(), sucursal.getCalle(),
                            sucursal.getNumero(), sucursal.getCodigoPostal(),
                            sucursal.getTelefono(), sucursal.getFechaApertura()]
            writer.writerow(nuevaSucursal)
        
        archivo.close()

    def consultarSucursal(self, id):
        with open('CSV/Sucursales.csv') as archivo:
            reader = csv.reader(archivo, delimiter=',')
            encabezado = next(archivo)
            next(archivo)
            for row in reader:
                if (row[0] == id):
                    print(encabezado)
                    print(row)
                    break
    
    def eliminarSucursal(self, id):
        data = pd.read_csv('CSV/Sucursales.csv', header=0)
        print(id)
        indice = data.index[data["ID"] == id]
        data.drop(indice, inplace=True)
        data.to_csv('CSV/Sucursales.csv', index= False) 

    def editarDato(self, id,columna, datoNuevo):
        data = pd.read_csv('CSV/Sucursales.csv', index_col= 'ID')
        data.loc[id, columna]  = datoNuevo
        data.to_csv('CSV/Sucursales.csv', index= False)      

        
            

arch = Archivo()
arch.verificaExistenciaSucursales("Sucursales")
"""
suc2 = Sucursal()
suc2.setID("sucursal01")
suc2.setNombre("Sucursal 01")
suc2.setColonia("Oriental")
suc2.setCalle("Oriente 45")
suc2.setNumero(78)
suc2.setCodigoPostal("12345")
suc2.setTelefono(5598546451)
suc2.setTelefono(1234569426)
suc2.setTelefono(6489278922)

suc1 = Sucursal()
suc1.setID("sucursal02")
suc1.setNombre("Sucursal 02")
suc1.setColonia("Providencia")
suc1.setCalle("Oriente 23")
suc1.setNumero(78)
suc1.setCodigoPostal("12345")
suc1.setTelefono(1234567894)
suc1.setTelefono(1234568935)
suc1.setTelefono(6489278922)

suc = Sucursal()
suc.setID("sucursal03")
suc.setNombre("Sucursal 03")
suc.setColonia("Agricola")
suc.setCalle("Oriente 45")
suc.setNumero(78)
suc.setCodigoPostal("12345")
suc.setTelefono(5598546451)
suc.setTelefono(1234569426)
suc.setTelefono(6489278922)

suc3 = Sucursal()
suc3.setID("sucursal04")
suc3.setNombre("Sucursal 04")
suc3.setColonia("Doctores")
suc3.setCalle("Oriente 23")
suc3.setNumero(78)
suc3.setCodigoPostal("12345")
suc3.setTelefono(1234567894)
suc3.setTelefono(1234568935)
suc3.setTelefono(6489278922)

arch.agregarSucursal(arch.archivo, suc2)
arch.agregarSucursal(arch.archivo, suc1)
arch.agregarSucursal(arch.archivo, suc)
arch.agregarSucursal(arch.archivo, suc3)

arch.consultarSucursal("sucursal02")

arch.eliminarSucursal("sucursal02")

arch.editarDato("sucursal03", "Colonia", "Roma")
"""

arch.eliminarSucursal("sucursal04")
arch.editarDato("sucursal03", "Nombre", "Roma")
