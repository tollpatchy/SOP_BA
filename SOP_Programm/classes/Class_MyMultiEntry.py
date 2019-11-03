#!/usr/bin/env python3
from tkinter import Tk, Frame, Entry, Button, NW, Label

class MyMultiEntry(Frame):
    def __init__(self, tkobj, text='', **kwargs):
        super().__init__(tkobj, **kwargs)
        
        #Label MyMultiEntry
        self.lblMME = Label(self, text=text+'\n', font=15)
        self.lblMME.grid(column=0, row=0, pady=5, padx=5, sticky=(NW))

        self.all_MME = []

        #Button MyMultiEntry
        self.btnaddMME = Button(self, text='+', fg='Red', command=self.__addMME)
        self.btnaddMME.grid(column=0, row=1, sticky=(NW))

        self.btnremMME = Button(self, text='-', fg='Dark Blue', command=self.__remMME)
        self.btnremMME.grid(column=1, row=1, sticky=(NW))
                
        #Frame Add Entry
        self.EntryMME = Frame(self)
        self.EntryMME.grid(column=0, row=2, sticky=(NW))
        
    
    #Definition des Add Entry Buttons
    def __addMME(self):
        
        self.entMME = Entry(self.EntryMME, width=50, background='white')
        self.entMME.pack(pady=5)

        self.all_MME.append(self.entMME)
        
    def __remMME(self): #(forget, destroy, remove from list)
        if len(self.all_MME)>0: #wenn elemente in all_MME vorhanden sind
            self.all_MME[-1].forget() #vergessen des graphischen Objektes (pack/grid), dass es zum frame gehört
            self.all_MME[-1].destroy() #zerstören des Objekte 
            self.all_MME.pop(-1) #letztes Element der Liste wird aus dem Speicher entfernt
        else:
            pass
        
    def get(self):
        temp = []
        for e in self.all_MME: #Element dieser Liste = Liste mit zwei Elementen ['', '']
            temp.append(e.get()) #Liste von Daten wird an Liste angehängt
        return temp
    
    def set(self, arg):
        while len(self.all_MME)>0:
            self.__remMME() #entfernt alle Entryfelder
        for index,elem in enumerate(arg): #iterieren durch die übergebenen Elemente 
            self.__addMME() #hinzufügen der Entries
            self.all_MME[index].insert(0, elem) #einfügen des str aus der Liste Position 0 von TAbk


if __name__ == "__main__":
    root = Tk()
    root.title('Test Tab')
    root.geometry('500x450')

    myentry = MyMultiEntry(root, text='test')
    myentry.pack()
    
    myentry.set( ['sadf','safd','536456','hfd'] )
    
    print(myentry.get())

    #root.mainloop()
