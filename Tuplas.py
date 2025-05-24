"""#EJERCICIOS
#Ejercicio1: crear una tupla con los numeros del 1 al 5
tupla=(1,2,3,4,5)
print("tupla creada:", tupla)

print ("------------")

#Ejercicio2: acceder a un elemento muestra es segundo valor de la tupla creada anteriormente 
print(" segundo valor de la tupla : " , tupla[1])

print ("------------")

#Ejercicio3: obtener la longitud imprime cuantos elementos tiene la tupla
print("numero de elemento de la tupla: " , len(tupla))

print ("------------")

#Ejercicio4: usar inde() encuentra la posicion del numero 4 en la tupla
print("posicion del numero 4: " , tupla.index(4))

print ("------------")

#Ejercicio5: usar count() cuenta cuantas veces aparece el numero 2 en la tupla 
print("cantidad de veces que aparece el numero 2: " , tupla.count(2))

print ("------------")

#Ejercicio6: tupla con tipos mezclados crea una tupla que contenga una cadena de texto, un numero entero y un numero decimal
tupla_mixta=("hola", 10, 3.14)
print("tupla con tipos mezclados: ", tupla_mixta)

print ("------------")

#Ejercicio7: tuplas anidadas, crea una tupla que contenga otra tupla en su interior. luego accede al primer valor de la tupla interna
tupla_anidada=((100, 200)), "otro valor"
print("el primer valor de la tupla interna: ", tupla_anidada[0][0])"""

#Ejercicios de tuplas y listas 
#Ejercicio1: crear una tupla de 5 numeros enteros y extraer el primer y el ultimo elemento
tupla1=(1,2,3,4,5)
print(tupla1[0], tupla1[-1])

print ("------------")

#Ejercicio2: crear una lista de 5 numeros decimales y extraer el segundo y el cuarto elemento
lista=[1.1, 2.2, 3.3, 4.4, 5.5]
print( lista[1] , lista[3])

print ("------------")

#Ejercicio3: crear una tupla de 3 elementos y asignarlos a variables individuales 
tupla2=(20, 30, 40)
A, F, T=tupla2
print(A, F, T)

print ("------------")

#Ejercicio4: crear una lista con 5 numeros enteros, sumarlos y almacenar el resultado en una variable
lista= [1,2,3,4,5,]
suma= sum(lista)
print(suma)

print ("------------")

#Ejercicio5: crear una tupla con 3 numeros flotantes y calcular su promedio
tupla3=(4.5, 5.5, 6.6)
promedio=sum(tupla3)/len(tupla3)
print("el promedio de la tupla es: ", promedio)

print ("------------")

#Ejercicio6: crear una lista con 4 numeros enteros y almacenarlos en variables individuales 
tupla4=(10, 20, 30, 40)
X, H, J, K,=[10, 20, 30, 40]
print("tu lista es: " , X, H, J, K,)

print ("------------")

#Ejercicio7: crear una tupla con 2 elementos y realizar una multiplicacion de los elementos
tupla5=(8, 7)
print(tupla5[0] * tupla5[1])

print ("------------")

#Ejercicio8: crear una lista con 3 elementos, agregar un nuevo numero y extraer el primer y el ultimo elemento
lista1=[50, 40, 30]
lista1.insert(1, 15)
print(lista1[0], lista1[-1])

print ("------------")

#Ejercicio9: crear una tupla con 4 numeros y calcular la suma de los primeros dos elementos 
tupla9=(3, 6, 9, 12)
print("suma: ", tupla9[0] + tupla9[1])

print ("------------")

#Ejercicio10= crear una lista con 5 numeros enteros y calcular la diferencia entre el segundo y el cuarto
lista10=[10, 20, 30, 40, 50]
print(lista10[1]-lista10[3])

print ("------------")

#Ejercicio11: crear una tupla con 5 numeros y almacenar la multiplicacion del primer y ultimo elemento

tupla11=(2, 4, 6, 8, 10)
print(tupla11[0]*tupla11[-1])

print ("------------")

#Ejercicio12: crear una lista con 3 numeros y realizar la division entre el primer y el tercer numero

tupla12=(12, 24, 6)
print(tupla12[0]/tupla12[2])

print ("------------")

#Ejercicio13: crear una tupla con 4 numeros enteros y extraer el tercer elemento

tupla13=(24, 43, 56)
print(tupla13[2])

print ("------------")

#Ejercicio14: crear una lista con 5 numeros flotantes y realizar la suma de todos los elementos

tupla14=[1.1, 2.2, 3.3, 4.4, 5.5]
print(sum(tupla14))

print ("------------")

#Ejercicio15: crear una lista con 4 elementos enteros luego convertir la lista en una tupla y mostrarla

lista15=[1, 2, 3, 4,]
tupla23=tuple(lista15)
print(tupla23)

print ("------------")

#Ejercicio16: crear una tupla con 3 elementos y convertirla en una lista luego agrega un nuevo numero a la lista

tupla16=(11, 22, 33)
lista20=list(tupla16)
lista20.append(44)
print(lista20)

print ("------------")

#Ejercicio17: crear una lista con 5 elementos y convertirla en una tupla luego muestra el tercer elemento de la tupla

lista2=[1, 2, 3, 4, 5]
tupla17=(1, 2, 3, 4, 5)
print(tupla17[2])

print ("------------")

#Ejercicio18: crear una tupla con 3 elementos y convertirla en una lista luego reemplaza el segundo elemento de la lista por un nuevo numero propocionado por el usuario

tupla18=(7, 8, 9)
lista19=(7, 8, 9)
lista200=int(input("ingrese un nuevo numero: "))
lista19[1]=lista200
print(lista19)

print ("------------")

#Ejercicio19: crear una lista de 4 numeros y convertirla en una tupla luego muestra la cantidad de elementos en la tupla

lista19=[2, 4, 6, 8]
tupla111=(2, 4, 6, 8)
print(len(tupla111))

print ("------------")

#Ejercicio20: crear una tupla con 5 elementos y convertirla en una lista luego elimina el ultimo elemnto de la lista 

tupla20=(1, 2, 3, 4, 5)
lista50=list(tupla20)
lista20=lista20[:-1]
print(lista20)

