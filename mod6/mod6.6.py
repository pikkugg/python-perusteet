#pizzan halkaisija ja hinta euroina parametrit, kysytään käyttäjältä kahden pizzan koko ja hinta

import math

def pizza_yksikkohinta(cm,eurot):
    r = cm / 2
    pinta_ala_cm = math.pi * (r**2)
    pinta_ala_m = pinta_ala_cm / 10000
    yksikkohinta = eurot / pinta_ala_m
    return yksikkohinta

print("Ensimmäisen pizzan koko ja hinta: ")
halkaisija1 = float(input("Halkaisija on (cm): "))
hinta1 = float(input("Hinta on (euroa): "))

print("Toisen pizzan koko ja hinta: ")
halkaisija2 = float(input("Halkaisija on (cm):"))
hinta2 = float(input("Hinta on (euroa): "))

yksikko1 = pizza_yksikkohinta(halkaisija1,hinta1)
yksikko2 = pizza_yksikkohinta(halkaisija2,hinta2)

if yksikko1 < yksikko2:
    print("Ensimmäinen pizza on enemmän vastinetta rahalle")
elif yksikko1 > yksikko2:
    print("Toka pizza on parempi vastike rahalle")
else:
    print("Pizzat ovat yhtä edukkaat")



