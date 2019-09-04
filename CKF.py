"""
ingreso = int(input("Ingrese un numero 1 si quiere conversión Celsius a Fahrenheit, 2 si quiere Celsius a Kelvin y 3 si quiere Fahrenheit a Kelvin"))

if(ingreso == 1):
    n1 = (float(input("Ingrese los grados Celsius que quiere convertir a Fahrenheit"))
    total = n1*(9/5)+32
    print("El total es ", total)
          
elif(ingreso == 2):
    n2 = (float(input("Ingrese los grados Celsius que quiere convertir a Kelvin"))
    total = n1+273.15
    print("El total es ",total)

elif(ingreso == 3):
    n3 = (float(input("Ingrese los grados Fahrenheit que quiere convertir a Kelvin"))
    total = (n1+459.67)*5/9
    print("El total es ",total)

else:
    print("Numero invalido :c")
"""




print("1. Celsius a Fahrenheit")
print("2. Kelvin a Celsius")
print("3. Kelvin a Fahrenheit")
op = int(input("Ingrese la opción deseada: "))


if(op == 1):
    op1 = input("Desea que sea de C a F o viceversa?")
    if(op1 =='c' or op1 == 'C'):
        c = int(input("ingrese grados celsius"))
        f = c*(9/5)+32
        print("el resultado es ",f)
    elif(op1 == 'v' or op1 == 'V'):
        f = int(input("ingrese grados fahrenheit"))
        c = (f-32)/1.8
        print("el resultado es ",c)

elif(op == 2):
    op1 = input("Desea que sea de Celsius(k) a Kelvin(K) o viceversa?")
    if(op1 =='k' or op1 == 'K'):
        c = int(input("ingrese grados Celsius"))
        k = k+273.15
        print("el resultado es ",k)
    elif(op1 == 'v' or op1 == 'V'):
        k = int(input("ingrese grados kelvin"))
        c = k-273.15
        print("el resultado es ",c)

elif(op == 3):
    op1 = input("Desea que sea de Fahrenheit a Kelvin o viceversa?")
    if(op1 =='k' or op1 == 'K'):
        f = int(input("ingrese grados Fahrenheit"))
        k = (f+459.67)*(5/9)
        print("el resultado es ",k)
    elif(op1 == 'v' or op1 == 'V'):
        k = int(input("ingrese grados Kelvin"))
        f = (k/0.56)-459.67
        print("el resultado es ",f)
else:
    print("Opción no válida :p")
