#!/usr/bin/env python3
from tkinter import Tk, messagebox, Menu, Entry, NW
import os


class MyMenu():
    def __init__(self, tkObj, newcmd=None, opencmd=None, savecmd=None, exportcmd=None, logincmd=None):
        #Popupmenü Cut, Copy, Paste - gebunden an den rechten Mausbutton (press and release)
        tkObj.bind('<Button-3><ButtonRelease-3>', self._show_popup)
        self._make_popup_menu(tkObj)
        
        self.menubar = Menu(tkObj)

        # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Neu', command=newcmd)
        self.filemenu.add_command(label='Öffnen', command=opencmd)
        self.filemenu.add_command(label='Speichern', command=savecmd)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='PDF-Export', command=exportcmd, background='dark red', foreground='white')
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', background='black', foreground='white', command=tkObj.destroy)
        self.menubar.add_cascade(label='Datei', menu=self.filemenu)

        self.editmenu = Menu(self.menubar, tearoff=0)
        #lambda definiert anonyme Funktionen
        #tkObj.focus_get() holt das Objekt, das den aktuellen Fokus hat.
        #In diesem Fokus wird der entsprechende event generiert.
        self.editmenu.add_command(label='Ausschneiden', accelerator="Ctrl+X", command=lambda: tkObj.focus_get().event_generate('<<Cut>>'))
        self.editmenu.add_command(label='Kopieren', accelerator="Ctrl+C", command=lambda: tkObj.focus_get().event_generate('<<Copy>>'))
        self.editmenu.add_command(label='Einfügen', accelerator="Ctrl+V", command=lambda: tkObj.focus_get().event_generate('<<Paste>>'))
        self.menubar.add_cascade(label='Bearbeiten', menu=self.editmenu)
        
        #self.loginmenu = Menu(self.menubar, tearoff=0)
        #self.loginmenu.add_command(label='Login Datenbank', command=logincmd)
        #self.menubar.add_cascade(label='Login', menu=self.loginmenu)
        
        
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label='Readme', command=self._readme)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label='Über SOPGUI', command=self._about)
        self.menubar.add_cascade(label='Hilfe', menu=self.helpmenu)

        tkObj.config(menu=self.menubar)

    #------------------------------------
    def _make_popup_menu(self, tkobj):
        #global popup_menu
        self.popup_menu = Menu(tkobj, tearoff=0)
        self.popup_menu.add_command(label='Cut')
        self.popup_menu.add_command(label='Copy')
        self.popup_menu.add_command(label='Paste')

    def _show_popup(self, e): #e ist der event, der zurückgerufen wird, wenn der callback aufgerufen wird.
        w = e.widget #Abfrage des Objekts
        self.popup_menu.entryconfigure('Cut', command=lambda: w.event_generate('<<Cut>>'))
        self.popup_menu.entryconfigure('Copy', command=lambda: w.event_generate('<<Copy>>'))
        self.popup_menu.entryconfigure('Paste', command=lambda: w.event_generate('<<Paste>>'))
        self.popup_menu.tk.call('tk_popup', self.popup_menu, e.x_root, e.y_root) #ruft an der Mauszeigerposition das popup_menu auf


    #------------------------------------
    def _readme(self):
        rm = messagebox.askokcancel('Bekanntmachung! ', 'Möchten Sie das Readme lesen?\nDie Datei öffnet sich im Webbrowser.')
        if rm == True:
            htmlfile = 'README.html'
            if os.name == 'nt': #windows
                os.startfile(htmlfile)
            elif os.name == 'posix': #unix/linux
                os.system('/usr/bin/xdg-open '+ htmlfile)
        else:
            pass
    #------------------------------------
    def _about(self):
        about = 'Entwickelt unter:\n\nLinux (64-bit)\nPython (Version 3.6.7)\nThonny (Version 3.1.2)\nTk (8.6.8)'
        messagebox.showinfo('Über SOPGUI ', message=about)
    #------------------------------------
        


if __name__ == "__main__":
    root = Tk()
    root.title('Test Menü')
    root.geometry('400x450')

    mymenu = MyMenu(root)

    textfeld = Entry(root, width = 50, background = 'white')
    textfeld.grid(column=0, row=1, sticky=(NW))

    root.mainloop()
