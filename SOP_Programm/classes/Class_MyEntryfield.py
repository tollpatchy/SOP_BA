#!/usr/bin/env python3
from tkinter import Tk, NW, Entry


class MyEntryfield(Entry):
    def __init__(self, tkobj, *args, **kwargs):
        super().__init__(tkobj, *args, width=50, background = 'white', **kwargs)
        
    
if __name__ == "__main__":
    root = Tk()
    root.title('Test Entry')
    root.geometry('400x450')

    myEntryfield = MyEntryfield(root)

    root.mainloop()
