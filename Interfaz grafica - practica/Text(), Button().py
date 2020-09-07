from tkinter import *

raiz = Tk()
raiz.resizable(1,1)



frame1 = Frame()
frame1.pack()

textocomentarios = Label(frame1, text = "Comentarios: ", width = 10, height = 12)
textocomentarios.grid(row = 0, column = 0)



cajacomentarios = Text(frame1, width = 10, height = 5)
cajacomentarios.grid(row = 0, column = 1)


boton = Button(raiz, text="cacatua")
boton.pack()


raiz.mainloop()
