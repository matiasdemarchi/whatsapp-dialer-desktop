import csv
import webbrowser
from tkinter import *
from tkinter import ttk


class Aplication:
    def __init__(self):
        self.app = Tk()
        self.app.title("WhatsApp Dialer for desktop")
        # A la izq aplicamos un Listbox con los paises
        self.paises = ttk.Label(self.app, text="Elija el país")
        self.paises.grid(column=0, row=0)
        # Aplicamos método para crear y llenar Listbox
        self.importar()
        self.listpaises.bind("<<ListboxSelect>>", self.onselect)
        # Solicitamos el número de WhatsApp, luego de elegir país
        self.solicitud = ttk.Label(
            self.app, text="Ingrese el número de WhatsApp"
        )
        self.solicitud.grid(column=2, row=0)
        # Creamos variable para el entry
        self.numero = StringVar()
        self.entrynumero = ttk.Entry(
            self.app, textvariable=self.numero, width=20
        )
        self.entrynumero.grid(column=2, row=1)
        # Creamos botón
        self.enviar = ttk.Button(
            self.app, text="Escribir", command=self.lanzar
        )
        self.enviar.grid(column=2, row=2)
        self.app.mainloop()

    def importar(self):
        # Abrimos un CSV con prefijos internacionales
        with open("prefijos.csv", newline="", encoding='UTF-8') as table:
            self.countries = csv.reader(table)
            # Scroll de la listbox
            self.scroll = Scrollbar(self.app, orient=VERTICAL)
            # Instanciamos la listbox integrando el scroll
            self.listpaises = Listbox(self.app, yscrollcommand=self.scroll.set)
            self.listpaises.grid(column=0, row=1)
            # Configuramos scroll
            self.scroll.configure(command=self.listpaises.yview)
            self.scroll.grid(column=1, row=1, sticky="NS")
            next(self.countries)  # Salteamos encabezado avanzando un row
            for row in self.countries:
                self.country = row[0]  # Con el [0] extraemos el nombre
                # Colocamos cada nombre al final del listbox
                self.listpaises.insert(END, self.country)

    def onselect(self, event):
        # Volvemos a abrir el CSV
        with open("prefijos.csv", newline="", encoding='UTF-8') as table:
            self.countries = csv.reader(table)
            self.prefixes = []  # Creamos una lista para cargar los prefijos
            next(self.countries)  # Salteamos encabezado
            for row in self.countries:
                self.prefixes.append(
                    row[5]
                )  # En el [5] se ubican los prefijos, con eso cargamos lista
            self.selection = (
                event.widget.curselection()
            )  # Colocamos un evento de seleccion
            if self.selection:  # Si el evento se cumple...
                self.index = self.selection[
                    0
                ]  # Extrae la posicion del registro seleccionado
                self.code = self.prefixes[
                    self.index
                ]  # Carga el prefijo de la posicion
            return self.code

    def lanzar(self):
        # Convertimos el StringVar del Entry a str mediante el método .get()
        self.marcar = self.numero.get()
        webbrowser.open(
            "https://api.whatsapp.com/send?phone=" + self.code + self.marcar
        )  # Concatenamos el link con el prefijo y el número cargado


execution = Aplication()
