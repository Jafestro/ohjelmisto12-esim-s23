# Funktio tulostetaan koko menu
def menu():
    print("1. Haluan syöttää uuden lento aseman")
    print("2. Haluan hakea lentoaseman")
    print("3. Lopeta")
    return


# Tämä funktio on sovellus itse, siis kaikki tapuhtuu täällä
def lentoasema_sovellus():
    while True:  # toimii kunnes käyttäjä syötä 3
        menu()  # Tulostetaan menu
        choice = str(input("(1-3)   "))  # Käyttäjältä kysytään hänen valintan
        if choice == "1":
            nimi = str(input("Anna uuden lentoaseman nimi:  "))  # Käyttäjältä kysytään lentoaseman nimi
            icao = str(input("Anna sen ICAO - koodi:  "))  # Käyttäjältä kysytän lentoaseman icao koodi
            if nimi != "" and icao != "":
                lentoasemat[icao] = nimi  # Lisätään sanakirjaan
            else:
                print("NIMI_JA_ICAO_EI_SA_OLLA_TYHJÄ")
        elif choice == "2":
            icao = str(input("Anna lentoaseman ICAO - koodi:  "))  # Käyttäjältä kysytän lentoaseman icao koodi
            if icao in lentoasemat:
                print(lentoasemat[icao])  # Jos kysyttävä lentoasema on sanakirjassa, siis tulostetaan
            else:
                print("WRONG_INPUT")  # Jos kysyttävä lentoasema ei ole sanakirjassa, siis tulostetaan WRONG_INPUT
        elif choice == "3":
            print("Nähään!!")  # Nähään!!!
            break
        else:  # Jos käyttäjä anna eri kuin 1, 2 tai 3 siis tulostetaan TRY_AGAIN ja toistetaan sovellus
            print("TRY_AGAIN")
            lentoasema_sovellus()  # Toista sovellus uudellen


# Pääohjelma
lentoasemat = dict()  # Lentoasemien tietokanta

lentoasema_sovellus()  # Alku- ja loppusijanti
