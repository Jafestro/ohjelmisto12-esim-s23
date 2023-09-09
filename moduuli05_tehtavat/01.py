import random

"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
Käytä for-toistorakennetta.
"""

lukumaara = int(input("Anna arpakuutioiden lukumäärän: "))
summa = 0
for luku in range(1, lukumaara + 1):
    print(f"{luku}:n arpakuution arvo: {random.randint(1, 6)}")
    summa += luku
print(f"Koko summa on: {summa}")
