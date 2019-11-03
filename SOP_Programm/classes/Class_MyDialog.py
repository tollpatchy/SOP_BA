#!/usr/bin/env python3
from tkinter import Tk, Listbox, SINGLE, Button, END, BOTH, LEFT, RIGHT, \
                    X, Y, Checkbutton, BooleanVar, NW, Frame, Label, Entry, DISABLED, NORMAL
try:
    from classes.Class_tkSimpleDialog import Dialog
except:
    pass
try:
    from Class_tkSimpleDialog import Dialog
except:
    pass



class MyListbox(Dialog):
    
    def __init__(self, master, soplst):
        self.sopListe = soplst
        super().__init__(master, title='SOP Liste')

    def body(self, master):
        self.lbox = Listbox(master, background='white', selectmode=SINGLE)
        self.lbox.pack(fill=BOTH, expand=5)
        
        for item in self.sopListe:
            self.lbox.insert(END, item)
        
        self.lbox.selection_set(0)
        return self.lbox # initial focus
        #return # no initial focus

    def apply(self):
        self.result = int( self.lbox.curselection()[0] ) # Position des ausgewählten Elements



#--------------------------------------------------------------------

class MyLogin(Dialog):
    
    def __init__(self, master, server=['',0]):
        self.server = server
        super().__init__(master, title='Login Datenbank')
     

    def login(self):
        '''
        Wenn Datenbank == True, dann erscheint die Login-Option.
        '''
        if self.a.get() == True:
            self.dbnCbtn.config(state=DISABLED)
            self.EntryFrame.grid(column=0, row=5, pady=5, padx=5, sticky=NW)
            
        else:
            self.dbnCbtn.config(state=NORMAL)
            self.EntryFrame.grid_forget()


    def nologin(self):
        '''
        Wenn option Datei gewählt ist
        '''
        if self.b.get() == True:
            self.dbjCbtn.config(state=DISABLED)
        else:
            self.dbjCbtn.config(state=NORMAL)


    def body(self, master):
        '''
        Auswahloption
        '''
        self.GFrame = Frame(master)
        self.GFrame.pack()
        #self.GFrame.grid(column=0, row=0, pady=5, padx=5, sticky=NW)

        self.cbtnLabel = Label(self.GFrame, text='Möchten Sie sich mit der Datenbank verbinden?', font=13)
        self.cbtnLabel.grid(column=0, row=0, pady=5, padx=5, sticky=(NW))

        self.a = BooleanVar()
        self.a.set(False)
        self.dbjCbtn = Checkbutton(self.GFrame, text='Ja, weiter zum Login.', var=self.a, command=self.login)
        self.dbjCbtn.grid(column=0, row=1, pady=5, padx=5, sticky=NW)
        self.dbjCbtn.config(state=DISABLED)

        self.b = BooleanVar()
        self.b.set(True)
        self.dbnCbtn = Checkbutton(self.GFrame, text='Nein, SOPs lokal verwalten.', var=self.b, command=self.nologin)
        self.dbnCbtn.grid(column=0, row=2, pady=5, padx=5, sticky=NW)
        
        '''
        Login-Option erscheint, wenn Checkbox "Ja" ausgewählt ist.
        '''
        self.EntryFrame = Frame(self.GFrame) 
        self.EntryFrame.grid(column=0, row=5, pady=5, padx=5, sticky=NW)
                        
        self.userLabel = Label(self.EntryFrame, text='Benutzername', font=13)
        self.userLabel.grid(column=0, row=9, pady=5, padx=5, sticky=(NW))

        self.userEntry = Entry(self.EntryFrame, width=15, background='white') #Entry Feld
        self.userEntry.grid(column=1, row=9, pady=5, padx=5, sticky=(NW))
                        
        self.pwLabel = Label(self.EntryFrame, text='Passwort', font=13)
        self.pwLabel.grid(column=0, row=10, pady=5, padx=5, sticky=(NW))

        self.pwEntry = Entry(self.EntryFrame, width=15, background='white') #Entry Feld
        self.pwEntry.grid(column=1, row=10, pady=5, padx=5, sticky=(NW))

        self.hostLabel = Label(self.EntryFrame, text='Host', font=13)
        self.hostLabel.grid(column=0, row=11, pady=5, padx=5, sticky=(NW))

        self.hostEntry = Entry(self.EntryFrame, width=15, background='white') #Entry Feld
        self.hostEntry.insert(0, self.server[0])
        self.hostEntry.grid(column=1, row=11, pady=5, padx=5, sticky=(NW))

        self.portLabel = Label(self.EntryFrame, text='Port', font=13)
        self.portLabel.grid(column=0, row=12, pady=5, padx=5, sticky=(NW))

        self.portEntry = Entry(self.EntryFrame, width=15, background='white', text=self.server[1]) #Entry Feld
        self.portEntry.insert(0, self.server[1])
        self.portEntry.grid(column=1, row=12, pady=5, padx=5, sticky=(NW))
        
        self.EntryFrame.grid_forget()
        

    def apply(self):
        if self.a.get() == True:      
            cred = [ self.userEntry.get(), self.pwEntry.get(), \
                     self.hostEntry.get(), int(self.portEntry.get()) ] 
        else:
            cred = None
        self.result = cred


                
#--------------------------------------------------------------------
        
if __name__ == "__main__":
    
    def dialog():
        mylistbox = MyListbox(root, ['ab', 'cd', 'ef', 'gh'])
        print( mylistbox.result )
        a=mylistbox.result
    
    def login():
        mylogin = MyLogin(root, server=['abc.fritz.box',27017])
        print( mylogin.result )
        
    root = Tk()
    root.title('Listbox')
    root.geometry('300x300+300+300')
    
    Dlg = Button(root, text='Dave', font=13, command=dialog)
    Dlg.pack()
    Hlg = Button(root, text='Hal', font=13, command=login)
    Hlg.pack()
    

    #root.mainloop()
    