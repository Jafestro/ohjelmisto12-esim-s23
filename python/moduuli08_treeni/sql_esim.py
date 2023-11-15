import mysql.connector

user = input("Anna user tunniksen: ")
password = input("Anna salasanasi: ")

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user=user,
    password=password,
    autocommit=True
)

print(yhteys)  # Testataan, että yhteys muodostuu virheittä
"""
kursori = yhteys.cursor()
sql = "select iso_country, name from country where iso_country ='fi';"
kursori.execute(sql)
tulos = kursori.fetchone()
if kursori.rowcount > 0: on sama if tulos:
    print(tulos)  
"""


def get_country_by_iso_code(iso_country):
    kursori = yhteys.cursor()
    sql = f"select iso_country, name from country where iso_country ='{iso_country}';"
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if tulos:
        return tulos
    else:
        return "No results."


country = get_country_by_iso_code('fi')
print(country)
country = get_country_by_iso_code(input("Syötä maakoodi: "))
print(country)


def update_country_by_iso_code(iso_code, country_name):
    kursori = yhteys.cursor()
    sql = f"update country set name='{country_name}' where iso_country ='{iso_code}';"
    kursori.execute(sql)
    if kursori.rowcount > 0:
        return f"koodi {iso_code} päivitetty, uusi maan nimi: {country_name}"
    else:
        return f"koodia {iso_code} ei löytynyt. Muutoksia ei tehty."


country_code = input("Syötä maakoodi: ")
country_name = input("Syötä maan nimi: ")
update_result = update_country_by_iso_code(country_code, country_name)
print(update_result)
yhteys.close()
