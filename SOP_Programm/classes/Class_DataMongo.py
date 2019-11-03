#!/usr/bin/env python3
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pprint import pprint


class DataMongo():
    '''
    Schnittstelle Datenbank : Programm
    '''
    def __init__(self, host='localhost', dport=27017, dauthSource='sopms', **kwargs):
        '''
        Kommunikationsparameter festlegen
        '''
        self.myclient = MongoClient(host, port=dport, authSource=dauthSource, **kwargs)
        self.db = self.myclient['sopms'] # Datenbank 'sopms'
        self.coll = self.db['SOP'] # Collection 'SOP'
        self.ma = self.db['MAinfo'] # Collection 'MAinfo'
    
    
    def login(self, dbuser=None, dbpw=None):
        '''
        Authentifizierung mit der Datenbank. Liefert False bei falschem Login.
        '''
        try:
            login = self.db.authenticate(dbuser, dbpw)
            self.result = ''
        except Exception as e:
            print(e.args)
            self.result = e.args
            login = False
            #raise(e)
        finally:
            pass
        return login
    
    
    def loadSOP(self, sopnr=None):
        '''
        SOP aus Datenbank holen. Aufruf mit SOPNr. (string). Liefert None wenn nicht vorhanden.
        Zum Beispiel: sop='GMP_001'
        '''
        sop = self.coll.find_one({'txtSOPNr': sopnr})
        return sop
    
    
    def writeSOP(self, sopdata):
        '''
        SOP in die Datenbank schreiben. Parameter ist das SOP dict. Wenn Key "_id" vorhanden, erfolgt ein Update,
        aufgrund der Annahme, dass die SOP aus der DB geladen wurde. Wenn Key nicht vorhanden ist, wird ein
        neues Dokument (SOP) eingefügt
        '''
        if '_id' in sopdata.keys():
            upd = self.coll.update_one({'_id':sopdata['_id']}, {"$set": sopdata}, upsert=False)
        else:
            upd = self.coll.insert_one(sopdata)
        return upd


    def SOPexists(self, sopNr):
        '''
        Liefert True wenn eine SOP mit der Nummer bereits existiert, sonst False
        '''
        sop = self.coll.find_one({'txtSOPNr': sopNr})
        if sop == None:
            ret = False
        else:
            ret = True
        return ret
    
    
    def getSOPlist(self):
        '''
        Liefert SOPliste aller vorhandenen SOP-Nummern und -Titel
        '''
        allSOP = []
        for e in self.coll.find({'txtSOPNr':{'$exists': True} }, {'txtSOPNr':1, 'txtTitel':1}):  # returns only the SOP number
            print(e['txtSOPNr'])
            allSOP.append( [e['txtSOPNr'], e['txtTitel']] )
            
        return allSOP #Liste von Liste mit zwei Elementen
    
    
    def getUsers(self):
        '''
        Liefert Mitarbeiterliste inkl Position als dictionary
        '''
        userlst = []
        for e in self.ma.find({}, {'_id':0, 'Titel':1, 'Vorname':1, 'Nachname':1, 'Position':1}):  # returns only the SOP number
            if 'Title' in e.keys():
                title = e['Title']
            else:
                title = ''
            userlst.append( title + ' ' + e['Vorname'] + ' ' + e['Nachname'] + ' (' + e['Position'] + ')' )
        
        return userlst
    
    
    
        

'''Programmstart'''

if __name__ == "__main__":
    #root = Tk()
    #root.title('Test Mongo')
    #root.geometry('200x150')
    #root.mainloop()

    mymongo = DataMongo(host='zim.fritz.box', dport=27017, dauthSource='sopms', serverSelectionTimeoutMS=5000)
    
    #print( mymongo.login(dbuser='RA', dbpw='wekjfg') )   # fails
    print( mymongo.login(dbuser='RA', dbpw='6575RA') )   # login
    print( mymongo.result )
    
    print( mymongo.getSOPlist() )
    #print( mymongo.loadSOP('QM_007') )
    
    print( mymongo.getUsers() )

    print( mymongo.SOPexists('QM_010') )
    d=mymongo.loadSOP('QM_010')
    #d['txtTitel']='SOP for Earthsampler'
    #mymongo.writeSOP(d)
