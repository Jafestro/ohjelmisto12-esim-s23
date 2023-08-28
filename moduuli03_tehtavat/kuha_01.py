# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha_sm = int(input("Kirjoita kuhan pituuden senttimetreinä: "))

if kuha_sm <= 37:
    print("Kuha on alamittainen palauta kuha takaisin järveen")
else:
    print("Voit otta kuhan, se ei oo alamittainen, eli bon appetite! :D")
