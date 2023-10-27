# Auto luokka
import random


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


# Kilpailu luokka
class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = autolista

    # muokata auton hetkinen nopeus ja tossa nopeudella auto kulje tunnin.
    def tunti_kuluu(self):
        for auto in self.autolista:
            nopeus = random.randint(-10, 15)
            auto.kiihdyta(str(nopeus))
            auto.kulje(1)

    # tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna
    def tulosta_tilanne(self):
        i = 1
        for auto in self.autolista:
            print(f"{i}. Kilpa Numero:{auto.rekisteritunnus}, Huippunopeus:{auto.huippunopeus}km/h, "
                  f"Hetkinen nopeus:{auto.hetkinen_nopeus}km/h, Kuljettu matka:{auto.kuljettu_matka}km")
            i += 1

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


# Pääohjelma
autolista = []

# Luoda ja lisätä uus auto oliot listaan
for i in range(1, 11):
    huippu_nopeus = random.randint(100, 200)
    autolista.append(Auto(f"ABC-{i}", huippu_nopeus))

# Luodan kilpailu
kilpailu = Kilpailu("Suuri romuralli", 8000, autolista)

loppu = False
tunti = 0
print("******************************🏁ALOITETAAN KILPAILU!🏁******************************")
while not loppu:
    kilpailu.tunti_kuluu()
    tunti += 1
    loppu = kilpailu.kilpailu_ohi()
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()
        print()
        print("#######################- 10 TUNTI KULUU -#######################")
        print()

print("******************************---🏆KILPAILU OHI!🏆---******************************")
kilpailu.tulosta_tilanne()
