# 1. Crear una clase básica
class Libro: 
    pass


libro1 = Libro()
print(type(libro1))


# 2. Crear el constructor y métodos de la clase
class Libro:

    def __init__(self, nombre, autor, estado):
        self.nombre = nombre
        self.autor = autor
        self.estado = estado

    def mostrar(self):
        print(f"Nombre del Libro: {self.nombre} | Nombre del autor: {self.autor}")

    def cambiar_estado(self, estado1):
        self.estado = estado1

    def __init__(self, nombre, autor, estado, listaLibros):
        self.nombre = nombre
        self.autor = autor
        self.estado = estado
        self.listaLibros = listaLibros

        def mostrar_lista(self):
            for e in self.listaLibros:
                print(e)

    def __str__(self):
        return (
        f"Nombre: {self.nombre}, Autor: {self.autor}, Estado: {self.estado}"
    )

libro2 = Libro("Python Intermedio", "Autor X", "Disponible", ["Python Basico", "Python II"])
