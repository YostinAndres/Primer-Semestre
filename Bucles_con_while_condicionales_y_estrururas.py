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

# print ("------------")

# 6. #Tabla de multiplicar interactiva

# contar="si"
# while contar.lower()=="si":
#     numero=int(input("ingrese la tabla de multiplicar: "))
#     contar=0
#     print(f"'\ntabla del {numero}:\n")

#     while contar <= 10:
#         resultado=numero*contar
#         print(f"{numero}*{contar}={resultado}")
#         contar<=1
# contar=input("\SEGUIMOS CON LA SIGUIENTE (si/no)")

# print ("------------")

# 7. #Adivina el numero

# numero=15
# intento=int(input("adivina el numero: "))

# while intento!= numero:
#     if intento<numero:
#         print("es mayor")
#     else:
#         print("es menor")
#     intento=int(input("intenta otra vez: "))
# print("adivinaste el numero!")        

# print ("------------")

# 8. #Tupla de frutas
# frutas = ("manzana", "pera", "banano", "uva", "sandía")
# encontrada = False

# while encontrada == False:
#     adivinanza = input("Adivina una fruta: ")
    
#     # Recorrer manualmente la tupla
#     for fruta in frutas:
#         if adivinanza == fruta:
#             encontrada = True
    
#     if encontrada == False:
#         print("No está en la lista.Intenta otra vez")

# print("Correcto!, Esa fruta sí está en la lista")        
    
# print ("------------")  

# 9. # Diccionario español-inglés
# diccionario = {
#     "pajaro": "bird",
#     "gato": "cat",
#     "casa": "house",
#     "libro": "book",
#     "rojo": "red"
# }

# palabra = input("Escribe una palabra en español (o 'salir' para terminar): ")

# while palabra != "salir":
#     if palabra in diccionario:
#         print("Traducción:", diccionario[palabra])
#     else:
#         print("Palabra no encontrada.")
    
#     palabra = input("Escribe otra palabra (o 'salir' para terminar): ")

# print("Fin del programa.")

# print ("------------")  

# 10. #calculadora basica
# opcion = ""

# while opcion != "5":
#     print("\n--- CALCULADORA ---")
#     print("1. Sumar")
#     print("2. Restar")
#     print("3. Multiplicar")
#     print("4. Dividir")
#     print("5. Salir")
    
#     opcion = input("Elige una opción: ")

#     if opcion in ["1", "2", "3", "4"]:
#         num1 = float(input("Ingresa el primer número: "))
#         num2 = float(input("Ingresa el segundo número: "))

#         if opcion == "1":
#             print("Resultado:", num1 + num2)
#         elif opcion == "2":
#             print("Resultado:", num1 - num2)
#         elif opcion == "3":
#             print("Resultado:", num1 * num2)
#         elif opcion == "4":
#             if num2 != 0:
#                 print("Resultado:", num1 / num2)
#             else:
#                 print("Error: No se puede dividir por cero.")
#     elif opcion == "5":
#         print("Saliendo del programa...")
#     else:
#         print("Opción inválida. Intenta de nuevo.")

# print ("------------") 

# 11. #Registro de edades
# personas = {}

# nombre = input("Ingresa un nombre (o 'salir' para terminar): ")

# while nombre != "salir":
#     edad = int(input(f"Ingrese la edad de {nombre}: "))
#     personas[nombre] = edad
#     nombre = input("Ingresa otro nombre (o 'salir' para terminar): ")

# print("\nRegistro de edades:")
# for nombre, edad in personas():
#     print(f"{nombre}: {edad} años")

# print ("------------") 

# 12. #Buscar en lista
# colores = ["rojo", "azul", "verde", "amarillo", "negro"]
# encontrado = False

# while not encontrado:
#     intento = input("Escribe un color: ")
#     for color in colores:
#         if intento == color:
#             encontrado = True
#     if not encontrado:
#         print("Ese color no está en la lista. Intenta de nuevo.")

# print("¡Correcto! Ese color está en la lista.")

# print ("------------") 

# 13. #potencias de un numero
# numero = int(input("Ingresa un número: "))
# exponente = 1

# while exponente <= 5:
#     resultado = numero ** exponente
#     print(f"{numero}^{exponente} = {resultado}")
#     exponente += 1

# print ("------------") 

# 14. #lista de cuadros
# cuadrados = []
# contador = 0

# while contador < 5:
#     numero = int(input(f"Ingrese el número #{contador + 1}: "))
#     cuadrados.append(numero ** 2)
#     contador += 1

# print("Lista de cuadrados:")
# print(cuadrados)

# print ("------------") 

# 15. #diccionario de estudiantes

# estudiantes = {}

# nombre = input("Nombre del estudiante (escribe 'fin' para terminar): ")

# while nombre != "fin":
#     nota = float(input("Nota final: "))
#     estudiantes[nombre] = nota
#     nombre = input("Nombre del estudiante (escribe 'fin' para terminar): ")

# print("Notas registradas:")
# print(estudiantes)