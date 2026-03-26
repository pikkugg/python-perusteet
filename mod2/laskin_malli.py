print("TERVETULOA KÄYTTÄMÄÄN LASKINTA!")

while True:
    print("\nValitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku \n C: Kertolasku"
          "\n D: Jakolasku")

    valinta = input("Valintasi (A-D, Q lopettaa): ")

    if valinta == "Q":
        print("Ohjelma lopetetaan.")
        break

    a = float(input("Anna eka luku: "))
    b = float(input("Anna toka luku: "))

    if valinta == "A":
        print("Lukujen summa on:", a+b)
    elif valinta == "B":
        print("Lukujen erotus on:", a-b)
    elif valinta == "C":
        print("Lukujen tulo on:", a*b)
    elif valinta == "D":
        print("Lukujen osamäärä on:", a/b)
    else:
        print("Virheellinen valinta tai luku.")