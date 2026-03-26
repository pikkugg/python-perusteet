#kysytään kolme lukua ja tulostetaan niistä suurin

def suurin_arvo(a,b,c):
    suurin = a
    if b > suurin:
        suurin = b
    if c > suurin:
        suurin = c
    return suurin

#pääohjelma

x = int(input("Anna eka luku: "))
y = int(input("Anna toinen luku: "))
z = int(input("Anna kolmas luku: "))

tulos = suurin_arvo(x, y, z)
print("Suurin arvo on:", tulos)