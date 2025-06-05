"""# CREDITO BANCARIO

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")

if edad >= 18:
    print("Crédito aprobado: el cliente es mayor de edad.")
else:
    print("Crédito rechazado: el cliente es menor de edad.")

print("---------")

#SALA DE JUEGOS

Edad3 = int(input("Ingrese su edad: "))

if Edad3>= 18:
    print("Crédito aprobado")
else:
    print("Crédito rechazado")

print("Fin")
 
print("---------")

#FUNCIONAMIENTO DE CALCULADORA

opa= input("Ingrese operación (s: suma, r: resta, m: multiplicación, d: división): ")

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

if opa == 's':
    print("Resultado:", a + b)
elif opa == 'r':
    print("Resultado:", a - b)
elif opa == 'm':
    print("Resultado:", a * b)
elif opa == 'd':
    if b == 0:
        print("Resultado:", a / b)
    else:
        print("No se puede dividir por cero")
else:
    print("Operación no válida")"""
 
