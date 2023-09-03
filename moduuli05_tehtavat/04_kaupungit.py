cities = []
city = ""
print("Anna 5 kaupunkien nimet")
for i in range(0, 5):
    city = input(f"{i + 1}:n kaupunki: ")
    cities.append(city)

for city in cities:
    print(city)
