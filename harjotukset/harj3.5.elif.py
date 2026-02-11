ika = int(input("kuinka vanha olet?"))

if ika >= 65:
    print("olet eläkkeellä!")

elif ika >= 18:
    print("olet työikäinen!")

elif ika >= 7:
    print("olet kouluikäinen!")

else:
    print("olet pieni lapsi!")

numero = int(input("anna jokin luku: "))
if numero > 0:
    print("numero on positiivinen!")
elif numero < 0:
    print("numero on negatiivinen!")
else:
    print("annoit 0)")

luku = int(input("anna jokin luku: "))
if luku > 0:
    if luku % 2 == 0:
        print("luku on parillinen!")
    else:
        print("numero oli pariton!")
else:
    print("luku oli negatiivinen tai 0!")


