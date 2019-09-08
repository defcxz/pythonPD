import random
import time


numRandom = random.randint(0,500) #se genera un numero aleatorio entre 0 y 500 
#a = int(input("Ingrese un numero: "))
b = 0
while(b < numRandom): #mientras b(0) sea menor al numero aleatorio, este ira incrementando hasta llegar al numero aleatorio
    b += 1
    print(b)
print("El numero aleatorio es ",numRandom, ". proceso terminado a las ",time.clock())