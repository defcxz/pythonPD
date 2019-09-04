    #ejercicio 1
verduleria = {"Frutilla":1000,
    "Manzana":650,
    "Limones":500,
    "Tomates":800,
    "Papas":600}

ingreso = input("Ingrese una fruta o verdura: ")

#preguntamos la existencia del ingreso del usuario
if(ingreso in verduleria):
    print("Si hay")
    resultado = verduleria.get(ingreso)
    print("Lo que usted quiere cuesta",resultado)
else:
    print("No hay. F")



    #ejercicio 2
saludos = { "Espaniol": "Hola",
            "Frances": "Salut",
            "Aleman": "Hallo",
            "Croata": "Bok",
            "Mapudungun": "Mari Mari"}

ingreso = input("Ingrese un idioma: ")

if(ingreso in saludos):
    print(saludos.get(ingreso))
else:
    opcion = input(print("El idioma que usted ingresó no se encuentra disponible, pero puede añadirlo al diccionario, quiere añadirlo?"))
    if(opcion == "si"):
        saludos[ingreso] 
        print(saludos)
        
            

