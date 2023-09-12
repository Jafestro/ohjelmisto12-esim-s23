"""
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien
lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
"""
import mysql.connector


# Funktio tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin ja palautetaan vastaava lista
def get_lentokentan_lkm_typpien(maakoodi):
    # SQL kysely
    sql = "select airport.type, count(type) from airport, country"
    sql += " where airport.iso_country = country.iso_country and country.iso_country='" + maakoodi + "'"
    sql += " group by type;"

    # Tietokannan ja pycharm valillä yhdeyksen asentaminen ja kyselyn tehtäminen ja tuloksen saaminen
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    # Tsekataan jos tulos on tyhjä tai ei
    if kursori.rowcount > 0:
        # Jos ei tyhjä tulostetaan taulu rivi riviltä ja palautetaan tulos eli taulu
        for i in tulos:
            print(f"Tyyppi: {i[0]}, Count: {i[1]}")
        print()
        return tulos
    # Jos tulos on tyhjä tulostetaan virhe viesti ja palautetaan 0
    print("LENTOKONEASEMA_NOT_FOUND_404")
    print("RETURN_0")
    return 0


# Pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)
print("\nMorjes! Tää sovellus toimi näin: \nKäyttäjä, eli sinä:) "
      "kirjoittaa maakoodi ja tämä sovellus tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.\n")
maa_koodi = input("Syöte maakoodi: ")
get_lentokentan_lkm_typpien(maa_koodi)
