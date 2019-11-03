#!/usr/bin/env python3
from tkinter import Tk, NW
try:
    from classes.Class_MyMultiEntry import MyMultiEntry
except:
    pass
try:
    from Class_MyMultiEntry import MyMultiEntry
except:
    pass

class Unterlagen():
    def __init__(self, tkobj):
        #Intern
        self.intern = MyMultiEntry(tkobj, text='Intern')
        self.intern.grid(column=0, row=0, pady=5, padx=5, sticky=NW)
        #Extern
        self.extern = MyMultiEntry(tkobj, text='Extern')
        self.extern.grid(column=0, row=1, pady=5, padx=5, sticky=NW)
        #Recht
        self.recht = MyMultiEntry(tkobj, text='geltendes Recht')
        self.recht.grid(column=0, row=2, pady=5, padx=5, sticky=NW)
        
#------------------------------------
if __name__ == "__main__":
    root = Tk()
    root.title('Test Tab')
    root.geometry('550x450')

    unterlagen = Unterlagen(root)

    root.mainloop()
