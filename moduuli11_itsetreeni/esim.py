class Tyontekija:
    tyontekijoiden_lukumaara = 0

    def __init__(self, etunimi, sukunimi):
        Tyontekija.tyontekijoiden_lukumaara += 1
        self.tyontekijanumero = Tyontekija.tyontekijoiden_lukumaara
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.tyontekijanumero}: {self.etunimi} {self.sukunimi}")


class Tuntipalkkainen(Tyontekija):

    def __init__(self, etunimi, sukunimi, tuntipalkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = tuntipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Tuntipalkka: {self.tuntipalkka}")


class Kuukausipalkkainen(Tyontekija):

    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        self.kuukausipalkka = kuukausipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Kuukausipalkka: {self.kuukausipalkka}")


tyontekijat = []
tyontekijat.append(Tuntipalkkainen("Viivi", "Virta", 12.35))
tyontekijat.append(Kuukausipalkkainen("Ahmed", "Habib", 2750))
tyontekijat.append(Tyontekija("Pekka", "Puro"))
tyontekijat.append(Tuntipalkkainen("Olga", "Glebova", 14.92))

for t in tyontekijat:
    t.tulosta_tiedot()
