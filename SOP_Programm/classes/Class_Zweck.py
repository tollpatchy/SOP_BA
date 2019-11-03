#!/usr/bin/env python3
from tkinter import Tk, INSERT, NW, Label, LEFT
try:
    from classes.Class_MyScrolledText import MyScrolledText
except:
    pass
try:
    from Class_MyScrolledText import MyScrolledText
except:
    pass


class Zweck():
    def __init__(self, tkobj):
           self.lbzweck = Label(tkobj, text='Zweck\n', font=15, justify=LEFT)
           self.lbzweck.grid(column=0, row=0, pady=5, padx=5, sticky=NW)
           self.scrzweck = MyScrolledText(tkobj)
           self.scrzweck.grid(column=0, row=1, pady=5, padx=5, sticky=NW)

if __name__ == "__main__":
    root = Tk()
    root.title('Test Tab')
    root.geometry('600x450')

    zweck = Zweck(root)

    root.mainloop()
