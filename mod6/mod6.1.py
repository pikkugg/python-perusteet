#heitetään noppaa kunnes saadaan 6 (ilman parametrejä)

import random

def noppa():
    tulos = random.randint(1,6)
    return tulos

print("Heitä noppaa kunnes saat 6")
luku  = 0
while luku !=6:
    luku = noppa()
    if luku == 6:
        print(f"Sait 6, lopetetaan!")
    else:
        print(f"Sait {luku}, heitä uudestaan")


