#!/usr/bin/env python3
from tkinter import Tk, NW, N, Frame, Label, Button, Checkbutton, BooleanVar, INSERT, scrolledtext, END
from tkinter.scrolledtext import ScrolledText


class MyScrolledText(Frame):
    def __init__(self, tkobj, *args, **kwargs):
        super().__init__(tkobj, **kwargs)
        
        #Textfeld
        self.textfeld = ScrolledText(self, relief='sunken', width=80, height=20, background='white', undo=True)
        self.textfeld.insert(INSERT,'Bitte geben Sie den Einleitungstext ein! ')
        self.textfeld.grid(column=0, row=0, pady=5, padx=5, sticky=NW)
        
        #Frame Checkbutton + Latex-Befehle
        self.boxframe = Frame(self)
        self.boxframe.grid(column=1, row=0, pady=10, padx=10, sticky=NW)
        
        #Hinzufügen eines Checkbuttons
        self.c = BooleanVar()
        self.c.set(False)
        self.latexctn = Checkbutton(self.boxframe, text='LaTeX-Befehl aktivieren', var=self.c, command=self.LaFrhide)
        self.latexctn.grid(column=0, row=0, pady=5, padx=5, sticky=NW)
        
        
        #Frame - LaTeX-Befehle aktivieren
        self.LaFr = Frame(self.boxframe)
        self.LaFr.grid(column=2, row=0, pady=10, padx=10, sticky=N)

        #Button für LaTeX-Befehle
        self.btnit = Button(self.LaFr, text='kursiv', font=('Arial', 10, 'italic'), command=self.LaTeXitalic)
        self.btnit.grid(column=0, row=0, pady=5, sticky=(NW))

        self.btnbd = Button(self.LaFr, text='fett', font=('Arial', 10, 'bold'), command=self.LaTeXbold)
        self.btnbd.grid(column=0, row=1, pady=5, sticky=(NW))

        self.btnun = Button(self.LaFr, text='unterstrichen', font=('Arial', 10, 'underline'), command=self.LaTeXundl)
        self.btnun.grid(column=0, row=2, pady=5, sticky=(NW))

        self.btntl = Button(self.LaFr, text='~', font=('Arial', 10, 'bold'), command=self.LaTeXTilde)
        self.btntl.grid(column=0, row=3, pady=5, sticky=(NW))

        self.btntg = Button(self.LaFr, text='<', font=('Arial', 10, 'bold'), command=self.LaTeXless)
        self.btntg.grid(column=1, row=3, pady=5, sticky=(NW))

        self.btntd = Button(self.LaFr, text='>', font=('Arial', 10, 'bold'), command=self.LaTeXgreater)
        self.btntd.grid(column=2, row=3, pady=5, sticky=(NW))

        self.btnLi = Button(self.LaFr, text='Aufzählung', font=('Arial', 10), command=self.LaTeXBullet)
        self.btnLi.grid(column=0, row=4, pady=5, sticky=(NW))

        self.btnim = Button(self.LaFr, text='Item', font=('Arial', 10), command=self.LaTeXItem)
        self.btnim.grid(column=1, row=4, pady=5, sticky=(NW))

        self.btnNum = Button(self.LaFr, text='Nummerierung', font=('Arial', 10), command=self.LaTeXNum)
        self.btnNum.grid(column=0, row=5, pady=5, sticky=(NW))

        #self.btnGr = Button(self.LaFr, text='Graphic', font=('Arial', 10), command=self.LaTeXGrafic)
        #self.btnGr.grid(column=0, row=6, pady=5, sticky=(NW))
        
        self.LaFr.grid_forget()
        

    def get(self):
        return self.textfeld.get(1.0, END)

    def insert(self, *args):
        self.textfeld.insert(*args)

    def delete(self, *args):
        self.textfeld.delete(*args)
    
    def getflag(self):
        return self.c.get()
        
    def setflag(self, flag):
        self.c.set(flag)
        self.LaFrhide()

    def LaFrhide(self):
        if self.c.get() == False:
            self.LaFr.grid_forget()
        else:
            self.LaFr.grid(column=0, row=1, pady=10, padx=10, sticky=(N))
            
    #------------------------------------
    def LaTeXitalic(self):
        try:
            self.focus_get().insert(INSERT, '\\textit{}')
        except:
            pass
        
    #------------------------------------
        
    def LaTeXbold(self):
        try:
            self.focus_get().insert(INSERT, '\\textbf{}')
        except:
            pass
        
    #------------------------------------

    def LaTeXundl(self):
        try:
            self.focus_get().insert(INSERT, '\\underline{}')
        except:
            pass

    #------------------------------------

    def LaTeXTilde(self):
        try:
            self.focus_get().insert(INSERT, r'$\sim$')
        except:
            pass   

    #------------------------------------
        
    def LaTeXless(self):
        try:
            self.focus_get().insert(INSERT, '\\textless{}')
        except:
            pass
        
    #------------------------------------
        
    def LaTeXgreater(self):
        try:
            self.focus_get().insert(INSERT, '\\textgreater{}')
        except:
            pass
        
    #------------------------------------

    def LaTeXBullet(self):
        try:
            self.focus_get().insert(INSERT, '\\begin{itemize}\n\\item lorem ipsum\n\\end{itemize}')
        except:
            pass
        
    #------------------------------------
    def LaTeXNum(self):
        try:
            self.focus_get().insert(INSERT, '\\begin{enumerate}\n\\item lorem ipsum\n\\end{enumerate}')
        except:
            pass
        
    #------------------------------------
    #def LaTeXGrafic(self):
        #try:
            #self.focus_get().insert(INSERT, '\\begin{figure}[h]\n\\centering\n\\includegraphics[width=4cm]{Dateiname}\n\\caption{Bildunterschrift}\n\\end{figure}')
        #except:
            #pass
        
    #------------------------------------

    def LaTeXItem(self):
        try:
            self.focus_get().insert(INSERT, '\\item ')
        except:
            pass
    #------------------------------------
        
        

if __name__ == "__main__":
    root = Tk()
    root.title('Test Tab')
    root.geometry('900x450')

    mylatex = MyScrolledText(root)
    mylatex.pack()
    
    print( mylatex.get() )
    print( mylatex.getflag() )
    mylatex.setflag(True)
    

    #root.mainloop()