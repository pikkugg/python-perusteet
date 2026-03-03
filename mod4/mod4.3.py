ensimmainen = input("Anna jokin luku (tyhjä lopettaa) ")

if ensimmainen == "":
    print("Lopetetaan, et antanut yhtään lukua...")
else:
    luku = int(ensimmainen)
    pienin = luku
    suurin = luku

while True:
    kasky = input("Anna jokin luku (tyhjä lopettaa)")
    if kasky == "":
        break

    luku = int(kasky)

    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku
print("Pienin luku: ", pienin)
print("Suurin luku; ", suurin)





