class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}", end=" ")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"(päätoimittaja {self.paatoimittaja})")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"(kirjailija {self.kirjailija}, {self.sivumaara} sivua)")


# Pääohjelma
julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for julkaisu in julkaisut:
    julkaisu.tulosta_tiedot()
