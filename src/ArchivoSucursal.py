import csv
import os.path
import pandas as pd
import sys
from Sucursal import Sucursal


class Archivo:
    
    global archivo
    sucursalPath = "CSV/Sucursales.csv"
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
        with open(self.sucursalPath, 'a', newline='') as archivo:
            print(sucursal.getTelefono())
            writer = csv.writer(archivo)
            nuevaSucursal = [sucursal.getID(), sucursal.getNombre(),
                        sucursal.getColonia(), sucursal.getCalle(),
                            sucursal.getNumero(), sucursal.getCodigoPostal(),
                            sucursal.getTelefono(), sucursal.getFechaApertura()]
            writer.writerow(nuevaSucursal)
        
        archivo.close()

    def consultarSucursal(self, id):
        data = pd.read_csv(self.sucursalPath, index_col= 'ID')
        sucursal = data.loc[id]
        return sucursal
    
    def eliminarSucursal(self, id):
        if(self.existeIDSucursal(id)):
            data = pd.read_csv(self.sucursalPath)
            print(id)
            indice = data.index[data["ID"] == id]
            data.drop(indice, inplace=True)
            data.to_csv(self.sucursalPath, index= False) 
        else:
            print("No se encontro el ID") 

    def editarDato(self, id,columna, datoNuevo):
        if(self.existeIDSucursal(id)):
            data = pd.read_csv(self.sucursalPath, index_col= 'ID')
            data.loc[id, columna]  = datoNuevo
            data.to_csv(self.sucursalPath)
        else:
            print("No se encontro el ID")

    def editarListaTelefonos(self, id, opcion, datoNuevo):
        if(self.existeIDSucursal(id)):
            if(opcion == 1):
                data = pd.read_csv(self.sucursalPath, index_col= 'ID')
                datoActual = data.loc[id, "Telefonos"]
                listaActual = datoActual.strip('][').split(', ')
                listaActual = list(map(int, listaActual))
                if(type(datoNuevo == int)):
                    listaActual.append(datoNuevo)

                    data.loc[id, "Telefonos"]  = str(listaActual)
                    data.to_csv(self.sucursalPath)
                else:
                    print("El telefono debe ser un numero")
            elif(opcion == 2):
                data = pd.read_csv(self.sucursalPath, index_col= 'ID')
                datoActual = data.loc[id, "Telefonos"]
                listaActual = datoActual.strip('][').split(', ')
                listaActual = list(map(int, listaActual))
                del listaActual[datoNuevo]
                data.loc[id, "Telefonos"]  = str(listaActual)
                data.to_csv(self.sucursalPath)
        else:
            print("No se encontro el ID")

    def existeIDSucursal(self,id):
        with open(self.sucursalPath) as archivo:
            reader = csv.reader(archivo, delimiter=',')
            encabezado = next(archivo)
            next(archivo)
            for row in reader:
                if (row[0] == id):
                    return True
            return False