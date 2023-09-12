vuodenajat = ("Kevät", "Kesä", "Syksy", "Talvi")

user = int(input("Anna kuukauden numero siis minä voisin kertoa sinulle vastaavan vuodenajan: "))
if user in (1, 2, 12):
    print(f"Se on {vuodenajat[3]}")
elif user in range(3, 6):
    print(f"Se on {vuodenajat[0]}")
elif user in range(6, 9):
    print(f"Se on {vuodenajat[1]}")
elif user in range(9, 12):
    print(f"Se on {vuodenajat[2]}")
else:
    print("Kuukausi ja vuodenaja ei olemassa")
