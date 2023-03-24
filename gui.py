import csv
import webbrowser
from tkinter import *
from tkinter import ttk

class Aplication():
    def __init__(self):
        self.app = Tk()
        self.app.title('WhatsApp Dialer for desktop')
        #A la izq aplicamos un Listbox con los paises
        self.paises = ttk.Label(self.app, text='Elija el país')
        self.paises.grid(column=0, row=0)
        #Aplicamos método para crear y llenar Listbox
        self.importar()
        self.listpaises.bind("<<ListboxSelect>>", self.onselect)
        #Solicitamos el número de WhatsApp, luego de elegir país
        self.solicitud = ttk.Label(self.app, text='Ingrese el número de WhatsApp')
        self.solicitud.grid(column=2, row=0)
        #Creamos variable para el entry
        self.numero = StringVar()
        self.entrynumero = ttk.Entry(self.app, textvariable=self.numero, width=20)
        self.entrynumero.grid(column=2, row=1)

        self.enviar = ttk.Button(self.app, text='Escribir', command=self.lanzar)
        self.enviar.grid(column=2, row=2)
        self.app.mainloop()

    def importar(self):
        with open('prefijos.csv', newline='') as table:
            self.scroll = Scrollbar(self.app, orient=VERTICAL)
            self.countries = csv.reader(table)
            self.listpaises = Listbox(self.app, yscrollcommand=self.scroll.set)
            self.listpaises.grid(column=0, row=1)
            self.scroll.configure(command=self.listpaises.yview)
            self.scroll.grid(column=1, row=1, sticky='NS')
            next(self.countries)
            for row in self.countries:
                self.country = row[0]
                self.listpaises.insert(END, self.country)

    def onselect(self, event):
        with open('prefijos.csv', newline='') as table:
            self.countries = csv.reader(table)
            self.prefixes = []
            next(self.countries)
            for row in self.countries:
                self.prefixes.append(row[5])
            self.selection = event.widget.curselection()
            if self.selection:
                self.index = self.selection[0]
                self.code = self.prefixes[self.index]
            return self.code

    def lanzar(self):
        self.marcar = self.numero.get()
        webbrowser.open("https://api.whatsapp.com/send?phone="+self.code+self.marcar)



execution = Aplication()
