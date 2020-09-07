from tkinter import *

cuadroprincipal = Tk()
marco = Frame()
marco.pack()



#pantalla 

pantalla = Entry(marco)
pantalla.grid(row = 1, column = 1, padx = 10, pady = 10)
pantalla.config(bg ="white", fg = "green", justify = "right")














cuadroprincipal.mainloop()