import random
import time

opcion = int(input("Ingrese la opcion deseada, 0 para salir "))

while(opcion != 0):
    if(opcion == 1):
        #ejercicio 0, genera un numero aleatorio y muestra los numeros hasta ese numero
        numRandom = random.randint(0,500) #se genera un numero aleatorio entre 0 y 500 
        #a = int(input("Ingrese un numero: "))
        b = 0
        while(b < numRandom): #mientras b(0) sea menor al numero aleatorio, este ira incrementando hasta llegar al numero aleatorio
            b += 1
            print(b)
        print("El numero aleatorio es ",numRandom, ". proceso terminado a las ",time.clock())
        break




    elif(opcion == 2):
        #ejercicio 1, crear una funcion max que muestre el mayor de 2 numeros.
        a = int(input("Ingrese un numero: "))
        b = int(input("Ingrese otro numero: "))

        def max(a,b):
            if(a > b):
                resultado = a
            else:
                resultado = b
            return resultado
        fun = max(a,b) 
        print ("el numero mayor es ",fun)
        break




    elif(opcion == 3):
        #ejercicio 2, crear una funcion max_de_tres que muestre el mayor de 3 numeros.

        max1 = int(input("ingrese un numero: "))
        max2 = int(input("ingrese otro numero: "))
        max3 = int(input("ingrese el ultimo numero: "))

        def max_de_tres(max1,max2,max3):
            if(max1 > max2 and max1 > max3):
                mayor = max1
            elif(max2 > max1 and max2 > max3):
                mayor = max2
            else:
                mayor = max3

            return mayor

        fun = max_de_tres(max1,max2,max3)
        print("El mayor de los tres numeros ingresados es: ",fun)
        break



    elif(opcion == 4):
        ing = raw_input("Ingrese cualquier cosa: ")
        print(len(ing))

        #print(longitud)



    elif(opcion == 0):
        print("Adios")
        break