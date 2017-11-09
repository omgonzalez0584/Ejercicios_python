#Crear una funcion y usar input
#def hola(persona):
 #   print("Hola",persona)

#a = input("Introduzca el nombre: ")
#hola(a)


#Ejercicio 2.4 Ciclo definido entre 10 a 20
#for x in range(10,20):
#    print(x)

#Ejercicio 2.5 Ciclo definido que salude a tus 5 mejores amigos
#for x in ['ERIC','ARMANDO','BETO','KILY','PUPI']:
 #   print("Hola",x)


#Ejercicio 2.6 Ciclo definido que pregunte nombre de 5 amigos y los salude
#for x in range(5):
 #   a = input("Amigo a Saludor: ")
  #  hola(a)


#Ejercicio 2.8 Preguntar cuantos amigos y luego los amigos
#a = int(input("Introduzca cuantos amigos desea saludar: "))
#for x in range(a):
 #   b = input("Amigo que desea Saludar: ")
  #  hola(b)


#Ejercicio 3.1

#def repite_hola(n):
 #   for i in range(n):
  #      print("Hola!")

#repite_hola(3)

#Ejercicios 3.2
#def repite_holaII(n):
 #   return n*'hola'

#c = int(input("Introduzca las n concatenaciones"))
#a = repite_holaII(c)
#print(a)


#Ejercicio 3.3
#def repite_saludo(n,saludo):
 #   for i in range(n):
  #      print(saludo)
#saludo = input("Introduzca el saludo:" )
#n = int(input("La cantidad de saludos: "))
#repite_saludo(n,saludo)


#Ejemplo de retornar 3 valores en una funcion
#def aHsMinSeg(x):
 #   hs = x / 3600
  #  min = (x%3600)/60
   # seg = ( x % 3600) % 60
    #return(hs,min,seg)


#(h,m,s) = aHsMinSeg(3661)
#print(h)
#print(m)
#print(s)


#Ejemplo dado un numero escribir si es positivo o negativo - Usando if y else
#def tipo_num(num):
 #   if num > 0:
    #    print("Es positivo")
  #  else:
     #   print("Es negativo")

#num = int(input("Introduzca un numero"))
#tipo_num(num)

#4.3 Coordenadas en el plano cartsiano

#def plano_cartesiano(x,y):
 #   if x > 0 and y > 0:
  #      print("Estan en el tercer cuadrante")

   # elif x < 0 and y > 0:
    #    print("Estan en el segundo cuadrante")

#    elif x < 0 and y < 0:
 #       print("Estan en el tercer cuadrante")

  #  elif x > 0 and y < 0:
   #     print("Estan en el cuarto cuadrante")

    #else:
     #   print("Debe colocar numeros positivos o negativos, no colocar cero")


#x = int(input("Introduzca X: "))
#y = int(input("Introduzca y: "))
#plano_cartesiano(x,y)


#5.1Ejemplo ciclo n numeros e ingresar si son positivos o negativos
#def tipo_numero(num):
 #   if num > 0:
  #     print("Es positivo")
   # elif num < 0:
    #    print("Es negativo")
    #else:
     #   print("Es cero")

#ciclo = int(input("Intruzca la cantidad de repeticiones: "))
#for i in range(ciclo):
 #  tipo_numero(int(input("Ingrese el numero: ")))


#5.4 Nueva version del 5.1

#def tipo_numero_5_4():
 #   while True:
  #      x = input("Introduzca el numero(Presione * para salir): ")
   #     if x == "*":
    #        break
     #   elif int(x) > 0:
      #      print("Es positivo")
       # elif int(x) < 0:
          #  print("Es negativo")
        #else:
         #   int(x)
          #  print("Es cero")

#tipo_numero_5_4()


#6.1 Programa que un ciclo escribas una cadena del fina al principio
#cadena = input("Introducir cadena: ")
#print(cadena)
#x = len(cadena)

#for i in range(1,x+1):
 #   i = -i
  #  print(cadena[i])


#6.2 Contar cuantas A tiene una cadena de caracteres

#def contar_cadena(a):
 #   cont = 0
  #  for i in a:
   #     if i == 'A' or i == 'a':
   #         cont = cont +1
    #print("Esta cadena tiene",cont,"A")

#texto = input("Introduzca el texto: ")
#contar_cadena(texto)

#6.6 Programa que cuente cuantas vocales hay de cada una en un texto
#def contar_vocales(texto):
 #   contar_a = 0
  #  contar_e = 0
   # contar_i = 0
    #contar_o = 0
    #contar_u = 0
    #for i in texto:
     #   if i == 'A' or i == 'a':
      #      contar_a = contar_a + 1
       # elif i == 'E' or i == 'e':
        #    contar_e = contar_e + 1
        #elif i == 'I' or i == 'i':
         #   contar_i = contar_i + 1
        #elif i == 'O' or i == 'o':
         #   contar_o = contar_o + 1
        #elif i == 'U' or i == 'u':
         #    contar_u = contar_u + 1

    #print("Tenemos ",contar_a," a")
    #print("Tenemos ",contar_e," e")
    #print("Tenemos ",contar_i," i")
    #print("Tenemos ",contar_o," o")
    #print("Tenemos ",contar_u," u")

#texto = input("Introduzca el texto")
#contar_vocales(texto)

#Programa que ordena elementos de una lista

a = [5,3,2,4,1]
b = []
x = len(a)
for i in range(x):
    for j in range(x):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)


# Tuplas
#t = (89766,"Alicia","Hacker",(9,"Julio",1988))
#print(len(t))

#Tupla unitaria
#u =(1980,)
#print(len(u))
#print(u)


#Listas
#xs = [1,2,3,4,5,6,7]

#agregar
#xs.append(20)
#print(xs)

#insertar
#xs.insert(2,30)
#print(xs)

#Borrar
#xs.remove(4)
#print(xs)

#buscar elementos
#print(10 in xs)
#print(2 in xs)

#Posicion de un elemento de la lista
#print(xs.index(3))

#for i in xs:
 #   print(i)



#7.1 Agregar numero de Padron de matricula, validar si ya existe.

xs = []
while True:
    padron = input("Introduzca el numero de Padron(Escriba * para salir: ")
    if padron == '*':
        print("Adios...")
        break
    if padron in xs:
        print("Error!, Padron existe , favor escribir uno nuevo....")

    else:
        xs.append(padron)

if len(xs)>0:
    print("Lista de padrones inscritos: ", xs)
else:
    print("No se han inscrito padrones a esta materia")





































