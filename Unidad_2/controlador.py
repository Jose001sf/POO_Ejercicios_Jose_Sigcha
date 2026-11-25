class Controlador_Licencia:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def menu(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == "1":
                software, precio, cantidad = self.vista.pedir_datos_registro()
                precio_num = float(precio)
                cantidad_num = int(cantidad)
                self.modelo.registrar(software, precio_num, cantidad_num)
                self.vista.mostrar_mensaje("Registrado")

            elif opcion == "2":
                self.vista.mostrar_tabla(self.modelo.lista)

            elif opcion == "3":
                codigo_texto = self.vista.pedir_codigo()
                codigo_num = int(codigo_texto)
                elemento = self.modelo.buscar(codigo_num)
                if elemento is None:
                    self.vista.mostrar_mensaje("No existe")
                else:
                    cantidad_texto = self.vista.pedir_cantidad()
                    cantidad_num = int(cantidad_texto)
                    resultado = elemento.asignar(cantidad_num)
                    if resultado:
                        self.vista.mostrar_mensaje(f"Al centro le quedan: {elemento.cantidad}")

            elif opcion == "4":
                self.vista.mostrar_mensaje("Fin")
                break

            else:
                self.vista.mostrar_mensaje("Seleccione otra opcion")