#!/usr/bin/env python3
from tkinter import Tk, Frame, Radiobutton, IntVar, W


class MyRadioButton(Frame):
    def __init__(self, tkobj, *args, **kwargs):
        super().__init__(tkobj, *args, **kwargs)
        #radiobutton engl/dt

        #self.EntrySpr = ttk.Frame(tkobj)
        #self.EntrySpr.grid(column=0, row=20, sticky=N)
        #self.lblSprache = Label(self.EntrySpr, text='Sprachausgabe PDF', font=13)
        #self.lblSprache.grid(column=0, row=0, pady=5, padx=5, sticky=NW)
        self.LangVar = IntVar()
        rad1 = Radiobutton(self, text='deutsch', value=0, variable=self.LangVar)
        rad2 = Radiobutton(self, text='englisch', value=1, variable=self.LangVar)

        rad1.grid(column=1, row=0, sticky=W)
        rad2.grid(column=2, row=0, sticky=W)
        rad1.select()
        rad1.invoke() # triggered to set default language
    
    def get(self):
        return self.LangVar.get()


'''Programmstart'''

if __name__ == "__main__":
    root = Tk()
    root.title('Test Radio')
    root.geometry('200x50')
    
    
    r1 = Frame(root)
    r1.grid(column=0, row=0)
    myradiobutton = MyRadioButton(r1)
    myradiobutton.pack()
    

    #root.mainloop()