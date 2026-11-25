class VistaLicencia:
    def mostrar_menu(self):
        print("Ejercicio 26")
        print("MENU")
        print("1. Registrar licencia")
        print("2. Mostrar licencias")
        print("3. Asignar licencias")
        print("4. Salir")

    def pedir_opcion(self):
        return input("Seleccione una opcion: ")

    def pedir_datos_registro(self):
        software = input("Software: ")
        precio = input("Precio: ")
        cantidad = input("Cantidad: ")
        return software, precio, cantidad

    def pedir_codigo(self):
        return input("Codigo: ")

    def pedir_cantidad(self):
        return input("Cantidad: ")

    def mostrar_tabla(self, lista):
        print("Codigo       Software          Precio         Cantidad")
        for elemento in lista:
            print(elemento)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)