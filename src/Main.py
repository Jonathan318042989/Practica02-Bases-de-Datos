from ArchivoSucursal import ArchivoSucursal
from ArchivoEmpleado import ArchivoEmpleado


class Main:
    def imprimirOpciones(self):
        print("\t\tBienvenido al gestor de Archivos.")
        print("\n\tOpciones:")
        print("1) Gestionar sucursales")
        print("2) Gestionar empleados")
        print("3) Gestionar productos")
        print("4) Salir")
        print("Seleccione una opción:")

    def menu(self):
        try:
            while True:
                self.imprimirOpciones()
                opcion = int(input("Ingrese la opción que desea ejecutar: "))
                if opcion == 1:
                    print('\nGestionar sucursales')
                    sucursal = ArchivoSucursal()
                    sucursal.menuSucursal()
                    break
                elif opcion == 2:
                    print('\nGestionar empleados')
                    empleado = ArchivoEmpleado()
                    empleado.menuEmpleado()
                    break
                elif opcion == 3:
                    print('\nGestionar productos')
                    break
                elif opcion == 4:
                    print("\n¡Hasta luego!")
                    return
                else:
                    print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("ERROR: Algo paso!!")

main = Main()
main.menu()