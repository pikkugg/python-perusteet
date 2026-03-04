from math import sqrt

while True:
    luku = int(input("Anna kokonaisluku: "))
    if luku < 0:
        print("Virheellinen numero!")
    elif luku == 0:
        print("Lopetetaan...")
        break

    else:
        print(sqrt(luku))
