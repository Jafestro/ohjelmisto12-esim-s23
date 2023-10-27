class Koira:
    def __init__(self, nimi, syntymavuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return


class Hoitola:

    def __init__(self):
        self.koirat = []

    def koira_sisaan(self, koira):
        self.koirat.append(koira)
        print(f"{koira.nimi} kirjattu sisään")
        return

    def koira_ulos(self, koira):
        self.koirat.remove(koira)
        return

    def tervehdi_koiria(self):
        for koira in self.koirat:
            koira.hauku(1)


# Pääohjelma
hoitola = Hoitola()

koira1 = Koira("Jake", 2021, "Adventure Time!")
koira2 = Koira("Muro", 2018)

hoitola.koira_sisaan(koira1)
hoitola.koira_sisaan(koira2)
hoitola.tervehdi_koiria()

hoitola.koira_ulos(koira2)
hoitola.tervehdi_koiria()
