nimet = set()

# Käyttäjä antaa nimet ja jos annettu nimi on uusi se lisätty joukon
# mutta jos se on jo aiemmin syötetty nimi siis ei lisätään joukoon
while True:
    nimi = str(input("Syötä nimesi: (Jos halut pois paina vain Enter) \n"))
    if nimi == "":
        print("Nähään!")
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")
    elif nimi not in nimet:
        print("Uusi nimi:")
        nimet.add(nimi)
# Tulostaa kaikki nimet, että ovat joukossa
print("Kaikki nimet joukossa: ")
for name in nimet:
    print(name)
