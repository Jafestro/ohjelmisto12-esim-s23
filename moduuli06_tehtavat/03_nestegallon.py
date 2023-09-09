def usgallon_to_litre(gallon):
    return gallon * 3.785


# Alkusijanti
user_input = 0

while user_input >= 0:
    # Kysy käyttäjältä nestegallonin määrä
    user_input = int(input("Syöte nestegalloni määrä: (Jos halut pois anna negatiivi määrä)\n"))
    litre = usgallon_to_litre(user_input)
    if user_input >= 0:
        print(f"Yhdysvaltain nestegallonoina vastaava litramäärä on {litre}")
