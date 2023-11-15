# Pyntetään kanta ja korkeus
print("\n\nSyöte suorakolmion kanta ja korkeuden ja minä lasketetaan sen piiri ja pinta-alá")
kanta = float(input("Kanta: "))
korkeus = float(input("Korkeus: "))

# lasketetaan piiri
piiri = (2 * kanta) + (2 * korkeus)

# lasketetaan pinta-ala
pinta_ala = kanta * korkeus

# tulostetaan niitä
print(f"Suorakolmion piiri: {piiri}")
print(f"Suorakolmion pinta-ala: {pinta_ala}")
