#sanakirja hedelmistä ja hedelmien hinnoista

hedelmat = {"banaani" : 2.99,
            "omena" : 1.5,
            "päärynä" : 4.25,
            "mango" : 5.99
}

yhteishinta = 0

while True:
    hedelma = input("Anna jokin hedelmä, jonka hinnan haluat tarkistaa (tyhjä lopettaa): ").lower()

    if hedelma == "":
        print("Tilaus valmis...")
        break
    if hedelma in hedelmat:
        print(f"{hedelma}n kilohinta on {hedelmat[hedelma]}e/kg")
        yhteishinta += hedelmat[hedelma]
    else:
        print("Meillä ei valitettavasti ole tuota hedelmää varastossa.")
        uusi = input("Haluatko lisätä sen (K/E)?: ").upper()

        if uusi == "K":
            hinta = float(input(f"Anna hinta {hedelma}lle: "))
            hedelmat[hedelma] = hinta
            print(f"{hedelma} lisätty varastoon kilohinnalla {hinta}.")

print("Yhteishinta tilaukselle on", yhteishinta, "euroa")

for hedelma in hedelmat:
    print(f"Hedelmä: {hedelma}, hinta: {hedelmat[hedelma]}")
