import math

'''
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. 
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. 
Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, 
kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
 Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
'''


# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri
def pizza_price_per_square(diameter, price):
    return price / ((diameter / 2) ** 2 * math.pi)


print("Anna kaksi pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.")

pizza1_diameter = float(input("Ensi pizzan halkaisija: "))  # Kysy ensi pizzan halkaisijan
pizza1_price = float(input("Ensi pizzan hinta: "))  # Kysy ensi pizzan hinnan
pizza1_yksikkohinta = pizza_price_per_square(pizza1_diameter, pizza1_price)  # Lasketetaan ensi pizzan yksikköhinnan
pizza2_diameter = float(input("Toinen pizzan halkaisija: "))  # Kysy toinen pizzan halkaisijan
pizza2_price = float(input("Toinen pizzan hinta: "))  # Kysy toinen pizzan hinnan
pizza2_yksikkohinta = pizza_price_per_square(pizza2_diameter, pizza2_price)  # Lasketetaan toinen pizzan yksikköhinnan

if pizza1_yksikkohinta < pizza2_yksikkohinta:
    print("Toinen pizza on paras vaihtoehto")
elif pizza1_yksikkohinta > pizza2_yksikkohinta:
    print("Ensi pizza on paras vaihtoehto")
else:
    print(f"Molemmat ovat samanhintaisia")
