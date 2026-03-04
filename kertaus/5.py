laskutoimitus = input("Kerro haluamasi laskutoimitus: plus/miinus/jako/kerto (loppu lopettaa ohjelman): ")

if laskutoimitus != "loppu":
    luku1 = float(input("Anna ensimmäinen lukusi: "))
    luku2 = float(input("Anna toinen lukusi: "))

    while True:
        if laskutoimitus == "plus":
            print(luku1 + luku2)

        elif laskutoimitus == "miinus":
            print(luku1 - luku2)

        elif laskutoimitus == "jako":
            print(luku1 / luku2)

        elif laskutoimitus == "kerto":
            print(luku1 * luku2)

        else:
            print("Lopetetaan...")
            break

        laskutoimitus = input("Kerro haluamasi laskutoimitus: ")
        if laskutoimitus == "loppu":
            break

        luku1 = float(input("Anna ensimmäinen lukusi: "))
        luku2 = float(input("Anna toinen lukusi:"))

print("Lopetetaan ohjelma...")