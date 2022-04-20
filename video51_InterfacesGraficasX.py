#-------------Video 51 Curso Python Interfaces Gráficas X-----------------
from tkinter import *
root = Tk()
root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViaje():
    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+=" Playa"
    if(montagna.get()==1):
        opcionEscogida+=" Montaña"
    if(turismoRural.get()==1):
        opcionEscogida+=" Turismo rural"

    textoFinal.config(text=opcionEscogida)

#foto=PhotoImage(file="avion.png")
#Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()