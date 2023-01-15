## Aplicacion de web scrapping con interface grafica 
## librerias beautiful soup y tkinter
import requests
from bs4 import BeautifulSoup
from tkinter import *
from module.funciones import *
from tkinter.messagebox import *
## Funciones
def limpiar_campos():
    entry_text.config(text="")
## Variables
## Interface grafica
raiz = Tk()
raiz.geometry("500x180")
raiz.title("Scrapping con GUI Y BeautifulSoup")
raiz.resizable(0,0)
###Frames
main_frame = Frame(raiz, width=480, height=140)
main_frame.config(background="#fff")
main_frame.grid(row=0, column=0, padx=0, pady=10)
main_frame.grid_propagate(False)
main_frame.pack()
secound_frame = Frame(raiz, width=480)
secound_frame.config(background="#fff")
secound_frame.pack()
###Widgets
busqueda = StringVar()
nombreArchivo = StringVar()

entry_text = Entry(main_frame, width=50, textvariable=busqueda)
entry_text.grid(row=0, column=0, padx=10, pady=1)
name_label = Label(main_frame, text="Nombre del archivo: ")
name_label.grid(row=1, column=0, padx=10, pady=10)
entry_name = Entry(main_frame, width=20, textvariable=nombreArchivo)
entry_name.grid(row=1, column=1, padx=10, pady=10)
## para ejecutar y desplegar en la GUI
def execute_gui():
    try:
        articulos = list_search(entry_text.get())
        export_to_txt(articulos, entry_name.get())
        limpiar_campos()
        showwarning("Listo", "Busqueda realizada con Exito !!")
    except:
        showerror("Error", "Error al realizar consulta")
##App programing
if __name__ == "__main__":
    ## APP EXECUTION
    btn_search = Button(main_frame, text="Buscar", width=20, command=execute_gui).grid(row=0, column=1, padx=10, pady=10)
    btn_exit = Button(secound_frame, text="SALIR", width=20, command=raiz.quit).grid(row=5, column=0,padx=10, pady=0)
    raiz.mainloop()
