#!/usr/bin/env python3
from tkinter import Tk, Frame, Entry, Button, NW, Label, EW, scrolledtext, INSERT, END


class AbkDef():
    def __init__(self, tkobj):
        #Label - AbkDef
        self.lblAbkDef = Label(tkobj, text='Abkürzungen und Definitionen \n', font=('Arial', 15))
        self.lblAbkDef.grid(column=0, row=0, pady=5, padx=5, sticky=(NW))

        self.lblAbk = Label(tkobj, text='Abkürzungen \n', font=('Arial', 13))
        self.lblAbk.grid(column=0, row=1, pady=5, padx=5, sticky=(NW))

        self.lblNewLine = Label(tkobj, text='\n ')
        self.lblNewLine.grid(column=0, pady=5, padx=5, row=4)

        self.lblDef = Label(tkobj, text='Definitionen \n', font=('Arial', 13))
        self.lblDef.grid(column=0, row=5, pady=5, padx=5, sticky=(NW))

        #Button für Abk Entries bzw Def Entries
        #Ausgabe der Entries als Liste
        self.all_Abk = []
        self.addAbkürzung = Button(tkobj, text='+', fg='Red', command=self.__addAbk)
        self.addAbkürzung.grid(column=0, row=2, pady=5, padx=5, sticky=(NW))

        self.remAbkürzung = Button(tkobj, text='-', fg='Dark Blue', command=self.__remAbk)
        self.remAbkürzung.grid(column=1, row=2, pady=5, padx=5, sticky=(NW))

        self.all_Def = []
        self.addDefinition = Button(tkobj, text='+', fg='Red', command=self.__addDef)
        self.addDefinition.grid(column=0, row=6, sticky=(NW))

        self.remDefinition = Button(tkobj, text='-', fg='Dark Blue', command=self.__remDef)
        self.remDefinition.grid(column=1, row=6, pady=5, padx=5, sticky=(NW))

        #Frame für Add Entry
        self.EntryAbk = Frame(tkobj)
        self.EntryAbk.grid(column=0, row=3, pady=5, padx=5, sticky=(NW))

        #Frame für Def Entry
        self.EntryDef = Frame(tkobj)
        self.EntryDef.grid(column=0, row=7, pady=5, padx=5, sticky=(NW))
        
    def __addAbk(self):
        self.frameAbk = Frame(self.EntryAbk) 
        self.frameAbk.pack()

        self.entAbk01 = Entry(self.frameAbk, width=5, background='white')
        self.entAbk01.grid(column=0, row=0, pady=5, sticky=(NW))

        self.entAbk02 = Entry(self.frameAbk, width=60, background='white')
        self.entAbk02.grid(column=1, row=0, padx=15, pady=5, sticky=(NW))

        self.all_Abk.append((self.entAbk01, self.entAbk02, self.frameAbk))
    
    def __remAbk(self):
        if len(self.all_Abk)>0: #wenn elemente in all_Abk vorhanden sind
            self.all_Abk[-1][2].forget() #vergessen des übergeordneten Frames (frameAbk) des graphischen Objektes (pack/grid)
            self.all_Abk[-1][2].destroy() #zerstören des Frameobjektes (Unterobjekte werden mitzerstört)
            self.all_Abk.pop(-1) #letztes Element der Liste wird aus dem Speicher entfernt
        else:
            pass
        
    #Definition des Add Entry Buttons
    def __addDef(self):
        #Hinzufügen eines Textfeldes
        self.txtDef = scrolledtext.ScrolledText(self.EntryDef, relief='sunken', width=70, height=5, background='white', undo=True)
        #insert content
        self.txtDef.insert(INSERT,'Bitte geben Sie Text ein! ')
        self.txtDef.pack(pady=5)
        
        self.all_Def.append(self.txtDef)
        
    def __remDef(self): #(forget, destroy, remove from list)
        if len(self.all_Def)>0: #wenn elemente in all_Def vorhanden sind
            self.all_Def[-1].forget() #vergessen des graphischen Objektes (pack/grid), dass es zum frame gehört
            self.all_Def[-1].destroy() #zerstören des Objekte 
            self.all_Def.pop(-1) #letztes Element der Liste wird aus dem Speicher entfernt
        else:
            pass
    
    
    def getAbk(self):
        temp = []
        for e in self.all_Abk: #Element dieser Liste = Liste mit zwei Elementen ['', '']
            nlist = [e[0].get(), e[1].get()] #Erstellung einer Hilfslist aus den Sublisten
            temp.append(nlist) #Liste von Daten wird an Liste angehängt
        return temp
    
    def setAbk(self, arg):
        while len(self.all_Abk)>0:
            self.__remAbk() #entfernt alle Entryfelder
        for index,elem in enumerate(arg): #iterieren durch die übergebenen Elemente 
            self.__addAbk() #hinzufügen der Entries
            self.all_Abk[index][0].insert(0, elem[0]) #einfügen des str aus der Liste Position 0 von TAbk
            self.all_Abk[index][1].insert(0, elem[1]) #einfügen des str aus der Liste Position 1 von TAbk
    
    def getDef(self):
        temp = []
        for e in self.all_Def: #Holen jedes Elements e der Objektliste all_Def 
            temp.append(e.get(1.0, END)) #get() holt vom Objekt e den str und hängt ihn an die Datenliste temp
        return temp
    
    def setDef(self, arg):
        while len(self.all_Def)>0:
            self.__remDef() #entfernt alle Textfelder
        for index,elem in enumerate(arg): #iterieren durch die übergebenen Elemente
            self.__addDef() #hinzufügen eines Textfeldes
            self.all_Def[index].delete(1.0, END) #löschen des initialen Inhalts
            self.all_Def[index].insert(1.0, elem) #einfügen des str aus der Liste


    
     

           
if __name__ == "__main__":
    root = Tk()
    root.title('Test Tab')
    root.geometry('600x450')

    abkdef = AbkDef(root)
    
    abk = [['a', 'irgendwas'], ['b', 'was anderes'], ['c', 'noch mehr']]
    
    abkdef.setAbk(abk)
    #abkdef.setAbk([])
    
    print( abkdef.getAbk() )
    
    abkdef.setDef(['hallo welt', 'blub'])

    root.mainloop()
