#-------------Video 46 Curso Python Interfaces Gráficas V-----------------
from tkinter import *
root = Tk()
miFrame=Frame(root)
miFrame.pack

pantalla=Entry(miFrame)
pantalla.grid(row=1, column=1, padx=10, pady=10)
pantalla.config(bg="black", fg="green", justify="right")

root.mainloop()
#---------------------------------------------------------------------------