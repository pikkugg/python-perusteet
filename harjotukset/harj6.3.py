def neliosumma(a,b):
    _tulos = a**2 + b**2
    return _tulos

#pääohjelma

luku1 = float(input("anna ensimmäinen luku "))
luku2 = float(input("anna toinen luku "))
tulos = neliosumma(luku1, luku2)

print(f"Lukujen {luku1} ja {luku2} neliösumma on {tulos:.2f}.")
