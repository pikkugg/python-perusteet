kerroin = 2.54


while True:
    tuumat = float(input("Anna jokin tuumamäärä niin muutan sen senteiksi (negatiivinen lopettaa): "))
    if tuumat < 0:
        print("Ei onnistu, ohjelma loppuu...")
        break
    sentit = kerroin * tuumat
    print(tuumat, "tuumaa on ", sentit, "cm")

