# Kysytään numeroita
print("\n\nAnna kolme kokonaislukua siis voisin lasketa niiden keskiarvo, summa ja tulo")
num_1 = int(input("luku 1: "))
num_2 = int(input("luku 2: "))
num_3 = int(input("luku 3: "))

# Lasketetaan keskiarvo
keskiarvo = (num_3 + num_2 + num_1) / 3
# Lasketetaan tulo
tulo = num_3 * num_2 * num_1
# Lasketetaan summa
summa = num_3 + num_2 + num_1

#tulostetaan niitä
print(f"Keskiarvo: {keskiarvo}\nTulo: {tulo}\nSumma: {summa}")
