from tkinter import *

raiz = Tk()

F = Frame(raiz, width=1200, height=600)
F.pack()


E = Entry(F)
E.grid(row = 0, column = 1) 

nombre = Label(F, text ="Apellido: ")
nombre.grid(row= 0, column = 0, sticky = "w")


E = Entry(F)
E.grid(row = 1, column = 1) 

nombre = Label(F, text ="nombre: ")
nombre.grid(row= 1, column = 0, sticky = "w")


E = Entry(F)
E.grid(row = 2, column = 1) 

nombre = Label(F, text ="Direccion : ")
nombre.grid(row= 2, column = 0, sticky = "w")



raiz.mainloop()