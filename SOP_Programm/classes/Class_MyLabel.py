#!/usr/bin/env python3
from tkinter import Tk, NW, W, Label, StringVar, LEFT


class MyLabel(Label):
    def __init__(self, tkobj, *args, **kwargs):
        self._txt = StringVar()
        super().__init__(tkobj, *args, textvariable=self._txt, font=13, anchor=W, **kwargs)
        
    def set(self, s):
        self._txt.set(s)   
    

if __name__ == "__main__":
    root = Tk()
    root.title('Test Entry')
    root.geometry('400x450')

    
    #txt.set('blub')
    myLabel = MyLabel(root)
    myLabel.pack()
    myLabel.set('test')

    #root.mainloop()
