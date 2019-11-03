#!/usr/bin/env python3
from tkinter import Tk, Frame, Entry, NW, END
from tkinter import ttk


class MyCombobox(Frame):
    '''
    Initialisierung einer Combobox mit Auswahlliste aus dem Datenbanksatz der Mitarbeiter (dict).
    Ermittelt aktive IDs bzw. startet beim ersten Element, wenn keine aktive ID vorhanden ist.
    Datenformat für ComboBox: list a=['user1 string', 'user2 string', ...]
    '''
    maListe = []
    
    def __init__(self, tkobj, *args, values=None, active='', **kwargs):
        '''
        '''
        super().__init__(tkobj, **kwargs)
        
        #MyCombobox selber erweitert die Klasse Frame
        
        #Erstellung der Combobox
        self.ComboMitarbeiter = ttk.Combobox(self, width = 30)
        self.ComboMitarbeiter.grid(column=0, row=0, pady=1, padx=0, sticky=(NW))
        
        #updaten der Liste
        if values != None:
            self.LoadMitarbeiter(values, active)
        else:
            pass

    
    def configure(self, state='', **kwargs):
        '''
        '''
        if state != '':
            self.ComboMitarbeiter.configure(state=state)
        else:
            pass
        super().configure(**kwargs)
    
    
    def config(self, **kwargs):
        self.configure(**kwargs)
    
        
    def LoadMitarbeiter(self, values=None, active=None):
        '''
        Laden der Mitarbeiterliste in das Auswahlfeld der Combobox. 
        '''
        if values == None: #None als default value, um ein "dangerous default value" zu vermeiden.
            values = ['']
        elif type(values) != type([]):
            print('Error: falsches Format')
        else:
            pass
    
        self.Mitarbeiter = values
        #_users = list(self.Mitarbeiter.keys()) #Liste der Mitarbeiternamen (keys)
        
        self.ComboMitarbeiter['values'] = values #Inhalt der Liste _users wird ins Auswahlfeld der Combobox geladen.
        
        if active == None:
            self.ComboMitarbeiter.current(0) #Liste startet beim ersten Listenelement
        else:
            #self.ComboMitarbeiter.current( num )
            self.ComboMitarbeiter.delete(0, END)
            self.ComboMitarbeiter.insert(0, active)

        
    def get(self):
        '''
        Liefert UID des aktiv angezeigten Mitarbeiters zurück
        '''
        #return self.Mitarbeiter[self.ComboMitarbeiter.get()][0]
        #print(self.ComboMitarbeiter.current(),':', self.ComboMitarbeiter.get())
        return self.ComboMitarbeiter.get()
    
    
    def set(self, name):
        self.ComboMitarbeiter.set(name)
    



'''Programmstart'''

if __name__ == "__main__":
    root = Tk()
    root.title('Test Name')
    root.geometry('600x450')
     
    
    allUserDict = {'Tick' : (1234, 'Neffe, blau'),
                    'Trick' : (5678, 'Neffe, rot'),
                    'Track' : (9012, 'Neffe, grün'),
                    'Donald Duck' : (5432, 'Pechvogel'),
                    'Mac Moneysac' : (2000, 'Antagonist und Kapitalist'),
                    'Dagobert Duck' : (1000, 'Abenteurer und Kapitalist')
                    }
    alluserList = ['Tick Duck (Neffe, blau)', 'Trick Duck (Neffe, rot)', 'Track (Neffe, grün)', 'Donald Duck (Pechvogel)',
                   'Mac Moneysac (Antagonist und Kapitalist)', 'Dagobert Duck (Abenteurer und Kapitalist)']
    
    f1=Frame(root)
    f1.grid(column=0, row=0)
    mycombobox1 = MyCombobox(f1)
    mycombobox1.pack()
    mycombobox2 = MyCombobox(f1, values=alluserList)
    mycombobox2.pack()
    mycombobox3 = MyCombobox(f1, values=alluserList, active='Trick')
    mycombobox3.pack()
    mycombobox4 = MyCombobox(f1, values=alluserList, active='Trick')
    mycombobox4.pack()
    mycombobox4.configure(state='readonly')
    
    #root.mainloop()
