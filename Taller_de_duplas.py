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








