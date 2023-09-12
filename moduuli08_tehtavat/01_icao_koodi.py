"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen
ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
"""

import mysql.connector


# Funktio: ICAO koodin avulla etsi vastaava lentokentän nimi ja sijanti eli maa
def get_lentokoneasema(icao):
    # SQL kysely
    sql = "select airport.name, country.name from airport, country"
    sql += " where ident='" + icao + "'"
    sql += " and airport.iso_country=country.iso_country;"

    # Tietokannan ja pycharm valillä yhdeyksen asentaminen ja kyselyn tehtäminen ja tuloksen saaminen
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    # Tsekataan jos tulos on tyhjä tai ei
    if kursori.rowcount > 0:
        # Jos ei oo tyhjä tulostetaan ensi lentokentaan nimi ja
        # sen jälkeen sijanti eli maa
        print(f"Lentokoneasema: {tulos[0][0]}\nSijanti: {tulos[0][1]}")
        return tulos  # Palautetaan tulos

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

icao_code = input("Anna icao koodi, että tämä ohjelma pystyy "
                  "tulostaa vastavaan lentokonenimi ja sen sijanti:\n")
lentokoneasema = get_lentokoneasema(icao_code)
