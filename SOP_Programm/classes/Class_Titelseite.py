#!/usr/bin/env python3
from tkinter import Tk, Frame, NW, LEFT, INSERT
from classes.Class_MyLabel import MyLabel
from classes.Class_MySpinDate import MySpinDate
from classes.Class_MyEntryfield import MyEntryfield
from classes.Class_MyCombobox import MyCombobox
from classes.Class_MyRadiobutton import MyRadioButton


class Titelseite():
    def __init__(self, tkobj):
        #Frame: Label + Entryfeld
        TiFrame = Frame(tkobj)
        TiFrame.grid(column=0, row=0, pady=5, padx=5, sticky=NW)
        
        #Label Titel
        lblTi = MyLabel(TiFrame)
        lblTi.set('Titel')
        lblTi.grid(column=0, row=1, pady=5, padx=5, sticky=NW)
        
        #Label SOPNr.
        lblSOP = MyLabel(TiFrame)
        lblSOP.set('SOP-Nr.')
        lblSOP.grid(column=0, row=2, pady=5, padx=5, sticky=NW)
        
        #Label Institut
        lblins = MyLabel(TiFrame)
        lblins.set('Institut')
        lblins.grid(column=0, row=3, pady=5, padx=5, sticky=NW)
        
        #Label Abteilung
        lblabt = MyLabel(TiFrame)
        lblabt.set('Abteilung')
        lblabt.grid(column=0, row=4, pady=5, padx=5, sticky=NW)
        
        #Entry Titel
        self.txtTitel = MyEntryfield(TiFrame)
        self.txtTitel.grid(column=1, row=1, pady=5, padx=5, sticky=NW)
        self.txtTitel.focus()
        
        #Entry SOPNr.
        self.txtSOPNr = MyEntryfield(TiFrame, fg='red')
        self.txtSOPNr.insert(INSERT, 'XX_999')
        self.txtSOPNr.config(width=10)
        self.txtSOPNr.grid(column=1, row=2, pady=5, padx=5, sticky=NW)
        
        #Entry Institut
        self.txtInst = MyEntryfield(TiFrame)
        self.txtInst.grid(column=1, row=3, pady=5, padx=5, sticky=NW)
        
        #Entry Abteilung
        self.txtAbt =  MyEntryfield(TiFrame)
        self.txtAbt.grid(column=1, row=4, pady=5, padx=5, sticky=NW)
        
        #Frame Checkbox
        CheckFrame = Frame(tkobj)
        CheckFrame.grid(column=0, row=1, pady=5, padx=5, sticky=NW)
        
        #Label Name, Rolle, Datum
        lblName = MyLabel(CheckFrame)
        lblName.set('Name, Rolle')
        lblName.grid(column=1, row=0, pady=5, padx=5, sticky=NW)
        
        lblDatum = MyLabel(CheckFrame)
        lblDatum.set('Datum (YYYY.MM.DD)')
        lblDatum.grid(column=2, row=0, pady=5, padx=5, sticky=NW)
        
        #Label der Checkbox
        #Label - Erstellung
        lblErstellung = MyLabel(CheckFrame)
        lblErstellung.set('erstellt')
        lblErstellung.grid(column=0, row=1, pady=5, padx=5, sticky=NW)

        #Label - Prüfung
        lbl1Prüfung = MyLabel(CheckFrame)
        lbl1Prüfung.set('geprüft')
        lbl1Prüfung.grid(column=0, row=2, pady=5, padx=5, sticky=NW)

        #Label - Prüfung
        lbl2Prüfung = MyLabel(CheckFrame)
        lbl2Prüfung.set('geprüft')
        lbl2Prüfung.grid(column=0, row=3, pady=5, padx=5, sticky=NW)

        #Label - Genehmigung
        lblFreigabe = MyLabel(CheckFrame)
        lblFreigabe.set('freigegeben')
        lblFreigabe.grid(column=0, row=4, pady=5, padx=5, sticky=NW)

        #Label - Veröffentlichung
        lblRel = MyLabel(CheckFrame)
        lblRel.set('veröffentlicht')
        lblRel.grid(column=0, row=5, pady=5, padx=5, sticky=NW)
        
        
        #Combobox zum Check-Block
        self.ComNaRo = MyCombobox(CheckFrame)
        self.ComNaRo.grid(column=1, row=1, pady=5, padx=5, sticky=NW)
        self.Ch1NaRo = MyCombobox(CheckFrame)
        self.Ch1NaRo.grid(column=1, row=2, pady=5, padx=5, sticky=NW)
        self.Ch2NaRo = MyCombobox(CheckFrame)
        self.Ch2NaRo.grid(column=1, row=3, pady=5, padx=5, sticky=NW)
        self.AppNaRo = MyCombobox(CheckFrame)
        self.AppNaRo.grid(column=1, row=4, pady=5, padx=5, sticky=NW)
        self.RelNaRo = MyCombobox(CheckFrame)
        #RelNaRo.configure(state='readonly')
        self.RelNaRo.grid(column=1, row=5, pady=5, padx=5, sticky=NW)
        
        #Spinbox zum Check-Block
        self.ComSpin = MySpinDate(CheckFrame)
        self.ComSpin.grid(column=2, row=1, pady=5, padx=5, sticky=NW)
        self.Ch1Spin = MySpinDate(CheckFrame)
        self.Ch1Spin.grid(column=2, row=2, pady=5, padx=5, sticky=NW)
        self.Ch2Spin = MySpinDate(CheckFrame)
        self.Ch2Spin.grid(column=2, row=3, pady=5, padx=5, sticky=NW)
        self.AppSpin = MySpinDate(CheckFrame)
        self.AppSpin.grid(column=2, row=4, pady=5, padx=5, sticky=NW)
        self.RelSpin = MySpinDate(CheckFrame)
        self.RelSpin.grid(column=2, row=5, pady=5, padx=5, sticky=NW)
        
        #Radiobutton
        LangFrame = Frame(tkobj)
        LangFrame.grid(column=0, row=2, pady=5, padx=5, sticky=NW)
        lblSprache = MyLabel(LangFrame)
        lblSprache.set('Sprachausgabe PDF')
        lblSprache.grid(column=0, row=0, sticky=NW, pady=5, padx=5)
        self.radioSprache = MyRadioButton(LangFrame)
        self.radioSprache.grid(column=1, row=0, pady=5, padx=5, sticky=NW)
        
        

if __name__ == "__main__":
    root = Tk()
    root.title('Test Titel')
    root.geometry('400x450')

    titelseite = Titelseite(root)

    root.mainloop()
