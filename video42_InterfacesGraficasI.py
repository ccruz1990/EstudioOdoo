#-------------Video 42 Curso Python Interfaces Gráficas I-----------------

from tkinter import *

raiz=Tk()

raiz.title("Ventana")

#raiz.resizable(0,0)

raiz.iconbitmap("postgres_icon.ico")

#raiz.geometry('400x300')

miFrame = Frame()
miFrame.pack(fill="both", expand="True")
miFrame.config(bg="red")
miFrame.config(width=350, height=400)
miFrame.config(bd=15)
miFrame.config(relief="groove")
miFrame.config(cursor="hand2")

raiz.mainloop()
#---------------------------------------------------------------------------