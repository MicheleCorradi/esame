import pickle

class Prototipo():

    def __init__(self,nome,descrizione):
        self.nome = nome 
        self.descrizione = descrizione

    def modifica(self,nome,descrizione):
        self.nome = nome
        self.descrizione = descrizione

    def stampa(self):
        print(f"Il Prototipo {self.nome},{self.descrizione}")

class Dipartimento():
    def __init__(self,nome):
        self.nome = nome
        self.prototipi = list()
        self.database = self.nome + ".p"

    def aggiungi_prototipo(self,prototipo):
        self.prototipi.append(prototipo)
        print("Il prototipo é stato aggiunto con successo!")

    def cancella(self,prototipo):
        if prototipo in self.prototipi:
            self.prototipi.remove(prototipo)
            print("Il prototipo é stato rimosso con successo!")
        else:
            print("Il prototipo non é presente!")

    def cerca_prototipo(self,nome):
        for prototipo in self.prototipi:
            if prototipo.nome == nome:
                prototipo.stampa()

    def stampa_dipartimento(self):
        for prototipo in self.prototipi:
            prototipo.stampa()

    def salva(self):
        with open(self.database, 'wb') as file:
            pickle.dump(self.prototipi, file)

    def carica(self):
        with open(self.database, 'rb') as file:
            self.prototipi = pickle.load(file)

telefonia = Dipartimento("telefonia")

prototipo1 = Prototipo("cover-Iphone12","nuova cover per Iphone12")
prototipo2 = Prototipo("cover-Andoid","nuova cover per Android")

telefonia.aggiungi_prototipo(prototipo1)
telefonia.aggiungi_prototipo(prototipo2)

prototipo1.modifica("nuova cover","prova")

#telefonia.cancella(prototipo2)

telefonia.cerca_prototipo("cover-Iphone12")

telefonia.salva()
telefonia.carica()

telefonia.stampa_dipartimento()
