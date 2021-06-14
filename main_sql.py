import sqlite3

conn = sqlite3.connect('prototipi.db')
curs = conn.cursor()

try:
    curs.execute("DROP table prototipo")
    curs.execute("DROP table dipartimento")
except:
    pass

curs.execute("CREATE table prototipo (nome char(20),descrizione char(300),dipartimento char(30))")

class Prototipo():

    def __init__(self,nome,descrizione):
        self.nome = nome 
        self.descrizione = descrizione

    def modifica(self,nome,descrizione):
        self.nome = nome
        self.descrizione = descrizione

    def stampa(self):
        print(f"Il prototipo {self.nome},{self.descrizione}")

class Dipartimento():
    def __init__(self,nome,cursore):
        self.nome = nome
        self.prototipi = list()
        self.cursore = cursore

    def aggiungi_prototipo(self,prototipo):
        self.prototipi.append(prototipo)
        row = (prototipo.nome, prototipo.descrizione,self.nome)
        self.cursore.execute("INSERT INTO prototipo values(?,?,?)",row)
        print("Il prototipo é stato aggiunto con successo!")

    def cancella(self,prototipo):
        if prototipo in self.prototipi:
            self.prototipi.remove(stampante)
            self.cursore.execute("DELETE FROM prototipo WHERE nome = ?",(prototipo.nome,))
            print("Il prototipo é stato rimosso con successo!")
        else:
            print("Il prototipo non é presente!")

    def cerca_prototipo(self,nome):
        for prototipo in self.prototipi:
            if prototipo.nome == nome:
                prototipo.stampa()
        print("dal database:")
        self.cursore.execute("SELECT * FROM prototipo WHERE nome = ?",(prototipo.nome, ))
        for row in self.cursore.fetchall():
            print(row)


    def stampa_dipartimento(self):
        for prototipo in self.prototipi:
            prototipo.stampa()
        print("Dal database:")
        self.cursore.execute("SELECT * FROM prototipo")
        for row in self.cursore.fetchall():
            print(row)

telefonia = Dipartimento("telefonia",curs)

prototipo1 = Prototipo("cover-Iphone12","nuova cover per Iphone12")
prototipo2 = Prototipo("cover-Andoid","nuova cover per Android")


telefonia.aggiungi_prototipo(prototipo1)
telefonia.aggiungi_prototipo(prototipo2)

telefonia.stampa_dipartimento()
telefonia.cerca_prototipo("cover-Iphone12")

conn.commit()
conn.close()