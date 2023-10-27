class Hissi:
    def __init__(self, alimman_kerros, ylimman_kerros):
        self.alimman_kerros = alimman_kerros
        self.ylimman_kerros = ylimman_kerros
        self.kerros = alimman_kerros

    def kerros_ylos(self):
        if self.kerros != self.ylimman_kerros:
            self.kerros += 1
            print(f"Tuleva kerros on {self.kerros}")
        else:
            print("Olet jo ylimmässä kerroksessa!")

    def kerros_alas(self):
        if self.kerros != self.alimman_kerros:
            self.kerros -= 1
            print(f"Tuleva kerros on {self.kerros}")
        else:
            print("Olet jo alimmassa kerroksessa!")

    def siirry_kerrokseen(self, kerros):
        kerta = self.kerros - kerros
        if kerta < 0:  # jos on miinus se tarkoittaa että pitää siirtää ylöspäin
            kerta *= -1
            for i in range(kerta):
                self.kerros_ylos()
        elif kerta > 0:  # jos on plus se tarkoittaa että pitää siirtää alaspäin
            for i in range(kerta):
                self.kerros_alas()
        elif kerta == 0:  # jos on nolla se tarkoittaa että olemme jo tarvittavassa kerroksessa
            print(f"Olemme jo {kerros}. kerroksessa!")
            return
        print(f"Olemme saapuneet {kerros} kerrokseen.")


hissi = Hissi(0, 15)

hissi.siirry_kerrokseen(0)
hissi.siirry_kerrokseen(hissi.alimman_kerros)

