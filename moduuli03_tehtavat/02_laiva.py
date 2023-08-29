hyttiluoka = input("Syötä laivan hyttiluoka:   (LUX, A, B, C) ")

if hyttiluoka.upper() == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluoka.upper() == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluoka.upper() == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluoka.upper() == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")
