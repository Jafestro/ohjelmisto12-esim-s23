luku = float((input("Syöte numero:  ")))

if luku > 0:
    print(f"{luku} on positiivinen")
elif luku < 0:
    print(f"{luku} on negatiivinen")
else:
    print("Numero on nolla")