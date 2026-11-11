#DECLARACION DE FUNCIONES
def saludar():
    print("Hola Yo")
saludar()

#FUNCION CON PARAMETROS
def calcular_edad(anio_nacimiento, anio_actual):
    print ("La edad actual es: ", anio_actual-anio_nacimiento)
a = int (input("Ingrese su año de nacimiento: "))
b = int (input("Ingrese el año actual: "))
calcular_edad(a,b)

#FUNCIONES CON RETORNO
def calcular_iva(precio_producto, valor_iva):
    return precio_producto*valor_iva
resultado = calcular_iva(10,0.15)
print("El resultado es: ", resultado)

#FUNCIONES CON VALORES POR DEFECTO
def calcular_iva(precio_producto, valor_iva = 0.15):
    return precio_producto*valor_iva
resultado = calcular_iva(100)
print("El resultado es: ", resultado)

#FUNCIONES CON LISTAS
def calcular_par(numeros):
    for i in numeros:
        if i%2 == 0:
            print(f"Es par {i}")
        else:
            print(f"Es impar {i}")
lista_numeros = [0,1,2,3,4,5,6,7,8,9]
calcular_par(lista_numeros)

#FUNCIONES CON TUPLAS
def suma_numeros(*A):
    return sum(A)
print(suma_numeros(1,2,3))

#FUNCION CON DICCIONARIO
def estudiantes(**lista_estudiantes):
    for nombre, edad in lista_estudiantes.items():
        print("El estudiante ", nombre, "tiene ", edad, "años")
        total = sum(lista_estudiantes.values())
        print("La suma de las edades es: ", total)
estudiantes(Ana=20, Carlos=22, Sofia=19)




#Menu de usuarios
#1. ingrese nombre MENSAJES DE BIENVENIDA
#2. menu de preguntas PRESENTAR 11 PREGUNTAS
#3. salir


