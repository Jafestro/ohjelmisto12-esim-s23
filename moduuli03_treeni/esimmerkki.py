# valintarakenne

user_input = input("a vai b? ")

if user_input.lower() == "a":
    # koodilohko merkataan nyt sisentämällä 4 välilyöntiä
    print("Tee jotain.")
    print("ja jatka sitä")
elif user_input.lower() == "b":
    print("käyttäjä valitsi b:een")
    print("tehdään jotain muuta")
elif user_input.lower() == "c":
    print("käyttäjä valitsi c:een")
else:
    print("käyttäjä ei syöttänyt vain a:ta, tehdään jotain muuta")

print("ohjelman suoritus jatkuu tästä")

# Loogiset operaattorit
age = 5
name = "Ville"
print(age < 10)
print(name == "Ville")
print(age < 10 and name == "Ville")
print(age < 10 or name == "Ville")


print(not True)


age = int(input("Anna ikä: "))
paino = 0
if 15 <= age < 18:
    paino = float(input("Anna paino (kg): "))
    if paino >= 55:
        print("Lääkkeen käyttö on sallittua.")
if age >= 18:
    print("Lääkkeen käyttö on sallittua.")

