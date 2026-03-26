def plus(a,b):
    return a+b
def miinus(a,b):
    return a-b
def jako(a,b):
    if b == 0:
        return "Virhe: ei voida jakaa 0!"
    return a/b
def kerto(a,b):
    return a*b

#laskin
while True:
    print("Laskimessa on laskutoimitukset: plus/miinus/jako/kerto (loppu sulkee ohjelman)")

    laskutoimitus = input("Kerro haluamasi laskutoimitus: ")
    if laskutoimitus == "loppu":
        break

    a = float(input("Anna ensimmäinen lukusi: "))
    b = float(input("Anna toinen lukusi: "))

    if laskutoimitus == "plus":
            print("Lukujen summa on: ", plus(a,b))

    elif laskutoimitus == "miinus":
            print("Lukujen erotus on: ", miinus(a,b))

    elif laskutoimitus == "jako":
            print("Lukujen osamäärä on: ", jako(a,b))

    elif laskutoimitus == "kerto":
            print("Lukujen tulo on: ", kerto(a,b))

    else:
        print("Lopetetaan...")

