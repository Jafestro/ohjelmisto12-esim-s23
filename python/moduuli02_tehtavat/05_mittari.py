# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

# Kysytään leviskain
leviskat = int(input("Anna leiviskät.\n"))
print()
naulat = int(input("Anna naulat.\n"))
print()
luodit = float(input("Anna luodit.\n"))
print()

# painet
luodit_paine = 13.3
naula_paine = 32 * luodit_paine
leiviska_paine = 20 * naula_paine

# lasketetaan koko paine
result = (leviskat * leiviska_paine) + (naulat * naula_paine) + (luodit * luodit_paine)

# tulostetaan paine
print("Massa nykymittojen mukaan:")
print(f"{(result // 1000):.0f} kilogrammaa ja {(result % 1000):.2f} grammaa.")
