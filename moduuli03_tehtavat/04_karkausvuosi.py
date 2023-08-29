vuosi = int(input("Anna jonkun vuosi ja tää ohjelma tsekata jos tää vuosi on karkausvuosi tai ei: "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0 and vuosi % 100 == 0):
    print(f"{vuosi} on karkaus vuosi")
else:
    print(f"{vuosi} ei oo karkausvuosi")
