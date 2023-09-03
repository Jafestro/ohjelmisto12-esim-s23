luku = '-'
lista = []
while luku != "":
    try:
        luku = int(input("Syöte luku: (Jos haluat pois paina vain Enter)\n"))
    except ValueError:
        luku = ""
    if luku != "":
        lista.append(luku)
lista.sort(reverse=True)
print(f"5 suurinta lukuja listasta: {lista[0:5]}")
