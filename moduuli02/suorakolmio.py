print("\n\nSyöte suorakolmion kanta ja korkeuden ja minä lasketetaan sen piiri ja pinta-alá")
kanta = float(input("Kanta: "))
korkeus = float(input("Korkeus: "))

piiri = (2 * kanta) + (2 * korkeus)
pinta_ala = kanta * korkeus

print(f"Suorakolmion piiri: {piiri}")
print(f"Suorakolmion pinta-ala: {pinta_ala}")
