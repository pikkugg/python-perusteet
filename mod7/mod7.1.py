## kysytään kuukauden numero, sen jälkeen kerrotaan mikä vuodenaika

#talvi: 12, 1, 2
#kevät: 3, 4, 5
#kesä: 6, 7, 8
#syksy: 9, 10,11

vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kuukausi = int(input("Anna kuukauden numero 1-12: "))


if kuukausi <= 2 or kuukausi == 12:
    print("Vuodenaika on", vuodenajat[0])

elif kuukausi <=5:
    print("Vuodenaika on", vuodenajat[1])

elif kuukausi <=8:
    print("Vuodenaika on", vuodenajat[2])

elif kuukausi <= 11:
    print("Vuodenaika on", vuodenajat[3])

else:
    print("Virheellinen numero!")

