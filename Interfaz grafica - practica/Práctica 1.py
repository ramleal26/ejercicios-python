from tkinter import *

#raiz

cuadroprincipal = Tk()
marco = Frame() 
marco.pack()

#texto 1

texto1 = Label(marco, text = "Nombre: ")
texto1.grid(row = 0, column = 0)
entradanombre = Entry(marco)
entradanombre.grid(row = 0, column = 1)
                   
#texto 2
 
texto2 = Label(marco, text = "Apellido: ")
texto2.grid(row = 1, column = 0)    
entradanombre2 = Entry(marco)
entradanombre2.grid(row = 1, column = 1)


#texto 3

texto3 = Label(marco, text = "Direccion: ")
texto3.grid(row = 2, column = 0)    
entradanombre3 = Entry(marco)
entradanombre3.grid(row = 2, column = 1)

#texto 4

texto4 = Label(marco, text = "Direccion 2: ")
texto4.grid(row = 3, column = 0)    
entradanombre4 = Entry(marco)
entradanombre4.grid(row = 3, column = 1)

#comentarios

comentarios = Label(marco, text = "Comentarios: ")
comentarios.grid(row = 4, column = 0)    

cajacomentario = Text(marco, width = 15, height = 5)
cajacomentario.grid(row = 4, column = 1)

#boton

boton = Button(marco, text = "Hola", padx = 10)
boton.grid(row = 5, column = 1)

#scrollbar 


scrollbar = Scrollbar(marco, command = cajacomentario.yview) 
scrollbar.grid(row= 4, column = 2, sticky = "nsew")

cajacomentario.config(yscrollcommand = scrollbar.set)

cuadroprincipal.mainloop()






        