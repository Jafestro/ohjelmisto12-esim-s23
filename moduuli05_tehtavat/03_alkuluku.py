luku = int(input("Anna arvo siis minä voisin tsekata jos se on alkuluku tai ei:  "))

# TODO: Needs Optimizing
if luku % 1 == 0 and luku % luku == 0:
    alku = True
    for i in range(2, 101):
        if luku % i == 0:
            if i != luku:
                print(f"{luku} ei oo alkuluku")
                alku = False
                break

    if alku:
        print(f"{luku} on alkuluku.")
