#kordinaattipisteet ja funktiot

import math

def koordinaatti(x,y):
    return (x,y)

def etaisyys(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#kysytään pisteet

x1 = int(input("Anna ensimmäisen koordinaatin x-arvo: "))
y1 = int(input("Anna ensimmäisen koordinaatin y-arvo: "))
p1 = koordinaatti(x1,y1)

x2 = int(input("Anna toisen koordinaatin x-arvo: "))
y2 = int(input("Anna toisen koordinaatin y-arvo: "))
p2 = koordinaatti(x2,y2)

#lasketaan etäisyys
e = etaisyys(p1,p2)

print("Pisteiden välinen etäisyys on", e)
