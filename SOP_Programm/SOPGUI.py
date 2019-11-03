#!/usr/bin/env python3
from tkinter import Tk, Frame, messagebox, ttk, END, NORMAL, DISABLED
from datetime import date
import json
from subprocess import Popen, PIPE
import os
from classes.Class_MyMenu import MyMenu
from classes.Class_Titelseite import Titelseite
from classes.Class_Einleitung import Einleitung
from classes.Class_Zweck import Zweck
from classes.Class_Geltungsbereich import Geltungsbereich
from classes.Class_Verantwortlichkeit import Verantwortlichkeit
from classes.Class_AbkDef import AbkDef
from classes.Class_Verfahren import Verfahren
from classes.Class_History import History
from classes.Class_Unterlagen import Unterlagen
from classes.Class_Anhang import Anhang
from classes.Class_DataMongo import DataMongo
from classes.Class_DataFile import DataFile
from classes.Class_tkSimpleDialog import Dialog
from classes.Class_MyDialog import MyListbox, MyLogin



## Globale Variablen
dbHost=''
dbPort=0
dbauthSource=''
templFiles=[]


class MainApplication():
    '''
    '''
    sopData = {}
    
    def __init__(self, tkobj):
        
        mymenu = MyMenu(tkobj, newcmd=self.newSOP, opencmd=self.opendata, exportcmd=self.sopToPDF, savecmd=self.saveSOP)
        
        self.tab_control = ttk.Notebook(tkobj)
        self.tabTitelseite = ttk.Frame(self.tab_control)
        self.tabEinleitung = ttk.Frame(self.tab_control)
        self.tabZweck = ttk.Frame(self.tab_control)
        self.tabGeltungsbereich = ttk.Frame(self.tab_control)
        self.tabVerantwortlichkeit = ttk.Frame(self.tab_control)
        self.tabAbkDef = ttk.Frame(self.tab_control)
        self.tabVerfahren = ttk.Frame(self.tab_control)
        self.tabHistory = ttk.Frame(self.tab_control)
        self.tabUnterlagen = ttk.Frame(self.tab_control)
        self.tabAnhang = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tabTitelseite, text='Titelseite')
        self.tab_control.add(self.tabEinleitung, text='Einleitung')
        self.tab_control.add(self.tabZweck, text='Zweck')
        self.tab_control.add(self.tabGeltungsbereich, text='Geltungsbereich')
        self.tab_control.add(self.tabVerantwortlichkeit, text='Verantwortlichkeit')
        self.tab_control.add(self.tabAbkDef, text='Abkürzungen und Definitionen')
        self.tab_control.add(self.tabVerfahren, text='Verfahren')
        self.tab_control.add(self.tabHistory, text='Änderungshistorie')
        self.tab_control.add(self.tabUnterlagen, text='mitgeltende Unterlagen')
        self.tab_control.add(self.tabAnhang, text='Anhang')
        self.tab_control.pack(expand=1, fill='both')
        
        self.titelseite = Titelseite(self.tabTitelseite)
        self.einleitung = Einleitung(self.tabEinleitung)
        self.zweck = Zweck(self.tabZweck)
        self.geltungsbereich = Geltungsbereich(self.tabGeltungsbereich)
        self.verantwortlichkeit = Verantwortlichkeit(self.tabVerantwortlichkeit)
        self.abkdef = AbkDef(self.tabAbkDef)
        self.verfahren = Verfahren(self.tabVerfahren)
        self.history = History(self.tabHistory)
        self.unterlagen = Unterlagen(self.tabUnterlagen)
        self.anhang = Anhang(self.tabAnhang)
        

        #<create the rest of your GUI here>
        
        ## popup für login oder file-basiert
        loginDone = False
        while not loginDone:
            LoginDlg = MyLogin(root, server=[dbHost,dbPort])
            if LoginDlg.result == None:
                self.sopDB = DataFile()
                loginDone = True
            else:
                self.sopDB = DataMongo(host=LoginDlg.result[2], dport=LoginDlg.result[3], dauthSource=dbauthSource, serverSelectionTimeoutMS=5000)
                if self.sopDB.login(dbuser=LoginDlg.result[0], dbpw=LoginDlg.result[1]) == True:
                    loginDone = True
                    root.title('Test SOP' + ' connected: ' + LoginDlg.result[0] + '@' + LoginDlg.result[2])
                else:
                    messagebox.showerror('Error', self.sopDB.result)
                    pass
        
        #self.sopDB = DataMongo(host=dbHost, dport=dbPort, dauthSource=dbauthSource)
        #self.sopDB.login(dbuser=self.__dbuser, dbpw=self.__dbpw)
        self.__load_user( self.sopDB.getUsers() )
        
    
    def __load_user(self, allUserList):
        '''
        '''
        self.titelseite.ComNaRo.LoadMitarbeiter(values=allUserList, active='')
        self.titelseite.Ch1NaRo.LoadMitarbeiter(values=allUserList, active='')
        self.titelseite.Ch2NaRo.LoadMitarbeiter(values=allUserList, active='')
        self.titelseite.AppNaRo.LoadMitarbeiter(values=allUserList, active='')
        self.titelseite.RelNaRo.LoadMitarbeiter(values=allUserList, active='')


    #------------------------------------
    def opendata(self):
        '''
        'Öffnen' callback Funktion, wird an myMenu übergeben.
        '''
        # von Datenbank Klasse Liste aller SOP mit Titel holen
        tempL = self.sopDB.getSOPlist()
        # SOP Liste in ListBox anzeigen
        listbox = MyListbox(root, [e[0]+' '+e[1] for e in tempL ] ) # macht aus [['','']] -> ['']
        # Auswahl aus ListBox empfangen nutzen um passende SOP aus Datenbank zu laden
        if listbox.result != None:
            selectedSOP = tempL[listbox.result][0]  # SOP Name an Stelle 0 in tempL
            self.sopData = self.sopDB.loadSOP(selectedSOP)
            # Datensatz aus der geladenen SOP in GUI eintragen
            self.setSOPdata()
        else:
            pass
        
    #------------------------------------
    
    def newSOP(self):
        '''
        Löscht alle eingetragenen Felder
        '''
        self.sopData.clear()
        self.setSOPdata()
        #pass
    #------------------------------------
    
    def saveSOP(self):
        '''
        'Speichern' callback Funktion, wird von MyMenu aufgerufen.
        '''
        # Daten aus tkObjekten holen
        self.getSOPdata()
        # prüfen, ob SOP Nr bereits vorhanden
        if '_id' in self.sopData.keys():
            ret = self.sopDB.writeSOP(self.sopData) # Daten an Datenbank übergeben
        else:
            if self.sopDB.SOPexists(self.sopData['txtSOPNr']):
                messagebox.showwarning('Der Papagei ist tot!','Eine SOP mit dieser Nummer ist bereits vorhanden!')
                return
            else:
                ret = self.sopDB.writeSOP(self.sopData) # Daten an Datenbank übergeben
                pass
        if not ret==None:
            messagebox.showinfo('Bekanntmachung!','Ihre SOP wurde gespeichert.')
        else:
            messagebox.showwarning('Bekanntmachung!','Es ist ein Problem beim Schreiben aufgetreten\nFehlercode: spamspamspam')
    #------------------------------------
    
    def setSOPdata(self):
        '''
        Gespeicherte SOP-Daten werden in die Eingabemaske geladen.
        '''
        self.titelseite.txtTitel.delete(0, END) #vorhandene Eingabe wird gelöscht        
        if 'txtTitel' in self.sopData.keys(): #ist ein entry vorhanden,
            self.titelseite.txtTitel.insert(0, self.sopData['txtTitel']) #wird es eingefügt
        else:
            pass
        
        self.titelseite.txtSOPNr.delete(0, END)
        if 'txtSOPNr' in self.sopData.keys(): 
            self.titelseite.txtSOPNr.config(state=NORMAL)
            self.titelseite.txtSOPNr.insert(0, self.sopData['txtSOPNr']) #Entry aus vorhandener *.sop wird geladen
            self.titelseite.txtSOPNr.config(state=DISABLED) #SOPNr. kann nicht mehr geändert werden
        else:
            self.titelseite.txtSOPNr.config(state=NORMAL) #bei Neuerstellung wird das Feld wieder freigegeben
            self.titelseite.txtSOPNr.delete(0, END) #vorhandenes Entry wird gelöscht.
        
        self.titelseite.txtInst.delete(0, END)
        if 'txtInst' in self.sopData.keys():
            self.titelseite.txtInst.insert(0, self.sopData['txtInst'])
        else:
            pass
        
        self.titelseite.txtAbt.delete(0, END)
        if 'txtAbt' in self.sopData.keys():
            self.titelseite.txtAbt.insert(0, self.sopData['txtAbt'])
        else:
            pass
                
        if 'CName' in self.sopData.keys():
            self.titelseite.ComNaRo.set(self.sopData['CName'])
        else:
            self.titelseite.ComNaRo.set('')

        if 'Ch1Name' in self.sopData.keys():
            self.titelseite.Ch1NaRo.set(self.sopData['Ch1Name'])
        else:
            self.titelseite.Ch1NaRo.set('')
            
        if 'Ch2Name' in self.sopData.keys():
            self.titelseite.Ch2NaRo.set(self.sopData['Ch2Name'])
        else:
            self.titelseite.Ch2NaRo.set('')
            
        if 'AppName' in self.sopData.keys():
            self.titelseite.AppNaRo.set(self.sopData['AppName'])
        else:
            self.titelseite.AppNaRo.set('')
            
        if 'RName' in self.sopData.keys():
            self.titelseite.RelNaRo.set(self.sopData['RName'])
        else:
            self.titelseite.RelNaRo.set('')

        if self.sopData.keys() >= {'CYear', 'CMonth', 'CDay'}:  # übprüft mit set() Operation ob Set im Superset (s.issuperset(t))
            self.titelseite.ComSpin.set( [self.sopData['CYear'], self.sopData['CMonth'], self.sopData['CDay']] )
        else:
            self.titelseite.ComSpin.setToday()
            
        if self.sopData.keys() >= {'Ch1Year', 'Ch1Month', 'Ch1Day'}:
            self.titelseite.Ch1Spin.set( [self.sopData['Ch1Year'], self.sopData['Ch1Month'], self.sopData['Ch1Day']] )
        else:
            self.titelseite.Ch1Spin.setToday()
            
        if self.sopData.keys() >= {'Ch2Year', 'Ch2Month', 'Ch2Day'}:
            self.titelseite.Ch2Spin.set( [self.sopData['Ch2Year'], self.sopData['Ch2Month'], self.sopData['Ch2Day']] )
        else:
            self.titelseite.Ch2Spin.setToday()
        
        if self.sopData.keys() >= {'AppYear', 'AppMonth', 'AppDay'}:
            self.titelseite.AppSpin.set( [self.sopData['AppYear'], self.sopData['AppMonth'], self.sopData['AppDay']] )
        else:
            self.titelseite.AppSpin.setToday()
            
        if self.sopData.keys() >= {'RYear', 'RMonth', 'RDay'}:
            self.titelseite.RelSpin.set( [self.sopData['RYear'], self.sopData['RMonth'], self.sopData['RDay']] )
        else:
            self.titelseite.RelSpin.setToday()
            
        self.einleitung.scrEin.delete(1.0, END)
        if 'TEinleitung' in self.sopData.keys():
            self.einleitung.scrEin.insert(1.0, self.sopData['TEinleitung'])
        else:
            self.einleitung.scrEin.insert(1.0, 'N/A')
        
        self.zweck.scrzweck.delete(1.0, END)
        if 'TZweck' in self.sopData.keys():
            self.zweck.scrzweck.insert(1.0, self.sopData['TZweck'])
        else:
            self.zweck.scrzweck.insert(1.0, 'N/A')
        
        self.geltungsbereich.scrGel.delete(1.0, END)
        if 'TGeltungsbereich' in self.sopData.keys():
            self.geltungsbereich.scrGel.insert(1.0, self.sopData['TGeltungsbereich'])
        else:
            self.geltungsbereich.scrGel.insert(1.0, 'N/A')
        
        self.verantwortlichkeit.scrVer.delete(1.0, END)    
        if 'TVerantwortlichkeiten' in self.sopData.keys():
            self.verantwortlichkeit.scrVer.insert(1.0, self.sopData['TVerantwortlichkeiten'])
        else:
            self.verantwortlichkeit.scrVer.insert(1.0, 'N/A')
        
        if 'LaEinl' in self.sopData.keys():
            self.einleitung.scrEin.setflag(self.sopData['LaEinl'])
        else:
            self.einleitung.scrEin.setflag(False)
        
        if 'LaZw' in self.sopData.keys():
            self.zweck.scrzweck.setflag(self.sopData['LaZw'])
        else:
            self.zweck.scrzweck.setflag(False)
        
        if 'LaGe' in self.sopData.keys():
            self.geltungsbereich.scrGel.setflag(self.sopData['LaGe'])
        else:
            self.geltungsbereich.scrGel.setflag(False)
        
        if 'LaVe' in self.sopData.keys():
            self.verantwortlichkeit.scrVer.setflag(self.sopData['LaVe'])
        else:
            self.verantwortlichkeit.scrVer.setflag(False)
               
        if 'TAbk' in self.sopData.keys():
            self.abkdef.setAbk(self.sopData['TAbk'])
        else:
            self.abkdef.setAbk([])
             
        if 'TDef' in self.sopData.keys():
            self.abkdef.setDef(self.sopData['TDef'])
        else:
            self.abkdef.setDef([])
        
        if 'TVerfahren' in self.sopData.keys():
            self.verfahren.set(self.sopData['TVerfahren'])
        else:
            self.verfahren.set([])
        
        if 'THistory' in self.sopData.keys():
            self.history.set(self.sopData['THistory'])
        else:
            self.history.set([])
        
        if 'TIntern' in self.sopData.keys():
            self.unterlagen.intern.set(self.sopData['TIntern'])
        else:
            self.unterlagen.intern.set([])
        
        if 'TExtern' in self.sopData.keys():
            self.unterlagen.extern.set(self.sopData['TExtern'])
        else:
            self.unterlagen.extern.set([])
            
        if 'TLgl' in self.sopData.keys():
            self.unterlagen.recht.set(self.sopData['TLgl'])
        else:
            self.unterlagen.recht.set([])
            
        if 'TAnhang' in self.sopData.keys():
            self.anhang.anhang.set(self.sopData['TAnhang'])
        else:
            self.anhang.anhang.set([])
        
        
    #------------------------------------
            
    def getSOPdata(self):
        '''
        Speichert SOP-Daten aus den tkObjekten in die Datenbank.
        '''
        self.sopData['txtTitel'] = self.titelseite.txtTitel.get()
        self.sopData['txtSOPNr'] = self.titelseite.txtSOPNr.get()
        self.sopData['txtInst'] = self.titelseite.txtInst.get()
        self.sopData['txtAbt'] = self.titelseite.txtAbt.get()
        self.sopData['CName'] = self.titelseite.ComNaRo.get()
        self.sopData['Ch1Name'] = self.titelseite.Ch1NaRo.get()
        self.sopData['Ch2Name'] = self.titelseite.Ch2NaRo.get()
        self.sopData['AppName'] = self.titelseite.AppNaRo.get()
        self.sopData['RName'] = self.titelseite.RelNaRo.get()
        temp = self.titelseite.ComSpin.get()
        self.sopData['CYear'] = temp[0]
        self.sopData['CMonth'] = temp[1]
        self.sopData['CDay'] = temp[2]
        temp = self.titelseite.Ch1Spin.get()
        self.sopData['Ch1Year'] = temp[0]
        self.sopData['Ch1Month'] = temp[1]
        self.sopData['Ch1Day'] = temp[2]
        temp = self.titelseite.Ch2Spin.get()
        self.sopData['Ch2Year'] = temp[0]
        self.sopData['Ch2Month'] = temp[1]
        self.sopData['Ch2Day'] = temp[2]
        temp = self.titelseite.AppSpin.get()
        self.sopData['AppYear'] = temp[0]
        self.sopData['AppMonth'] = temp[1]
        self.sopData['AppDay'] = temp[2]
        temp = self.titelseite.RelSpin.get()
        self.sopData['RYear'] = temp[0]
        self.sopData['RMonth'] = temp[1]
        self.sopData['RDay'] = temp[2]
        self.sopData['TEinleitung'] = self.einleitung.scrEin.get()
        self.sopData['LaEinl'] = self.einleitung.scrEin.getflag()
        self.sopData['TZweck'] = self.zweck.scrzweck.get()
        self.sopData['LaZw'] = self.zweck.scrzweck.getflag()
        self.sopData['TGeltungsbereich'] = self.geltungsbereich.scrGel.get()
        self.sopData['LaGe'] = self.geltungsbereich.scrGel.getflag()
        self.sopData['TVerantwortlichkeit'] = self.verantwortlichkeit.scrVer.get()
        self.sopData['LaVe'] = self.verantwortlichkeit.scrVer.getflag()
        self.sopData['TAbk'] = self.abkdef.getAbk()
        self.sopData['TDef'] = self.abkdef.getDef()
        self.sopData['TVerfahren'] = self.verfahren.get()
        self.sopData['THistory'] = self.history.get()
        if len(self.sopData['THistory']) > 0:
            self.sopData['txtVersion'] = self.history.get()[-1][0]
        else:
            self.sopData['txtVersion'] = '00'
        self.sopData['TIntern'] = self.unterlagen.intern.get()
        self.sopData['TExtern'] = self.unterlagen.extern.get()
        self.sopData['TLgl'] = self.unterlagen.recht.get()
        self.sopData['TAnhang'] = self.anhang.anhang.get()
        
    #------------------------------------
        
    def sopToPDF(self):
        self.getSOPdata() #holen der Daten
        OUTPATH = 'output/'
        helperfiles = ['tex', 'toc', 'log', 'aux']
        if self.titelseite.radioSprache.get() == 0:
            OUTFILE = self.sopData['txtSOPNr'] + 'de' + '.tex' #Dateiname (Sprachausgabe des Formulars in deutsch)
        else:
            OUTFILE = self.sopData['txtSOPNr'] + 'en' + '.tex' #Dateiname(Sprachausgabe des Formulars in englisch)
        
        #Ausgabe als pdf. Doppeltes Aufrufen nötig, damit Element wie Inhaltsverzeichnis oder LastPage aktuallisiert werden.
        cmds = [['ls','-a'], ['pdflatex', OUTFILE], ['pdflatex', OUTFILE]]
        for e in helperfiles:
            cmds.append( ['rm', '-f', OUTFILE[:-3]+e] ) # entfernen von Hilfsdateien
        
        #Texteingabe ersetzt INFILE durch OUTFILE
        INFILE = templFiles[ self.titelseite.radioSprache.get() ]
        with open(INFILE,'r', encoding='utf-8') as templatefile:
            iTEXT = templatefile.readlines()
        
        oTEXT = []
        
        for line in iTEXT:
            #nl - Zeile wird gelesen, Suchwort wird ersetzt
            #nl.replace - Fortsetzung in der nächsten Zeile
            nl = line.replace('<txtTitel>', self.strToLaTeX( self.sopData['txtTitel'] ))
            nl = nl.replace('<txtSOPNr>', self.strToLaTeX(self.sopData['txtSOPNr']))
            nl = nl.replace('<txtVersion>', self.strToLaTeX(self.sopData['txtVersion'])) #Version = Letzte Versionsnummer in Änderungshistorie
            nl = nl.replace('<txtInst>', self.strToLaTeX(self.sopData['txtInst']))
            nl = nl.replace('<txtAbt>', self.strToLaTeX(self.sopData['txtAbt']))
            nl = nl.replace('<CName>', self.strToLaTeX(self.sopData['CName']))
            nl = nl.replace('<CYear>', self.strToLaTeX(str(self.sopData['CYear'])))
            nl = nl.replace('<CMonth>', self.strToLaTeX(str(self.sopData['CMonth'])))
            nl = nl.replace('<CDay>', self.strToLaTeX(str(self.sopData['CDay'])))
            nl = nl.replace('<Ch1Name>', self.strToLaTeX(self.sopData['Ch1Name']))
            nl = nl.replace('<Ch1Year>', self.strToLaTeX(str(self.sopData['Ch1Year'])))
            nl = nl.replace('<Ch1Month>', self.strToLaTeX(str(self.sopData['Ch1Month'])))
            nl = nl.replace('<Ch1Day>', self.strToLaTeX(str(self.sopData['Ch1Day'])))
            nl = nl.replace('<Ch2Name>', self.strToLaTeX(self.sopData['Ch2Name']))
            nl = nl.replace('<Ch2Year>', self.strToLaTeX(str(self.sopData['Ch2Year'])))
            nl = nl.replace('<Ch2Month>', self.strToLaTeX(str(self.sopData['Ch2Month'])))
            nl = nl.replace('<Ch2Day>', self.strToLaTeX(str(self.sopData['Ch2Day'])))
            nl = nl.replace('<AppName>', self.strToLaTeX(self.sopData['AppName']))
            nl = nl.replace('<AppYear>', self.strToLaTeX(str(self.sopData['AppYear'])))
            nl = nl.replace('<AppMonth>', self.strToLaTeX(str(self.sopData['AppMonth'])))
            nl = nl.replace('<AppDay>', self.strToLaTeX(str(self.sopData['AppDay'])))
            nl = nl.replace('<RName>', self.strToLaTeX(self.sopData['RName']))
            nl = nl.replace('<RYear>', self.strToLaTeX(str(self.sopData['RYear'])))
            nl = nl.replace('<RMonth>', self.strToLaTeX(str(self.sopData['RMonth'])))
            nl = nl.replace('<RDay>', self.strToLaTeX(str(self.sopData['RDay'])))
            
            if self.sopData['LaEinl'] == True:
                nl = nl.replace('<TEinleitung>', self.sopData['TEinleitung'].rstrip()) #Textfelder benötigen einen Start- und Endwert
            else:
                nl = nl.replace('<TEinleitung>', self.strToLaTeX(self.sopData['TEinleitung']).rstrip() )
                
            if self.sopData['LaZw'] == True:    
                nl = nl.replace('<TZweck>', self.sopData['TZweck'].rstrip())
            else:
                nl = nl.replace('<TZweck>', self.strToLaTeX(self.sopData['TZweck']).rstrip() )
            
            if self.sopData['LaGe'] == True:
                nl = nl.replace('<TGeltungsbereich>', self.sopData['TGeltungsbereich'].rstrip())
            else:
                nl = nl.replace('<TGeltungsbereich>', self.strToLaTeX(self.sopData['TGeltungsbereich']).rstrip() )
            
            if self.sopData['LaVe'] == True:
                nl = nl.replace('<TVerantwortlichkeiten>', self.sopData['TVerantwortlichkeit'].rstrip())
            else:
                nl = nl.replace('<TVerantwortlichkeiten>', self.strToLaTeX( self.sopData['TVerantwortlichkeit']).rstrip() )
                
            temp_str = '\\begin{table}[H]\n\\centering\n\\renewcommand{\\arraystretch}{1.5}\n\\begin{tabular}{ll}\n'
            if len(self.sopData['TAbk'])>0:    
                for n in self.sopData['TAbk']: #Element dieser Liste = Liste mit zwei Elementen ['', '']
                    temp_str = temp_str + self.strToLaTeX(n[0].rstrip()) + ' & ' + self.strToLaTeX(n[1].rstrip()) + ' \\\\\n' #Erstellung eines Hilfstrings aus allen Objektelementen        
            else:
                temp_str = temp_str + 'N/A' + '\\\\\n' #Wenn kein Eintrag vorhanden ist, erscheint im PDF an dieser Stelle ein N/A.
            temp_str = temp_str + '\\end{tabular}\n\\end{table}'    
            nl = nl.replace('<TAbk>', temp_str) #Hilfsstring wird eingesetzt
            
            temp_str = '' #Option einen \LaTeX cmd einzusetzen.
            if len(self.sopData['TDef'])>0:
                for n in self.sopData['TDef']:
                    temp_str = temp_str + self.strToLaTeX(n.rstrip()) + '\\\\\\\\\n'
            else:
                temp_str = temp_str + 'N/A'
            nl = nl.replace('<TDef>', temp_str)
            
            temp_str = ''
            if len(self.sopData['TVerfahren'])>0:
                for n in self.sopData['TVerfahren']:
                    temp_str = temp_str + '\\begin{description}\n\\item ' + self.strToLaTeX(n[0].rstrip()) + \
                               '\n\\end{description}\n' + self.strToLaTeX(n[1].rstrip()) + '\\\\\n'
            else:
                temp_str = temp_str + 'N/A'
            nl = nl.replace('<TVerfahren>', temp_str)
            
            temp_str = '\\begin{table}[H]\n\\centering\n\\renewcommand{\\arraystretch}{1.5}\n\\begin{tabular}{p{2cm}p{9cm}}\n00 & init. Version\\\\'
            if len(self.sopData['THistory'])>0:    
                for n in self.sopData['THistory']: #Element dieser Liste = Liste mit zwei Elementen ['', '']
                    temp_str = temp_str + self.strToLaTeX(n[0].rstrip()) +  ' & ' + self.strToLaTeX(n[1].rstrip()) + '\\\\\n' #Erstellung eines Hilfstrings aus allen Objektelementen        
            else:
                pass
            temp_str = temp_str + '\\end{tabular}\n\\end{table}'    
            nl = nl.replace('<THistory>', temp_str) #Hilfsstring wird eingesetzt
            
            temp_str = '\\begin{itemize}\n'
            if len(self.sopData['TIntern'])>0:
                for n in self.sopData['TIntern']:
                    temp_str = temp_str + '\\item ' + self.strToLaTeX(n.rstrip()) + '\\\\\n'
            else:
                temp_str = temp_str + '\\item ' + 'N/A' + '\\\\\n'
            temp_str = temp_str + '\\end{itemize}'
            nl = nl.replace('<TIntern>', temp_str)
            
            temp_str = '\\begin{itemize}\n'
            if len(self.sopData['TExtern'])>0:
                for n in self.sopData['TExtern']:
                    temp_str = temp_str + '\\item ' + self.strToLaTeX(n.rstrip()) + '\\\\\n'
            else:
                temp_str = temp_str + '\\item ' + 'N/A' + '\\\\\n'
            temp_str = temp_str + '\\end{itemize}'
            nl = nl.replace('<TExtern>', temp_str)
            
            temp_str = '\\begin{itemize}\n'
            if len(self.sopData['TLgl'])>0:
                for n in self.sopData['TLgl']:
                    temp_str = temp_str + '\\item ' + self.strToLaTeX(n.rstrip()) + '\\\\\n'
            else:
                temp_str = temp_str + '\\item ' + 'N/A' + '\\\\\n'
            temp_str = temp_str + '\\end{itemize}'
            nl = nl.replace('<TLgl>', temp_str)
            
            temp_str = '\\begin{itemize}\n'
            if len(self.sopData['TAnhang'])>0:
                for n in self.sopData['TAnhang']:
                    temp_str = temp_str + '\\item ' + self.strToLaTeX(n.rstrip()) + '\\\\\n'
            else:
                temp_str = temp_str + '\\item ' + 'N/A' + '\\\\\n'
            temp_str = temp_str + '\\end{itemize}'     
            nl = nl.replace('<TAnhang>', temp_str)
            
            oTEXT.append(nl)

        with open(OUTPATH+OUTFILE,'w', encoding='utf-8') as of:
            of.writelines(oTEXT)
        
        pwd = os.getcwd()
        for cmd in cmds: #cmd = spawn child process
            with Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=pwd+'/'+OUTPATH) as proc:
                data = proc.communicate()
                if len(data[1])>0:
                    print('! error: ' + data[1].decode())
                else:
                    print(data[0].decode())
        
        ret = messagebox.askokcancel('Bekanntmachung! ', 'Ihre SOP wird als PDF exportiert!\nPDF öffnen?')
        if ret == True:
            pdffile = OUTFILE[:-3] + 'pdf'
            print('pdf file: '+pdffile)
            if os.name == 'nt': #windows
                os.startfile(pwd+'/'+OUTPATH+pdffile)
            elif os.name == 'posix': #unix/linux
                os.system('/usr/bin/xdg-open '+pwd+'/'+OUTPATH+pdffile)
        else:
            pass
    
    #------------------------------------
    
    def strToLaTeX(self, InStr): #reservierte Sonderzeichen ersetzen, um Probleme mit dem Latexformat zu vermeiden
        temp_str = InStr.replace('\\', '\\\\')
        temp_str = temp_str.replace('{', r'\{') #r = raw-string literal
        temp_str = temp_str.replace('}', r'\}')
        temp_str = temp_str.replace('_', r'\_')
        temp_str = temp_str.replace('%', r'\%')
        temp_str = temp_str.replace('&', r'\&')
        temp_str = temp_str.replace('^', r'\^')
        temp_str = temp_str.replace('#', r'\#')
        temp_str = temp_str.replace('<', r'\textless ')
        temp_str = temp_str.replace('>', r'\textgreater ')
        temp_str = temp_str.replace('~', r'$\sim$ ')
        return temp_str

    #------------------------------------- 
        


if __name__ == "__main__":
    #zuerst config Datei laden
    with open('sopgui.cfg', 'r', encoding='utf-8') as myfile:
        cfg = json.load(myfile)
    dbHost = cfg['HOST']
    dbPort = cfg['PORT']
    dbauthSource = cfg['AUTHSRC']
    templFiles = cfg['TEMPL']
    
    
    root = Tk()
    root.title('Test SOP')
    root.geometry('900x500+300+300')
    root.update()
    #MainApplication(root).pack(side="top", fill="both", expand=True)
    MainApplication(root)
    

    root.mainloop()
