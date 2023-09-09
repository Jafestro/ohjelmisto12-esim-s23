import random


def random_silmaluku(side_max_number):
    return random.randint(1, side_max_number)  # Palautetaan satunnainen silmaluvun


silmaluku = 0  # Alkupointti

# Kysy käyttäjältä maksimisilmäluku
maksimisilmaluku = int(input("Anna nopan maksimisilmäluku:  "))

# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun
while silmaluku != maksimisilmaluku:
    silmaluku = random_silmaluku(maksimisilmaluku)
    print(silmaluku)
