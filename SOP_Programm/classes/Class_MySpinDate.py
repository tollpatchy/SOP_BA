#!/usr/bin/env python3
#import tkinter as tk
from tkinter import Tk, Spinbox, Frame, IntVar, N, NW
from datetime import date


class MySpinDate(Frame):
    '''
    '''
    def __init__(self, tkobj, *args, today=True, **kwargs):
        '''
        '''
        super().__init__(tkobj, **kwargs)
        #Frame der Spinbox
        #self.SpinFrame = Frame(tkobj)
        #self.SpinFrame.pack()
        
        #Variablen der Spinbox festlegen
        self.varYear = IntVar()
        self.varMonth = IntVar()
        self.varDay = IntVar()

        #Spinbox erstellen
        self.Spin_Year = Spinbox(self, from_=2000, to=2030, width=4, textvariable=self.varYear, background='white')
        self.Spin_Month = Spinbox(self, from_=1, to=12, width=2, textvariable=self.varMonth, background='white')
        self.Spin_Day = Spinbox(self, from_=1, to=31, width=2, textvariable=self.varDay, background='white')

        #Geometrie festlegen
        self.Spin_Year.grid(column=0, row=0, pady=0, sticky=(N))
        self.Spin_Month.grid(column=1, row=0, pady=0, sticky=(N))
        self.Spin_Day.grid(column=2, row=0, pady=0, sticky=(N))
        
        #Wenn today == True, dann wird das aktuelle Datum gesetzt.
        if today == True:
            self.setToday()
        else:
            pass
        
     
    def set(self, dateValue):
        '''
        Setzen des Datums
        Beispieldatum [YYYY, MM, DD]
        '''
        if len(dateValue) == 3 and type(dateValue) == type([]):
            self.varYear.set(dateValue[0])
            self.varMonth.set(dateValue[1])
            self.varDay.set(dateValue[2])
        else:
            print('Error! Falsches Format.')
            #pass
    
    def get(self):
        '''
        Holt die Werte für die Datumsvariabeln und gibt sie als Liste zurück.
        Format [YYYY, MM, DD]
        '''
        return [self.varYear.get(), self.varMonth.get(), self.varDay.get()]
    
    def setToday(self):
        '''
        Setzt das aktuelle Datum.
        '''
        #Variable: heutiges Datum
        today = date.today()

        self.varYear.set(today.year)
        self.varMonth.set(today.month)
        self.varDay.set(today.day)
        
        
        

'''Programmstart'''

if __name__ == "__main__":
    root = Tk()
    root.title('Test Date')
    root.geometry('200x150')

    #myspindate = MySpinDate(root)
    s1 = Frame(root)
    s1.grid(column=0, row=0)

    ComSpin = MySpinDate(root, today=True)
    ComSpin.grid(column=2, row=1, pady=5, padx=5, sticky=NW)
    Ch1Spin = MySpinDate(root)
    Ch1Spin.grid(column=2, row=2, pady=5, padx=5, sticky=NW)
    Ch2Spin = MySpinDate(root)
    Ch2Spin.grid(column=2, row=3, pady=5, padx=5, sticky=NW)
    AppSpin = MySpinDate(root)
    AppSpin.grid(column=2, row=4, pady=5, padx=5, sticky=NW)
    RelSpin = MySpinDate(root)
    RelSpin.grid(column=2, row=5, pady=5, padx=5, sticky=NW)
    RelSpin.set([1999, 12, 31])
    
    root.mainloop()
