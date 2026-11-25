class Licencia:
    def __init__(self, codigo, software, precio, cantidad):
        self.codigo = codigo
        self.software = software
        self.precio = precio
        self.cantidad = cantidad

    def asignar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        if cantidad > self.cantidad:
            raise ValueError("No hay suficientes licencias")
        self.cantidad = self.cantidad - cantidad
        return True

    def __str__(self):
        return f"{self.codigo}{self.software}{self.precio}{self.cantidad}"


class GestorLicencias:
    def __init__(self):
        self.lista = [
            Licencia(1, "Office", 70.00, 30),
            Licencia(2, "AutoCAD", 250.00, 10)
        ]

    def registrar(self, software, precio, cantidad):
        codigo = len(self.lista) + 1
        nueva = Licencia(codigo, software, precio, cantidad)
        self.lista.append(nueva)
        return nueva

    def buscar(self, codigo):
        for elemento in self.lista:
            if elemento.codigo == codigo:
                return elemento
        return None
