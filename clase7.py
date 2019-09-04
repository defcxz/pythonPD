#def <nombre> (<variables a usar>):
n1 = float(input("Ingrese la primera nota de cátedra:\n"))
n2 = float(input("Ingrese la segunda nota de cátedra:\n"))
n3 = float(input("Ingrese la tercera nota de cátedra:\n"))
def prom_cat(n1,n2,n3):
    prom = (n1+n2+n3)/3
    return(prom)
promedioCat = prom_cat(n1,n2,n3)
print("Su promedio de cátedra es: ",promedioCat,"\n")

n4 = float(input("Ingrese la primera nota de trabajo:\n"))
n5 = float(input("Ingrese la segunda nota de trabajo:\n"))
def promLab(n4,n5):
    prom2 = (n4+n5)/2
    return(prom2)

promedioLab = promLab(n4,n5)
print("Su promedio de Laboratorio es:",promedioLab,"\n")

promedioGen = (promedioCat+promedioLab)/2

if(promedioGen < 4.0):
    print("No aprobó el curso, tuvo nota de",promedioGen)
else:
    print("Aprobó el curso con nota de",promedioGen)
