biologisen_sukupuoli = input("Oletko biologisesti Nainen vai Mies?:   N/M    ")
hemoglobiiniarvo = int(input("Anna sinun hemoglobiiniarvo:   "))

if biologisen_sukupuoli.upper() == "M":
    if hemoglobiiniarvo < 134:
        print("hemoglobiiniarvo on alhainen")
    elif 134 <= hemoglobiiniarvo <= 195:
        print("hemoglobiiniarvo on normaali")
    elif hemoglobiiniarvo > 195:
        print("hemoglobiiniarvo on korkea")


elif biologisen_sukupuoli.upper() == "N":
    if hemoglobiiniarvo < 117:
        print("hemoglobiiniarvo on alhainen")
    elif 117 <= hemoglobiiniarvo <= 175:
        print("hemoglobiiniarvo on normaali")
    elif hemoglobiiniarvo > 175:
        print("hemoglobiiniarvo on korkea")
else:
    print("Anteeksi, mutta saa antaa vain N tai M")
