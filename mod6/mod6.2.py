#edellinen tehtävä, mutta parametrinä nopan tahkojen määrä ja noppaa heitetään kunnes saadaan max silmäluku

import random

def noppa(tahkot):
    tulos = random.randint(1, tahkot)
    return tulos

tahkot = int(input("Anna nopan tahkojen määrä: "))
print("Heitä noppaa kunnes saat maksimisilmäluvun")

luku  = 0
while luku != tahkot:
    luku = noppa(tahkot)
    if luku == tahkot:
        print(f"Sait {luku}, maksimisilmäluvun, lopetetaan!")
    else:
        print(f"Sait {luku}, heitä uudestaan")
