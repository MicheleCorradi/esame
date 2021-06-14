import sqlite3

conn = sqlite3.connect('stampanti.db')
curs = conn.cursor()

try:
    curs.execute("DROP table stampante")
    curs.execute("DROP table dipartimento")
except:
    pass

curs.execute("CREATE table stampante (nome char(20),descrizione char(300),dipartimento char(30))")

class Stampante():

    def __init__(self,nome,descrizione):
        self.nome = nome 
        self.descrizione = descrizione

    def modifica(self,nome,descrizione):
        self.nome = nome
        self.descrizione = descrizione

    def stampa(self):
        print(f"La stampante {self.nome},{self.descrizione}")

class Dipartimento():
    def __init__(self,nome,cursore):
        self.nome = nome
        self.stampanti = list()
        self.cursore = cursore

    def aggiungi_stampante(self,stampante):
        self.stampanti.append(stampante)
        row = (stampante.nome, stampante.descrizione,self.nome)
        self.cursore.execute("INSERT INTO stampante values(?,?,?)",row)
        print("La stampante é stata aggiunta con successo!")

    def cancella(self,stampante):
        if stampante in self.stampanti:
            self.stampanti.remove(stampante)
            self.cursore.execute("DELETE FROM stampamte WHERE nome = ?",(stampante.nome,))
            print("La stampante é stata rimossa con successo!")
        else:
            print("La stampante non é presente!")

    def cerca_stampante(self,nome):
        for stampante in self.stampanti:
            if stampante.nome == nome:
                stampante.stampa()
        print("dal database:")
        self.cursore.execute("SELECT * FROM stampante WHERE nome = ?",(stampante.nome, ))
        for row in self.cursore.fetchall():
            print(row)


    def stampa_dipartimento(self):
        for stampante in self.stampanti:
            stampante.stampa()
        print("Dal database:")
        self.cursore.execute("SELECT * FROM stampante")
        for row in self.cursore.fetchall():
            print(row)

industriale = Dipartimento("industriale",curs)

stampante1 = Stampante("3DRAG","si tratta di una macchina molto versatile e che si presta a differenti utilizzi")
stampante2 = Stampante("Alfawise","è una macchina di costruzione cinese, il suo volume è di 300 x 300 x 400 mm")


industriale.aggiungi_stampante(stampante1)
industriale.aggiungi_stampante(stampante2)

industriale.stampa_dipartimento()
industriale.cerca_stampante("Alfawise")

conn.commit()
conn.close()