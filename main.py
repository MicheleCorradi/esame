import pickle

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
    def __init__(self,nome):
        self.nome = nome
        self.stampanti = list()
        self.database = self.nome + ".p"

    def aggiungi_stampante(self,stampante):
        self.stampanti.append(stampante)
        print("La stampante é stata aggiunta con successo!")

    def cancella(self,stampante):
        if stampante in self.stampanti:
            self.stampanti.remove(stampante)
            print("La stampante é stata rimossa con successo!")
        else:
            print("La stampante non é presente!")

    def cerca_stampante(self,nome):
        for stampante in self.stampanti:
            if stampante.nome == nome:
                stampante.stampa()

    def stampa_dipartimento(self):
        for stampante in self.stampanti:
            stampante.stampa()

    def salva(self):
        with open(self.database, 'wb') as file:
            pickle.dump(self.stampanti, file)

    def carica(self):
        with open(self.database, 'rb') as file:
            self.stampanti = pickle.load(file)

industriale = Dipartimento("industriale")

stampante1 = Stampante("3DRAG","si tratta di una macchina molto versatile e che si presta a differenti utilizzi")
stampante2 = Stampante("Alfawise","è una macchina di costruzione cinese, il suo volume è di 300 x 300 x 400 mm")

industriale.aggiungi_stampante(stampante1)
industriale.aggiungi_stampante(stampante2)

#stampante1.modifica("nuova stampante","prova")

#industriale.cancella(stampante2)

#industriale.cerca_stampante("Alfawise")

industriale.salva()
industriale.carica()

industriale.stampa_dipartimento()
