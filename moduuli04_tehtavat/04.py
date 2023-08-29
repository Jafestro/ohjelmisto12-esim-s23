import random

rdnum = random.randint(1, 10)
user = -1
print("Tietokone arpoo kokonaisluvun väliltä 1..10")
while user != rdnum:
    user = int(input("Sun arvosi: "))
    if user <= 0:
        print("Ei saa olla pienempi tai yhtäkuin 0")
    elif user > rdnum:
        print("Liian suuri arvaus")
    elif user < rdnum:
        print("Liian pieni arvaus")

print("Oikein! Onneksi Olkoon!")
