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


auto_lista = []

# Luoda ja lisätä uus auto oliot listaan
for i in range(1, 11):
    huippu_nopeus = random.randint(100, 200)
    auto_lista.append(Auto(f"ABC-{i}", huippu_nopeus))

sorted_auto_lista = []

# Tää silmukka loppu kun yksi auto kulje enemmän tai yhtä suuri kuin 10000 kilsa
while True:
    # Tää sortaa auto_lista kuljettu matka käyttäen ja sortaa se enemmästä vähemmään
    sorted_auto_lista = sorted(auto_lista, key=lambda auto: auto.kuljettu_matka, reverse=True)

    if sorted_auto_lista[0].kuljettu_matka >= 10000:
        break
    for auto in auto_lista:
        auto.kiihdyta(f"{random.randint(-10, 15)}")
        auto.kulje(1)

# Tulosta kaikki autot
i = 1
for auto in sorted_auto_lista:
    print(f"{i}. Kilpa Numero:{auto.rekisteritunnus}, Huippunopeus:{auto.huippunopeus}km/h, "
          f"Hetkinen nopeus:{auto.hetkinen_nopeus}km/h, Kuljettu matka:{auto.kuljettu_matka}km")
    i += 1
