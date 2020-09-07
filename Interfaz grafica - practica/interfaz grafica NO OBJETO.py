from tkinter import *

raiz = Tk()        

raiz.title("Ventana")

raiz.resizable(1,1)

raiz.config(bg = "white")
 
raiz.iconbitmap("ecohome.ico")

miFrame = Frame()

miFrame.pack()

miFrame.config(bg = "blue")

miFrame.config(width = "720", height = "320")

w = Label(miFrame, text = "HOLA", fg = "red").place(x=100, y=200)

photo = PhotoImage(file ="")

 



raiz.mainloop()