class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, hetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkinen_nopeus = hetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka


auto = Auto("ABC-123", 142)

print(f'''
Rekisteritunnus: {auto.rekisteritunnus}
Huippinopeus: {auto.huippunopeus}
Hetkinen nopeus: {auto.hetkinen_nopeus}
Kuljettu matka: {auto.kuljettu_matka}
''')
