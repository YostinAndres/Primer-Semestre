"""print("sistema de evaluacion")
print("buenas tardes, bienvenido al sistema de evaluacion, recuerde si su nota es 2.9 o menos pierede, si su nota es mas de 3.0 gana, sus cinco notas son:")
nombre=input("señor ususario ingrese su nombre: ")

Mater1="fisica"
Mater2="español"
Mater3="quimica"
Mater4="sociales"
Mater5="ingles"

print("ingrese 8 notas de la", Mater1)
Nota1=float(input("ingrese la nota1: ",))
Nota2=float(input("ingrese la nota2: ",))
Nota3=float(input("ingrese la nota3: ",))
suma1=Nota1 + Nota2 + Nota3
division1= suma1 / 3
print("La suma de notas es: ", suma1)
print("El promedio de", Mater1, "es: ", division1)


print("ingrese 8 notas de la", Mater2)
Notaa1=float(input("ingrese la nota1: ",))
Notaa2=float(input("ingrese la nota2: ",))
Notaa3=float(input("ingrese la nota3: ",))
suma2=Notaa1 + Notaa2 + Notaa3
division2= suma2 / 3
print("La suma de notas es: ", suma2)
print("El promedio de", Mater2, "es: ", division2)


print("ingrese 8 notas de la", Mater3)
Not1=float(input("ingrese la nota1: ",))
Not2=float(input("ingrese la nota2: ",))
Not3=float(input("ingrese la nota3: ",))
suma3=Not1 + Not2 + Not3
division3= suma3 / 3
print("La suma de notas es: ", suma3)
print("El promedio de", Mater3, "es: ", division3)


print("ingrese 8 notas de la", Mater4)
NNota1=float(input("ingrese la nota1: ",))
NNota2=float(input("ingrese la nota2: ",))
NNota3=float(input("ingrese la nota3: ",))
suma4=NNota1 + NNota2 + NNota3
division4= suma4 / 3
print("La suma de notas es: ", suma4)
print("El promedio de", Mater4, "es: ", division4)


print("ingrese 8 notas de la", Mater5)
Nat1=float(input("ingrese la nota1: ",))
Nat2=float(input("ingrese la nota2: ",))
Nat3=float(input("ingrese la nota3: ",))
suma5=Nat1 + Nat2 + Nat3
division5= suma4 / 3
print("La suma de notas es: ", suma5)
print("El promedio de", Mater5, "es: ", division5)

print("Listas")
productos=[]

producto1=input("ingrese el primer producto: ")
productos.append(producto1)

producto2=input("ingrese el sugundo producto: ")
productos.append(producto2)

producto3=input("ingrese el tecer producto: ")
productos.append(producto3)

print("Lista completa de productos: ", productos)



precios=[]

precio1=float(input("precio del primer articulo: "))
precios.append(precio1)

precio2=float(input("precio del segundo articulo: "))
precios.append(precio2)

precio3=float(input("precio el tercer articulo: "))
precios.append(precio3)

total=sum(precios)
print("suma total de los precios: ", total)

numeros=[]

num1=int(input("ingresa el primer numero: "))
numeros.append(num1)

num2=int(input("ingresa el segundo numero: "))
numeros.append(num2)

num3=int(input("ingresa el tercer numero: "))
numeros.append(num3)

num4=int(input("ingrese el cuarto numero: "))
numeros.append(num4)

print("El numero mayor es: ", max(numeros))
print("El numero menor es: ", min(numeros))"""


print("ejemplo de remove")
frutas=["banana","manzana","naranja","banana"]
frutas.remove("banana")
print(frutas)

print("ejemplo de max")
print("letras")
letras=["ana","carlos","beatriz"]
print(max(letras))

print("ejemplo de min")
numeross=[5,2,8,1,9]
minimo=min(numeross)
print("el valor minimo es:", minimo)

print("ejemplo de .index")
nombrees=["Ana","Luis","Carlos","Luis"]
print(nombrees.index("Luis"))

print("ejemplo de remove")
numeros=[1,2,3,2]
numeros.remove(2)


print ("------------")

clientes=["Ana","Maria","Sebastian","julian"]

clientes[0]= clientes[0].upper()
clientes[1]= clientes[1].upper()
clientes[2]= clientes[2].upper()
clientes[3]= clientes[3].upper()

clientes.append("JULIANA")
print("cantidad de elementos: ", len(clientes))



















