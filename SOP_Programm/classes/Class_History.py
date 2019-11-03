#!/usr/bin/env python3
from tkinter import Tk, Frame, Entry, Button, NW, Label, LEFT, EW, INSERT, scrolledtext, DISABLED, END


class History():
    def __init__(self, tkobj):
        #Label - Änderungshistorie
        self.lblHist00 = Label(tkobj, text='Änderungshistorie \n', font=('Arial', 15))
        self.lblHist00.grid(column=0, row=0, pady=5, padx=5, sticky=(NW))

        self.lblHist01 = Label(
                    tkobj, text='''Sie möchten eine neue SOP erstellen?\nDann generieren Sie bitte kein Entry.
                    \nInitialversionen werden automatisch für Sie angelegt.\nVielen Dank! ''',
                    font=('Arial', 12), foreground='red', justify=LEFT, 
                    )
        self.lblHist01.grid(column=0, row=1, pady=5, padx=5, sticky=(NW))

        #Frame für Add Entry
        self.EntryHistory = Frame(tkobj)
        self.EntryHistory.grid(column=0, row=3, pady=5, padx=5, sticky=(NW))

        self.all_History = []
        self.HistCount = 0

        #Button addHistory
        self.btnaddHistory = Button(tkobj, text='+', fg='Red', command=self.__addHist)
        self.btnaddHistory.grid(column=0, row=2, pady=5, padx=5, sticky=(NW))

        self.btnremHistory = Button(tkobj, text='-', fg='Dark Blue', command=self.__remHist)
        self.btnremHistory.grid(column=1, row=2, pady=5, padx=5, sticky=(NW))
    
    
    #Definition der Add Entry Buttons
    def __addHist(self):
        
        self.frameHist = Frame(self.EntryHistory) #Erstellung eines Frames
        self.frameHist.pack()
        
        self.frameVe = Frame(self.frameHist)
        self.frameVe.grid(row=1, column=0, sticky=(NW))
        
        self.frameHiTe = Frame(self.frameHist)
        self.frameHiTe.grid(row=2, column=0, sticky=(NW))
        
        
        Label(self.frameVe, text='Version', font=12).grid(row=0, column=0, padx=5, pady=5, sticky=(EW)) #Bezeichnung des Entries
        self.entVeHist = Entry(self.frameVe, background='white', width=2)
        self.entVeHist.grid(row=0, column=1, padx=60, pady=5, sticky=(EW))
        
        Label(self.frameHiTe, text='Änderung aus\nvorheriger\nVersion', justify=LEFT , font=12).grid(column=0, row=0, padx=5, sticky=(EW)) #Bezeichnung der Textbox

        self.txtHist = scrolledtext.ScrolledText(self.frameHiTe, width=60, height=5, background='white', undo=True) #Textbox
        self.txtHist.insert(INSERT, 'Bitte geben sie Text ein! ') #Vorgegebener Text
        self.txtHist.grid(column=1, row=0, padx=7, sticky=(EW))

        self.all_History.append((self.entVeHist, self.txtHist, self.frameHist))
        
    def __remHist(self):
        if len(self.all_History)>0 and len(self.all_History)>self.HistCount: #wenn elemente in all_Hist vorhanden sind UND deren Anzahl >HistCount ist
            self.all_History[-1][2].forget() #vergessen des graphischen Objektes (pack/grid), dass es zum frame gehört
            self.all_History[-1][2].destroy() #zerstören des Objekte 
            self.all_History.pop(-1) #letztes Element der Liste wird aus dem Speicher entfernt
        else:
            pass

    def get(self):
        temp = []
        for e in self.all_History: #Element dieser Liste = Liste mit zwei Elementen ['', '']
            nlist = [e[0].get(), e[1].get(1.0, END)] #Erstellung einer Hilfslist aus den Sublisten
            temp.append(nlist) #Liste von Daten wird an Liste angehängt
        return temp
    
    def set(self, arg):
        self.HistCount = 0
        while len(self.all_History)>0:
            self.__remHist() #entfernt alle Entryfelder
        self.HistCount = len(arg)
        for index,elem in enumerate(arg): #iterieren durch die übergebenen Elemente 
            self.__addHist() #hinzufügen der Entries
            self.all_History[index][0].insert(0, elem[0]) #einfügen des str aus der Liste Position 0 von TVerf
            self.all_History[index][1].delete(1.0, END) #löschen des initialen Inhalts
            self.all_History[index][1].insert(1.0, elem[1]) #einfügen des str aus der Liste Position 1 von TVerf
            self.all_History[index][0].config(state=DISABLED)
            self.all_History[index][1].config(state=DISABLED, foreground='black', background='light grey')
            

if __name__ == "__main__":
    root = Tk()
    root.title('Test Tab')
    root.geometry('800x600')

    history = History(root)
    
    his = [['a', 'irgendwas'], ['b', 'was anderes'], ['c', 'noch mehr']]
    
    history.set(his)
    print(history.get())
    history.set([])
    
    last_hist = history.get()[-1][0]
    
    
    
    #root.mainloop()
