luku = int(input("Anna arvo siis minä voisin tsekata jos se on alkuluku tai ei:  "))

if luku <= 1:
    print(f"{luku} ei ole alkuluku")
else:
    alku = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            if i != luku:
                print(f"{luku} ei oo alkuluku")
                alku = False
                break
    if alku:
        print(f"{luku} on alkuluku.")

