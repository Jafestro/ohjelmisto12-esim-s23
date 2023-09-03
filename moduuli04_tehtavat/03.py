user = 0
lista = list()

while user != "":

    user = input(
        "Syötä numeroita siis ohjelma tulostaa saaduista luvuista pienimmän "
        "ja suurimman: (Jos halut pois syötä tyhjän merkkijonon)\n")

    if user.isdigit() or user[1:].isdigit():
        lista.append(int(user))

print(f"Pienin arvo listassa on {min(lista)}")
print(f"Suurin arvo listassa on {max(lista)}")
