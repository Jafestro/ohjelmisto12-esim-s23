import mysql.connector
from geopy import distance


# Funktio
def get_latitude_and_longtitude_by_icao(icao):
    # SQL kysely latitude ja longtitude palautamisen varten
    sql = "select latitude_deg, longitude_deg from airport"
    sql += " where ident ='" + icao + "';"

    # Tietokannan ja pycharm valillä yhdeyksen asentaminen ja kyselyn tehtäminen ja tuloksen saaminen
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    # Tsekataan jos tulos on tyhjä tai ei
    if tulos:
        # Jos ei tyhjä tulostetaan taulu rivi riviltä ja palautetaan tulos eli taulu
        sijanti = tulos[0]
        return sijanti

    # Jos tulos on tyhjä tulostetaan virhe viesti ja palautetaan tyhjän listaan
    print("LENTOKONEASEMA_NOT_FOUND_404")
    print("RETURN_EMPTY_LIST")
    return list()


# Funktio
def measure_distance_between_lentokentta(icao_1, icao_2):
    sijanti_1 = get_latitude_and_longtitude_by_icao(icao_1)
    sijanti_2 = get_latitude_and_longtitude_by_icao(icao_2)

    return distance.distance(sijanti_1, sijanti_2).km


# Pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

print("Anna 2 icao koodia, että tämä ohjelma pystyy "
      "tulostaa lentokenttien välisen etäisyyden kilometreinä:\n")
icao_code_1 = input("Eka ICAO koodi: ")
icao_code_2 = input("Toinen ICAO koodi: ")
distance_between = measure_distance_between_lentokentta(icao_code_1, icao_code_2)
print(f"Lentokenttien välisen etäisyyden kilometreinä on {distance_between:.2f} km.")
