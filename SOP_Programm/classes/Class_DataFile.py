#!/usr/bin/env python3
from pprint import pprint
import json
import os


class DataFile():
    '''
    Schnittstelle json files : Programm
    '''
    datadir = './data/'
    
    def __init__(self, *args, **kwargs):
        '''
        dummy: Kommunikationsparameter festlegen
        '''
        pass
    
    
    def login(self, dbuser=None, dbpw=None):
        '''
        dummy: Authentifizierung mit der Datenbank.
        '''
        return True
    
    
    def loadSOP(self, sopnr=None):
        '''
        Sucht nach SOP Datei mit dem passenden Namen und lädt diese.
        Rückgabe:  SOP dict
        Zum Beispiel: sop='GMP_001'
        '''
        if not sopnr == None:
            try:
                with open(self.datadir + sopnr + '.sop', 'r', encoding='utf-8') as myfile: #öffnen der entsprechenden Dateien
                    sop = json.load(myfile)
                sop['_id'] = None
            except:
                sop = None
        else:
            sop = None
        return sop
    
    
    def writeSOP(self, sopdata):
        '''
        Schreibt SOP dict in json Datei mit Nahmen aus SOPNr.
        Rückgabe: {}?? wenn geschrieben, None wenn nicht geschrieben
        '''
        filename = self.datadir + sopdata['txtSOPNr'] + '.sop'
        try:
            with open(filename, 'w') as myfile:
                json.dump(sopdata, myfile, indent=2, ensure_ascii=False) #ensure_ascii=False damit Umlaute und Sonderzeichen korrekt angezeigt werden
            upd = filename
        except:
            upd = None 
        return upd
    
    
    def SOPexists(self, sopNr):
        '''
        Liefert True wenn einen SOP mit der Nummer bereits existiert, sonst False
        '''
        files=os.listdir(self.datadir)
        allSOPnr = [e[:-4] for e in files if e[-4:]=='.sop'] #nimmt alle Einträge mit, die '.sop' enthalten
        
        return sopNr in allSOPnr
    
    
    def getSOPlist(self):
        '''
        Liefert SOPliste aller vorhandenen SoP Nr und Titel aus den Dateinamen
        '''
        # TBD
        # find & read all SOP files, get txtSOPNr and txtTitel from files
        allSOP = []
        files=os.listdir(self.datadir)
        sopFiles = [e for e in files if e[-4:]=='.sop'] #nimmt alle Einträge mit, die '.sop' enthalten
        
        for f in sopFiles:
            with open(self.datadir + f, 'r', encoding='utf-8') as myfile: #öffnen der entsprechenden Dateien
                sop = json.load(myfile)
            allSOP.append([f[:-4], sop['txtTitel']]) #Liste von Liste mit zwei Elementen ['Dateiname - Endung', 'Titel']
        return allSOP #Liste von Liste mit zwei Elementen
    
    
    def getUsers(self):
        '''
        Liefert Mitarbeiterliste inkl Position. Liest hierfür die Mitarbeiter.json aus.
        '''
        with open(self.datadir+'Mitarbeiter.json', 'r', encoding='utf-8') as myfile:
            users = json.load(myfile)
        
        return users
    
    
    
        

'''Programmstart'''

if __name__ == "__main__":
    #root = Tk()
    #root.title('Test Data')
    #root.geometry('300x350')
    #root.mainloop()


    #myDataClass = DataFile(host='zim.fritz.box', dport=27017, dauthSource='sopms')
    myDataClass = DataFile()
    
    #print( myDataClass.login(dbuser='RA', dbpw='6575RA') )   # login
    #print( myDataClass.login() )
    
    print( myDataClass.getSOPlist() )
    
    #print( myDataClass.getUsers() )
    
    if myDataClass.SOPexists('QM_009'):
        print('vorhanden')
    else:
        print('nicht vorhanden')


    d=myDataClass.loadSOP('QM_009')
    if d==None:
        print('SOP nicht vorhanden')
    else:
        #pprint(d)
        pass

    d['txtTitel']='SOP for Earthsampler'
    d['txtSOPNr']='QM_001'
    #myDataClass.writeSOP(d)
