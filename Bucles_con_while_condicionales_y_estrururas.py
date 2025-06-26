#EJERCICIOS CON WHILE

# 1. #Suma hasta cero
# suma=0
# numero=int(input("ingrese un numero (0 para terminar: "))

# while numero!=0:
#     suma+=numero
#     numero=int(input("ingrese un numero (0 para terminar: "))
# print(f"el programa a terminado {suma}")

# print ("------------")

# 2. #Contraseña secreta 
# clave= input ("ingrese la contraseña: ")

# while clave !="python123":
#     print("contraseña incorrecta: ")
#     clave= input ("intenta de nuevo: ")
# print("¡acceso concedido.")    

# print ("------------")

# 3. #Lista de compras
# lista=[]
# producto=input("ingrese un producto (escribe fin para termniar: ")
# while producto!="fin":
#     lista.append(producto)
#     producto=input("ingrese un producto (escribe fin para terminar ")

# print(f"tu lista es: {lista}")

# print ("------------")

# # 4. #Contador de pares e impares
# contador = 0
# pares = 0
# impares = 0

# while contador < 10:
#     numero = int(input(f"Ingrese el número: {contador}: "))
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     contador += 1

# print("Cantidad de números pares:", pares)
# print("Cantidad de números impares:", impares)

# print ("------------")

# 5. #promedio de calificaciones
# notas = []
# entrada = input("Ingresa una nota (escribe 'salir' para terminar): ")

# while entrada != "salir":
#     nota = float(entrada)
#     notas.append(nota)
#     entrada = input("Ingresa otra nota (escribe 'salir' para terminar): ")

# suma = sum(notas)
# cantidad = len(notas)
# promedio = suma / cantidad

# print("El promedio es:", promedio)

print ("------------")

6. #Tabla de multiplicar interactiva

contar="si"
while contar.lower()=="si":
    numero=int(input("ingrese la tabla de multiplicar: "))
    contar=0
    print(f"'\ntabla del {numero}:\n")

    while contar <= 10:
        resultado=numero*contar
        print(f"{numero}*{contar}={resultado}")
        contar<=1
contar=input("\SEGUIMOS CON LA SIGUIENTE (si/no)")
