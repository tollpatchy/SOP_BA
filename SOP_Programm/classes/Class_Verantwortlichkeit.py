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


class Verantwortlichkeit():
    def __init__(self, tkobj):
        self.lbVer = Label(tkobj, text='Verantwortlichkeit\n', font=15, justify=LEFT)
        self.lbVer.grid(column=0, row=0, pady=5, padx=5, sticky=NW)
        self.scrVer = MyScrolledText(tkobj)
        self.scrVer.grid(column=0, row=1, pady=5, padx=5, sticky=NW)
    

if __name__ == "__main__":
    root = Tk()
    root.title('Test Tab')
    root.geometry('400x450')

    verantwortlichkeit = Verantwortlichkeit(root)

    root.mainloop()
