#kysytään käyttäjältä nimiä ja lisätään listaan

nimet = set()

while True:
    nimi = input("Anna jokin nimi (tyhjä lopettaa): ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Nimi on jo listassa.")

    else:
        print("Uusi nimi, lisätään listaan.")
        nimet.add(nimi)
print("Syötetyt nimet: ", nimet)
