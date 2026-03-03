oikea_tunnus = "python"
oikea_salasana = "rules"
yritykset = 0
maksimi = 5

while yritykset < maksimi:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break

    else:
        yritykset += 1
        print("Väärä tunnus tai salasana")

if yritykset == maksimi:
    print("Pääsy evätty.")
