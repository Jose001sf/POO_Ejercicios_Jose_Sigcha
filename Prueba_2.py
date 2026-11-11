clave = input("Contraseña: ")
# Escriba su solución aquí

errores = []
if len(clave) < 8:
    errores.append("Debe tener 8 caracteres")
if not any(verificar.isdigit() for verificar in clave):
    errores.append("Debe tener un digito")
if not any(verificar.isupper() for verificar in clave):
    errores.append("Debe tener una letra mayuscula")
if not errores:
    print("Contraseña segura")
else:
    print("La contraseña no cumple con estas reglas: ")
    for error in errores:
        print(error)
