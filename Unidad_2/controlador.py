class Controlador_Licencia:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def menu(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == "1":
                try:
                    software, precio, cantidad = self.vista.pedir_datos_registro()

                    if not software or not software.strip():
                        raise ValueError("El nombre del software no puede estar vacio")

                    try:
                        precio_num = float(precio)
                        cantidad_num = int(cantidad)
                    except ValueError:
                        raise ValueError("Ingrese un precio y cantidad numericos validos")

                    if precio_num < 0:
                        raise ValueError("El precio no puede ser negativo")
                    if cantidad_num <= 0:
                        raise ValueError("La cantidad debe ser mayor que cero")

                    self.modelo.registrar(software.strip(), precio_num, cantidad_num)
                    self.vista.mostrar_mensaje("Registrado")

                except ValueError as e:
                    self.vista.mostrar_mensaje(f"Error: {e}")

            elif opcion == "2":
                self.vista.mostrar_tabla(self.modelo.lista)

            elif opcion == "3":
                try:
                    codigo_texto = self.vista.pedir_codigo()
                    try:
                        codigo_num = int(codigo_texto)
                    except ValueError:
                        raise ValueError("El codigo debe ser un numero entero valido")

                    if codigo_num <= 0:
                        raise ValueError("El codigo debe ser un numero positivo")

                    elemento = self.modelo.buscar(codigo_num)
                    if elemento is None:
                        self.vista.mostrar_mensaje("No existe")
                    else:
                        cantidad_texto = self.vista.pedir_cantidad()
                        try:
                            cantidad_num = int(cantidad_texto)
                        except ValueError:
                            raise ValueError("La cantidad debe ser un numero entero valido")

                        if cantidad_num <= 0:
                            raise ValueError("La cantidad a asignar debe ser mayor que cero")

                        if elemento.asignar(cantidad_num):
                            self.vista.mostrar_mensaje(f"Al centro le quedan: {elemento.cantidad}")
                        else:
                            self.vista.mostrar_mensaje("No hay suficientes licencias disponibles")

                except ValueError as e:
                    self.vista.mostrar_mensaje(f"Error: {e}")

            elif opcion == "4":
                self.vista.mostrar_mensaje("Fin")
                break

            else:
                self.vista.mostrar_mensaje("Seleccione otra opcion")