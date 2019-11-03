'''
http://effbot.org/tkinterbook/tkinter-dialog-windows.htm
https://stackoverflow.com/questions/10057672/correct-way-to-implement-a-custom-popup-tkinter-dialog-box
'''
from tkinter import Tk, Toplevel, Frame, Button, LEFT, ACTIVE, RIGHT, X


class Dialog(Toplevel):

    def __init__(self, parent, title = None):

        Toplevel.__init__(self, parent)
        self.transient(parent) #set to be on top of the main window

        if title:
            self.title(title)
            
        self.parent = parent

        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(fill=X, padx=5, pady=5)

        self.buttonbox()

        self.grab_set() #hijack all commands from the master (clicks on the main window are ignored)

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        parent.update()
        x = parent.winfo_rootx() + parent.winfo_width()/2 - self.winfo_width()/2
        y = parent.winfo_rooty() + parent.winfo_height()/2 - self.winfo_height()/2
        self.geometry("+%d+%d" % (x,y))
        #self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
        #                          parent.winfo_rooty()+50))

        self.initial_focus.focus_set()

        self.wait_window(self) #pause anything on the main window until this one closes

    #
    # construction hooks

    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden

        pass

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    #
    # standard button semantics

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def cancel(self, event=None):

        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks

    def validate(self):

        return 1 # override

    def apply(self):

        pass # override





if __name__ == "__main__":

    from tkinter import Label, Entry

    class MyDialog(Dialog):

        def body(self, master):

            Label(master, text="First:").grid(row=0)
            Label(master, text="Second:").grid(row=1)

            self.e1 = Entry(master)
            self.e2 = Entry(master)

            self.e1.grid(row=0, column=1)
            self.e2.grid(row=1, column=1)
            #return self.e1 # initial focus
            return

        def apply(self):
            first = int(self.e1.get())
            second = int(self.e2.get())
            self.result = first, second



    def cmd():
        pass

    root = Tk()
    root.title('Listbox')
    root.geometry('300x300+300+300')
    root.update()
    
    #okbtn = Button(root, text='OK', command=None)
    print(str(root.winfo_rootx())+':'+str(root.winfo_rooty()))
    
    d = MyDialog(root)
    print(d.result)
    
    #root.mainloop()
