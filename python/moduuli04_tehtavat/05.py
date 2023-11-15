data = ["python", "rules"]
kertaa = 0

while True:
    user_login = input("Anna käyttäjätunnuksen: ")
    user_password = input("Anna salasana: ")
    if user_login == data[0] and data[1] == user_password:
        print("Tervetuloa")
        break
    else:
        kertaa += 1
    if kertaa == 5:
        print("Pääsy evätty")
        break
