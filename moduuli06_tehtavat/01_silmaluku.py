import random


def random_silmaluku():
    return random.randint(1, 6)  # Palautetaan satunnainen silmaluvun


silmaluku = 0  # Alkupointti

# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun
while silmaluku != 6:
    silmaluku = random_silmaluku()
    print(silmaluku)
