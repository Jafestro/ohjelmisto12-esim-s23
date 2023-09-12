# Funktio puhdistaa parittomat luvut pois listalta
def only_even(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens


# data
lukuja = []
luku = input("Luku: ")  # Käyttäjä annaa jonkin luvun

while luku != "":  # Se ei pysähdy kunnes käyttäjä antaa tyhjä merkkijono eli nappa enter
    if luku.isnumeric() or luku[1:].isnumeric() and luku[0] == "-":  # tsekataan että input on luku tai ei
        lukuja.append(int(luku))  # jos totta lisätään luku listaan
    luku = input("Luku: ")  # Käyttäjä antaa uuden luvun

print(f"Alkuperäinen lista\n {lukuja}")
print(f"Muokattu/karsittu lista\n {only_even(lukuja)}")
