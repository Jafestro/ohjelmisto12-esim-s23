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


auto = Auto("ABC-123", 142)
auto.kiihdyta("30")
auto.kiihdyta("70")
auto.kiihdyta("50")
auto.kiihdyta("-200")