import peewee

db = peewee.SqliteDatabase("stampanti_peewee.db")

class DipartimentoStampanti(peewee.Model):
    nome = peewee.CharField()
    descrizione = peewee.CharField()
    dipartimento = peewee.CharField()

    class Meta:
        database = db
        db_table = 'stampanti'

DipartimentoStampanti.create_table(DipartimentoStampanti)

stampante1 = DipartimentoStampanti.create(nome = "3DRAG",descrizione = "si tratta di una macchina molto versatile e che si presta a differenti utilizzi",dipartimento = "industriale")
stampante2 = DipartimentoStampanti.create(nome = "Alfawise",descrizione = "è una macchina di costruzione cinese, il suo volume è di 300 x 300 x 400 mm",dipartimento = "industriale")

stampante1.save()
stampante2.save()

stampanti = DipartimentoStampanti.select()

for stampante in stampanti:
    print(stampante.nome,stampante.descrizione)