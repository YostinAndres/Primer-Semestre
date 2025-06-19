#EJEMPLO DE WHILE
contador=1
while contador <= 100:
    print("contador:", contador)
    contador +=1
    
print("------------")

#EJEMPLO WHILE TRUE
while True:
    texto=input("escribe algo(o escribe 'salir' para terminar):")
    if texto=="salir":
        break
    print("escribiste:",texto)