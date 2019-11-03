#!/usr/bin/env python3
from tkinter import Tk, Frame, Entry, Button, NW, Label, scrolledtext, INSERT, LEFT, END, EW


class Verfahren():
    def __init__(self, tkobj):
        #Label - Verfahren
        self.lblVerf = Label(tkobj, text='Verfahren \n', font=('Arial', 15))
        self.lblVerf.grid(column=0, row=0, pady=5, padx=5, sticky=(NW))

        #Buttons für Verf Entries und Textfeld
        #Ausgabe der Entries als Liste
        self.all_Verf = []
        self.addVerfahren = Button(tkobj, text='+', fg='Red', command=self.__addVerf)
        self.addVerfahren.grid(column=0, row=1, pady=5, padx=5, sticky=(NW))

        self.remVerfahren = Button(tkobj, text='-', fg='Dark Blue', command=self.__remVerf)
        self.remVerfahren.grid(column=1, row=1, pady=5, padx=5, sticky=(NW))

        self.EntryVerf = Frame(tkobj)
        self.EntryVerf.grid(column=0, row=2, pady=5, padx=5, sticky=(NW))
        
    def __addVerf(self):
        self.frameVerf = Frame(self.EntryVerf) #Erstellung eines Frames
        self.frameVerf.pack()
        
        self.frameVeAb = Frame(self.frameVerf)
        self.frameVeAb.grid(row=1, column=0, sticky=(NW))
        self.frameVeTe = Frame(self.frameVerf)
        self.frameVeTe.grid(row=2, column=0, sticky=(NW))
        
        Label(self.frameVeAb, text='Abschnitt', font=12, justify=LEFT).grid(row=0, column=0, padx=5, pady=5, sticky=(NW)) #Bezeichnung des Entries

        self.entVerf = Entry(self.frameVeAb, width=60, background='white') #Entry-Feld
        self.entVerf.grid(column=1, row=0, padx=36, pady=5, sticky=(EW))
        
        Label(self.frameVeTe, text='Beschreibung', font=12).grid(column=0, row=2, padx=5, pady=5, sticky=(NW)) #Bezeichnung der Textbox

        self.txtVerf = scrolledtext.ScrolledText(self.frameVeTe, relief='sunken', width=60, height=5, background='white') #Textbox
        self.txtVerf.insert(INSERT, 'Bitte geben sie Text ein! ') #Vorgegebener Text
        self.txtVerf.grid(column=1, row=2, padx=5, pady=5, sticky=(EW))

        self.all_Verf.append((self.entVerf, self.txtVerf, self.frameVerf)) # Plus-Button hängt o.g. Objekte an die Bestehenden an.    

    def __remVerf(self):
        if len(self.all_Verf)>0: #wenn elemente in all_Verf vorhanden sind
            self.all_Verf[-1][2].forget() #vergessen des übergeordneten Frames (frameVerf) des graphischen Objektes (pack/grid)
            self.all_Verf[-1][2].destroy() #zerstören des Frameobjektes (Unterobjekte werden mitzerstört)
            self.all_Verf.pop(-1) #letztes Element der Liste wird aus dem Speicher entfernt
        else:
            pass

    def get(self):
        temp = []
        for e in self.all_Verf: #Element dieser Liste = Liste mit zwei Elementen ['', '']
            nlist = [e[0].get(), e[1].get(1.0, END)] #Erstellung einer Hilfslist aus den Sublisten
            temp.append(nlist) #Liste von Daten wird an Liste angehängt
        return temp
    
    def set(self, arg):
        while len(self.all_Verf)>0:
            self.__remVerf() #entfernt alle Entryfelder
        for index,elem in enumerate(arg): #iterieren durch die übergebenen Elemente 
            self.__addVerf() #hinzufügen der Entries
            self.all_Verf[index][0].insert(0, elem[0]) #einfügen des str aus der Liste Position 0 von TVerf
            self.all_Verf[index][1].delete(1.0, END) #löschen des initialen Inhalts
            self.all_Verf[index][1].insert(1.0, elem[1]) #einfügen des str aus der Liste Position 1 von TVerf
            


if __name__ == "__main__":
    root = Tk()
    root.title('Test Verfahren')
    root.geometry('800x600')

    verfahren = Verfahren(root)
    
    verf = [['a', 'irgendwas'], ['b', 'was anderes'], ['c', 'noch mehr']]
    
    verfahren.set(verf)
    print(verfahren.get())
    
    
    
    root.mainloop()
