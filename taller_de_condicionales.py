"""#TALLER DE CONDICIONALES

#1. verificar si un numero es positivo, negativo o cero.
num = int(input("Número: "))
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Cero")
    
print("---------")

#2. calcula el mayor de dos numeros ingresados
a = int(input("Número 1: "))
b = int(input("Número 2: "))
if a > b:
    print("Mayor:", a)
else:
    print("Mayor:", b)

print("---------")

#3. determina si un numero es par o inpar 
n = int(input("Número: "))
if n % 2 == 0:
    print("Par")
else:
    print("Impar")
    
print("---------")

#4. dado un numero, verifica si esta entre 10 y 20
n = int(input("Número: "))
if n > 10 and n < 20:
    print("Está entre 10 y 20")
else:
    print("Fuera de rango")

print("---------")

#5. dados tres numeros, encuentran el mayor usando condicionales
a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))
if a >= b and a >= c:
    print("Mayor:", a)
elif b >= a and b >= c:
    print("Mayor:", b)
else:
    print("Mayor:", c)
    
print("---------")

#6. calcula el precio final con un 10% de descuento si el total es mayor a $100
total = float(input("Total: "))
if total > 100:
    total = total * 0.9
print("Precio final:", total)

print("---------")

#7. verifica si una persona puede votar (mayor o igual a 18 años)
edad = int(input("Edad: "))
if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")
    
print("---------")

#8. dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP
precio = float(input("Precio: "))
tipo = input("Tipo de cliente (VIP/normal): ")
if tipo == "VIP":
    precio = precio * 0.8
print("Precio final:", precio)

print("---------")

#9. determina si un numero es multiplo de 5 y de 3 al mismo tiempo
n = int(input("Número: "))
if n % 3 == 0 and n % 5 == 0:
    print("Múltiplo de 3 y 5")
else:
    print("No lo es")
    
print("---------")

#10. dado un numero, verifica si es divisible entre dos numeros dados
n = int(input("Número: "))
d1 = int(input("Divisor 1: "))
d2 = int(input("Divisor 2: "))
if n % d1 == 0 and n % d2 == 0:
    print("Es divisible entre ambos")
else:
    print("No es divisible entre ambos")"""

