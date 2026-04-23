#lentoasematietojen haku ja syöttäminen

lentoasemat = {"EFHK" : "Helsinki-Vantaa",
               "EFHF" : "Malmin lentokenttä",
               "JHKY" : "Dubai"
}

while True:
    print("Valitse toiminto: 1 = SYÖTÄ, 2 = HAE, 0 = LOPETA")
    valinta = input("Valinta: ")

    if valinta == "0":
        print("Ohjelma loppuu.")
        break
    elif valinta == "1":
        icao = input("Anna lentokentän ICAO-koodi: ").upper()
        nimi = input("Anna lentokentän nimi: ")
        lentoasemat[icao] = nimi
        print("Uusi lentoasema lisätty luetteloon.")
    elif valinta == "2":
        icao = input("Anna lentoaseman ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoaseman nimi on: ", lentoasemat[icao])
        else:
            print("Koodilla ei löydy lentoasemaa.")
    else:
        print("Virheellinen valinta.")