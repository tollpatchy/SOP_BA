#!/usr/bin/env python3
from tkinter import Tk,NW
try:
    from classes.Class_MyMultiEntry import MyMultiEntry
except:
    pass
try:
    from Class_MyMultiEntry import MyMultiEntry
except:
    pass

class Anhang():
    def __init__(self, tkobj):
        self.anhang = MyMultiEntry(tkobj, text='Anhang')
        self.anhang.grid(column=0, row=0, pady=5, padx=5, sticky=NW)
        

if __name__ == "__main__":
    root = Tk()
    root.title('Test Tab')
    root.geometry('500x450')

    anhang = Anhang(root)

    root.mainloop()
