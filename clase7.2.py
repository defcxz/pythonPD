pago = int(input("Ingrese valor a pagar:\n"))
billete = int(input("Ingrese billete con el que se pagará:\n"))

if(billete == 1000 or billete == 2000 or billete == 5000 or billete == 10000 or billete == 20000):
    def total (pago,billete):
        vuelto = (billete-pago)
        return(vuelto)
    vueltoxd = total(pago,billete)
    print("Su vuelto será de: ",vueltoxd)

else:
    print("Ingreso no válido xdddxddxdxd gsgfdfg")



    
