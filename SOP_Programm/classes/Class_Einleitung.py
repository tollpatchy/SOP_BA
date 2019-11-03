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


class Einleitung():
    def __init__(self, tkobj):
        self.lbEin = Label(tkobj, text='Einleitung\n', font=15, justify=LEFT)
        self.lbEin.grid(column=0, row=0, pady=5, padx=5, sticky=NW)
        self.scrEin = MyScrolledText(tkobj)
        self.scrEin.grid(column=0, row=1, pady=5, padx=5, sticky=NW)
    
if __name__ == "__main__":
    root = Tk()
    root.title('Test Tab')
    root.geometry('400x450')

    einleitung = Einleitung(root)

    root.mainloop()
