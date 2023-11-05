class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, hetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkinen_nopeus = hetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, nopeus):
        if nopeus[0] == "-":
            self.hetkinen_nopeus -= int(nopeus[1:])
        else:
            self.hetkinen_nopeus += int(nopeus)
        if self.hetkinen_nopeus >= self.huippunopeus:
            self.hetkinen_nopeus = self.huippunopeus
        elif self.hetkinen_nopeus <= 0:
            self.hetkinen_nopeus = 0

    def kulje(self, tuntimaara):
        kuljettu_matka = self.hetkinen_nopeus * tuntimaara
        self.kuljettu_matka += kuljettu_matka


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akku_kapasiteetti_kilowattitunteina):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akku_kapasiteetti = akku_kapasiteetti_kilowattitunteina


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatanki_litroina):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatanki_litroina = bensatanki_litroina


# Pääohjelma
sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta("50")
polttomoottoriauto.kiihdyta("40")

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauton matkamittarilukema: {sahkoauto.kuljettu_matka} km")
print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.kuljettu_matka} km")
