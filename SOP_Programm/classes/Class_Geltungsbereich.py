#!/usr/bin/env python3
from tkinter import Tk, NW, LEFT, Label
try:
    from classes.Class_MyScrolledText import MyScrolledText
except:
    pass
try:
    from Class_MyScrolledText import MyScrolledText
except:
    pass


class Geltungsbereich():
    def __init__(self, tkobj):
        self.lbGel = Label(tkobj, text='Geltungsbereich\n', font=15, justify=LEFT)
        self.lbGel.grid(column=0, row=0, pady=5, padx=5, sticky=NW)
        self.scrGel = MyScrolledText(tkobj)
        self.scrGel.grid(column=0, row=1, pady=5, padx=5, sticky=NW)
    

if __name__ == "__main__":
    root = Tk()
    root.title('Test Tab')
    root.geometry('400x450')

    geltungsbereich = Geltungsbereich(root)

    root.mainloop()
