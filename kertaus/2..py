tuntipalkka = float(input("Tuntipalkka: "))
tunnit = float(input("Tehdyt tunnit: "))
paiva = input("Viikonpäivä: ")

if paiva == "sunnuntai":
    palkka = 2 * tuntipalkka * tunnit

else:
    palkka = tuntipalkka * tunnit

print("Päiväpalkka on ", palkka, "euroa")