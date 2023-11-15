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
        print(f"Auton nopeus nyt on {self.hetkinen_nopeus}")

    def kulje(self, tuntimaara):
        kuljettu_matka = self.hetkinen_nopeus * tuntimaara
        self.kuljettu_matka += kuljettu_matka
        print(f"{tuntimaara} tunnissa on kuljettu {kuljettu_matka}km")


auto = Auto("ABC-123", 142)
auto.kiihdyta("60")
auto.kuljettu_matka = 2000
auto.kulje(1.5)
print(f"Yleensä on kuljettu {auto.kuljettu_matka} km")
