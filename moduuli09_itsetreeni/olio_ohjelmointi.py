class Koira:
    tehty = 0

    def __init__(self, nimi, vuosi, haukahdus="Vuh vuh"):
        self.nimi = nimi
        self.vuosi = vuosi
        self.haukahdus = haukahdus
        Koira.tehty += 1

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(f"{self.haukahdus}")


# koira.nimi = "Rekku"
# koira.vuosi = 2022

# print(f"Minulla on koira nimeltään {koira1.nimi} ja hän syntynyt vuonna {koira2.vuosi}.")


koira1 = Koira('Rekku', 2022)
print(f"Koiria on nyt {Koira.tehty}")
koira2 = Koira('Jake', 2021, "Adventure Time!")
print(f"Koiria on nyt {koira2.tehty}")

koira1.hauku(2)
koira2.hauku(7)
