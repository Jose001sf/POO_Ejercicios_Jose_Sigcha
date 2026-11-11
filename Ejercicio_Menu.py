def saludo():
    nombre = input("Ingrese su nombre: ")
    print("Bienvenido: ", nombre)
    return nombre

def pregunta1():
    print("1. Que imprime el siguiente codigo?")
    print('print("ab" * 3)')
    print("Respuesta correcta: ababab")

def pregunta2():
    print("2. Que imprime el siguiente codigo?")
    print("a = {1, 2, 3, 4}")
    print("b = {3, 4, 5}")
    print("print(len(a & b))")
    print("Respuesta correcta: 2")

def pregunta3():
    print("3. Que imprime el siguiente codigo?")
    print('socio = {"nombre": "Ana", "saldo": 120}')
    print('print(socio.get("correo", "Sin correo"))')
    print("Respuesta correcta: Sin correo")

def pregunta4():
    print("4. Que ocurre al ejecutar el siguiente codigo?")
    print("datos = (10, 20, 30)")
    print("datos[1] = 99")
    print("print(datos)")
    print("Respuesta correcta: Se produce un TypeError")

def pregunta5():
    print("5. Que imprime el siguiente codigo?")
    print("a = [1, 2, 3]")
    print("b = a")
    print("b[0] = 5")
    print("print(a)")
    print("Respuesta correcta: [5, 2, 3]")

def pregunta6():
    print("6. Que imprime el siguiente codigo?")
    print("saldo = 350")
    print("if saldo >= 1000:")
    print('print("Oro")')
    print("elif saldo >= 100:")
    print('print("Plata")')
    print("else:")
    print('print("Básica")')
    print("Respuesta correcta: Plata")

def pregunta7():
    print("7. Que imprime el siguiente codigo?")
    print("print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])")
    print("Respuesta correcta: [4, 16]")

def pregunta8():
    print("8. Que imprime el siguiente codigo?")
    print("for i in range(3, 0, -1):")
    print('print(i, end=" ")')
    print("Respuesta correcta: 3 2 1")

def pregunta9():
    print("9. Que imprime el siguiente codigo?")
    print('notas = {"Ana": 10, "Luis": 8}')
    print("for nombre, nota in notas.items():")
    print('print(f"nombre:nota", end=" ")')
    print("Respuesta correcta: Ana:10 Luis:8")

def pregunta10():
    print("10. Que imprime el siguiente codigo?")
    print("total = 0")
    print("n = 1")
    print("while n <= 5:")
    print("total += n")
    print("n += 1")
    print("print(total)")
    print("Respuesta correcta: 15")

def pregunta11():
    print("11. Validar Contraseña")
    print("Respuesta correcta: codigo")

def menu_preguntas():
    while True:
        print("Menu de preguntas")
        print("1. Pregunta 1")
        print("2. Pregunta 2")
        print("3. Pregunta 3")
        print("4. Pregunta 4")
        print("5. Pregunta 5")
        print("6. Pregunta 6")
        print("7. Pregunta 7")
        print("8. Pregunta 8")
        print("9. Pregunta 9")
        print("10. Pregunta 10")
        print("11. Pregunta 11")
        print("12. Regresar")
        
        opcion1 = input("Elija una opcion: ")
        
        if opcion1 == "1":
            pregunta1()
        elif opcion1 == "2":
            pregunta2()
        elif opcion1 == "3":
            pregunta3()
        elif opcion1 == "4":
            pregunta4()
        elif opcion1 == "5":
            pregunta5()
        elif opcion1 == "6":
            pregunta6()
        elif opcion1 == "7":
            pregunta7()
        elif opcion1 == "8":
            pregunta8()
        elif opcion1 == "9":
            pregunta9()
        elif opcion1 == "10":
            pregunta10()
        elif opcion1 == "11":
            pregunta11()
        elif opcion1 == "12":
            break
        else:
            print("Invalido")

def menu():
    while True:
        print("Menu")
        print("1. Ingrese nombre")
        print("2. Menu de preguntas")
        print("3. Salir")
        opcion = input("Elije una opcion: ")
        
        if opcion == "1":
            saludo()
        elif opcion == "2":
            menu_preguntas()
        elif opcion == "3":
            print("Fin")
            break
        else:
            print("Invalido")
menu()
