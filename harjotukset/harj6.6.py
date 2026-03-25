def seven_brothers():
    veljekset.sort()
    print(veljekset)
    return

#pääohjelma
veljekset = ["Simo", "Lauri", "Timo", "Aapo", "Tuomas", "Eero", "Juhani"]
seven_brothers()


def eka_kirjain(sana):
    print(sana[0])
    return

#pääohjelma
eka_kirjain("python")
eka_kirjain("yellow")
eka_kirjain("tomorrow")
eka_kirjain("heliotrope")
eka_kirjain("open")
eka_kirjain("night")


def keskiarvo(a,b,c):
    _tulos = (a + b + c)/3
    return _tulos

#pääohjelma
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))
tulos = keskiarvo(luku1, luku2, luku3)

print(f"Lukujen {luku1} ja {luku2} ja {luku3} keskiarvo on {tulos:.2f}.")
