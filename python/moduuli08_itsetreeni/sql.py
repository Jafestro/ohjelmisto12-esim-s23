import mysql.connector


def hae_tyontekijat_sukunimella(sukunimi):
    sql = "select numero, sukunimi, etunimi, palkka from Tyontekija"
    sql += " where sukunimi='" + sukunimi + "';"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)  # Executing sql query

    # it returns result table which is get by executing the sql query.
    # You can also use fetchmany or fetchone if result table could be bigger than expected.
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:  # It checks if result table empty or not
        for rivi in tulos:  # if not it goes through each record
            print(f"Päivää! Olen {rivi[2]} {rivi[1]}. Palkkani on {rivi[3]} euroa kuussa.")
    return


def paivita_palkkaa(numero, uusipalkka):
    sql = "update tyontekija set palkka=" + str(uusipalkka) + " where numero=" + str(numero) + ";"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    if kursori.rowcount == 1:
        print("Palkka päivitetty")


# Pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='ihmiset',
    user='root',
    password='root',
    autocommit=True
)

last_name = input("Anna sukunimi: ")
hae_tyontekijat_sukunimella(last_name)

number = int(input("Anna numero: "))
uusiPalkka = float(input("Anna uusi palkka: "))
paivita_palkkaa(number, uusiPalkka)

last_name = input("Anna sukunimi: ")
hae_tyontekijat_sukunimella(last_name)
