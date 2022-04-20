#-------------Video 44 Curso Python Interfaces Gráficas III-----------------
from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)
miFrame.pack()

miImagen = PhotoImage(file="banana-gif.gif")
Label(miFrame, image=miImagen).place(x=100, y=200)
#Label(miFrame, text="Hola mundo", font=("Comic Sans MS", 18)).place(x=100, y=200)

root.mainloop()
#---------------------------------------------------------------------------