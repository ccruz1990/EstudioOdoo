#-------------Video 53 Curso Python Interfaces Gráficas XII-----------------
from tkinter import *
from tkinter import messagebox
root = Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Alex", "Procesador de textos versión 2022")

def infoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
    valor=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
    if valor=="yes":
        root.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar","No es posible cerrar, documento bloqueado")
    if valor==False:
        root.destroy()

barraMenu = Menu()
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

edicionMenu=Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")

herramientaMenu=Menu(barraMenu, tearoff=0)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=edicionMenu)
barraMenu.add_cascade(label="Herramienta", menu=herramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

root.mainloop()