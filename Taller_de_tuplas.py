"""print("EJERCIO 1")
#solicitar datos al usuario 

nombre=input("ingrese el nombre del producto: ")
precio=float(input("ingrese el precio unitario del producto: "))
cantidad=int(input("ingrese la cantidad comprada: "))
print ("------------")
#tuplas y listas

tupla_producto=(nombre, precio)
lista_producto=[tupla_producto, cantidad]
registro={"producto":lista_producto}

print ("------------")
#total de los productos

total=precio*cantidad

print ("------------")
#final

print("producto:", nombre)
print("precio unitario:", precio)
print("cantidad:", precio)
print("total a pagar:", total)

print ("------------")
print("EJERCICIO 2")

# Producto 1
nombre1 = input("Nombre producto 1: ")
precio1 = float(input("Precio unitario 1: "))
cantidad1 = int(input("Cantidad 1: "))

print ("------------")

# Producto 2
nombre2 = input("Nombre producto 2: ")
precio2 = float(input("Precio unitario 2: "))
cantidad2 = int(input("Cantidad 2: "))

print ("------------")

# Producto 3
nombre3 = input("Nombre producto 3: ")
precio3 = float(input("Precio unitario 3: "))
cantidad3 = int(input("Cantidad 3: "))

print ("------------")

#Crear tuplas y listas
prod1 = [(nombre1, precio1), cantidad1]
prod2 = [(nombre2, precio2), cantidad2]
prod3 = [(nombre3, precio3), cantidad3]

print ("------------")

#Diccionario
factura = {
    "producto1": prod1,
    "producto2": prod2,
    "producto3": prod3
}

print ("------------")

#Calculo de los totales
total1 = precio1 * cantidad1
total2 = precio2 * cantidad2
total3 = precio3 * cantidad3
total = total1 + total2 + total3

print ("------------")

#resultados
print(nombre1, total1)
print(nombre2, total2)
print(nombre3, total3)
print("Total:", total)"""

print ("------------")
print("EJERCICIO 3")

# Solicitar el nombre del estudiante
nombre = input("Ingrese el nombre del estudiante: ")

# Materia 1
asign1 = input("\nIngrese el nombre de la primera asignatura: ")
nota1_1 = float(input("Ingrese la primera nota de " + asign1 + ": "))
nota1_2 = float(input("Ingrese la segunda nota de " + asign1 + ": "))
prome1 = (nota1_1 + nota1_2) / 2
materia1 = [(asign1, prome1), nota1_1, nota1_2]

# Materia 2
asign2 = input("\nIngrese el nombre de la segunda asignatura: ")
nota2_1 = float(input("Ingrese la primera nota de " + asign2 + ": "))
nota2_2 = float(input("Ingrese la segunda nota de " + asign2 + ": "))
prome2 = (nota2_1 + nota2_2) / 2
materia2 = [(asign2, prome2), nota2_1, nota2_2]

# Materia 3
asign3 = input("\nIngrese el nombre de la tercera asignatura: ")
nota3_1 = float(input("Ingrese la primera nota de " + asign3 + ": "))
nota3_2 = float(input("Ingrese la segunda nota de " + asign3 + ": "))
prome3 = (nota3_1 + nota3_2) / 2
materia3 = [(asign3, prome3), nota3_1, nota3_2]

# Crear el diccionario
estudiante = {
    "nombre": nombre,
    "materias": [materia1, materia2, materia3]
}

# Calcular promedio final
promedio_final = (prome1 + prome2 + prome3) / 3

# Imprimir boletín
print("\n--- BOLETÍN DE CALIFICACIONES ---")
print("Nombre del estudiante:", estudiante["nombre"])
print()

# Asignatura 1
print("Asignatura:", materia1[0][0])
print("  Nota 1:", materia1[1])
print("  Nota 2:", materia1[2])
print("  Promedio:", round(materia1[0][1], 2))
print()

# Asignatura 2
print("Asignatura:", materia2[0][0])
print("  Nota 1:", materia2[1])
print("  Nota 2:", materia2[2])
print("  Promedio:", round(materia2[0][1], 2))
print()

# Asignatura 3
print("Asignatura:", materia3[0][0])
print("  Nota 1:", materia3[1])
print("  Nota 2:", materia3[2])
print("  Promedio:", round(materia3[0][1], 2))
print()

# Promedio final
print("Promedio final del estudiante:", round(promedio_final, 2))





