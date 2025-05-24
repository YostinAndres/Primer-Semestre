x,y,z = 1,4,8
print(x)
print(y)
print(z)

print ("------------")

x=y=z=0
print(x)
print(y)
print(z)

print ("------------")

x=10
x=x+5
print (x)

print ("------------") 

a=b=c=0
print(a,b,c)

print ("------------")

opa="hola "
opa+="a "
opa+="todos "
print(opa)

print ("------------")

Y="CONTENACION"
texto1="hola "
texto2="mundo"
resultado=texto1+""+texto2
print(resultado)

print ("------------")

Y="BUSQUEDA"
mensaje="hola mundo"
buscar=mensaje.find("mundo")
print(buscar)


print ("------------")

Y="EJERCICIOS"

y="CONCATENACION"

frase="el conocimiento es poder"
print(frase.find("conocimiento"))
print(frase.find("poder"))

print ("------------")

frase1="La practica hace al maestro"
print(frase1.find("practica"))
print(frase1.find("maestro"))

print ("------------")

Y="CONCATENACION I INTERACCION"

frase2=input("ingrese una frase: ")
frase3=input("ingrese la palabra: ")
print(frase2.find(frase3))

print ("------------")

texto5="Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"

print(texto5.find("Sabia"))
print(texto5.find("Caminaba"))
print(texto5.find("falanges"))

print ("------------")

texto7="Algunos días del año se interrumpía el tráfico y la industria de Ribamoura. El pueblo entero se congregaba a celebrar las solemnidades consuetudinarias, que servían de pretexto para solaces y holgorio. Tal ocurría con el Carnaval, tal con la fiesta de la Patrona, tal con los días de la Semana Santa. A pesar de ser éstos de penitencia y mortificación, para los de Ribamoura tenían carácter de fiesta; en ellos se celebraba, en la iglesia principal, espacioso edificio de la época herreriana, la representación de la Pasión, con personajes de carne y hueso, y encargándose de los papeles gente del pueblo mismo"

print(texto7.find("congregaba"))
print(texto7.find("A"))
print(texto7.find("mismo"))

print ("------------")

nombre=input("buenas tardes señor usuario, digite su nombre")
nota_1=float(input("ingrese la primera nota: "))
nota_2=float(input("ingrese la segunda nota: "))
nota_3=float(input("ingrese la tecera nota: "))

nota_final=(nota_1 * 0.2) + (nota_2 * 0.3) + (nota_3 * 0.5)

print("Hola", nombre, ", tu nota final es: ", nota_final)