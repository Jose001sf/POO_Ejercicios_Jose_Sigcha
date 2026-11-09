
notas = [10,8,9,5]
print(notas)

notas.insert(1,10)
print(notas)

notas.append(20)
print(notas)

print(notas[1])

print(notas[-1])

print(len(notas))

print(sum(notas))

print(max(notas))

print(min(notas))

notas.remove(9)
print(notas)

orden = sorted(notas)
print(orden)

print(notas[2:])

print(notas[:2])

print(notas[::-1])


meses = (1,2,3,4,5,6,7,8,9,10,11,12)
print(meses[0])
print(meses[-1])
#meses.insert(1,2)

estudiante = {
    "cedula": "0107332355",
    "nombre": "Jose Sigcha",
    "correo": "jose.sigcha.est@tecazuay.edu.ec",
    "celular": "0985067232",
    "nota": 7
}
print(estudiante.get("nombre"))
print(estudiante.keys())

conjunto_a = {1,1,5,4,6,8}
conjunto_b = {1,9,6,5,4}

print(conjunto_a & conjunto_b)
print(conjunto_a | conjunto_b)

