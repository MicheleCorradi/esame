import peewee

db = peewee.SqliteDatabase("prototipi_peewee.db")

class DipartimentoPrototipi(peewee.Model):
    nome = peewee.CharField()
    descrizione = peewee.CharField()
    dipartimento = peewee.CharField()

    class Meta:
        database = db
        db_table = 'prototipi'

DipartimentoPrototipi.create_table(DipartimentoPrototipi)

prototipo1 = DipartimentoPrototipi.create(nome = "cover-Iphone12",descrizione = "nuova cover per Iphone12",dipartimento = "telefonia")
prototipo2 = DipartimentoPrototipi.create(nome = "cover-Andoid",descrizione = "nuova cover per Android",dipartimento = "telefonia")

prototipo1.save()
prototipo2.save()

prototipi = DipartimentoPrototipi.select()

for prototipo in prototipi:
    print(prototipo.nome,prototipo.descrizione)