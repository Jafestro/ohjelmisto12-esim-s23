cities = []
city = ""
print("Anna 5 kaupunkien nimet")
# Pydetään kaupunkia käyttäjältä ja lisätään niitä listan
for i in range(0, 5):
    city = input(f"{i + 1}:n kaupunki: ")
    cities.append(city)
# Tulostetan kaupunkia listalta
for city in cities:
    print(city)
