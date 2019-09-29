from tkinter import *

raiz = Tk()

raiz.title("Mi primera Ventana") #se determina el titulo de la ventana

ancho = 1
alto = 1
raiz.resizable(True,True) #determina si es redimensionable o no (0 = no, 1 = si)
#raiz.geometry("650x350")#determina el tamaño de la ventana, la raiz se adaptará al tamaño del frame
#raiz.config(bg = "red") #cambia el color de fondo

frame = Frame()
frame.pack()
frame.config(width = "500", height = "500") #se determina el color y tamaño del frame
#frame.config(relief = "sunken", bd = 25) #personalizar borders
#frame.config(cursor = "pirate")#personalizar cursores dentro del frame

Label(frame, text = "Hola, mundo!", fg = "red").place(x = 250, y = 100) #se inserta una label
Button(frame, text = "Prueba").place(x = 250, y = 150) #se crea un botón :p
raiz.mainloop() #se crea el loop infinito que mantiene abierta la ventana

