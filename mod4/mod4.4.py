import random

luku = random.randint(1,10)
arvaus = int(input("Arvaa luku 1-10 väliltä: "))

while True:
    if arvaus == luku:
        print("Oikein!")
        break

    if arvaus < luku:
        print("Liian pieni!")

    if arvaus > luku:
        print("Liian iso!")

    arvaus = int(input("Kokeile uudelleen: "))2

