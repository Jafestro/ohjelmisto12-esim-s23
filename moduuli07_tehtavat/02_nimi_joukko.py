nimet = set()

while True:
    nimi = str(input("Syötä nimesi: "))
    if nimi == "":
        print("Nähään!")
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")
    elif nimi not in nimet:
        print("Uusi nimi:")
        nimet.add(nimi)
print("Kaikki nimet joukossa: ")
for name in nimet:
    print(name)
