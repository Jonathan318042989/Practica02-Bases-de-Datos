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
        writer.writerow(["ID", "Nombre", "Colonia", "Calle", "Numero", "CodigoPostal", "Telefonos"])
        archivo.close()

    def agregarSucursal(self, archivo, sucursal):
        with open('CSV/Sucursales.csv', 'a', newline='') as archivo:

            writer = csv.writer(archivo)
            nuevaSucursal = [sucursal.getID(), sucursal.getNombre(),
                        sucursal.getColonia(), sucursal.getCalle(),
                            sucursal.getNumero(), sucursal.getCodigoPostal(),
                            sucursal.getTelefono()]
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

        
            

arch = Archivo()
arch.verificaExistenciaSucursales("Sucursales")
suc = Sucursal()
suc.setID("sucursal01")
suc.setNombre("Sucursal 01")
suc.setColonia("Agrícola")
suc.setCalle("Oriente 45")
suc.setNumero(78)
suc.setCodigoPostal("12345")
suc.setTelefono(5598546451)
suc.setTelefono(1234569426)
suc.setTelefono(6489278922)

arch.agregarSucursal(arch.archivo, suc)

suc1 = Sucursal()
suc1.setID("sucursal02")
suc1.setNombre("Sucursal 02")
suc1.setColonia("Doctores")
suc1.setCalle("Oriente 23")
suc1.setNumero(78)
suc1.setCodigoPostal("12345")
suc1.setTelefono(1234567894)
suc1.setTelefono(1234568935)
suc1.setTelefono(6489278922)

arch.agregarSucursal(arch.archivo, suc1)

arch.consultarSucursal("sucursal02")


