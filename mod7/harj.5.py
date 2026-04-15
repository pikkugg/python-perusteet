#sanakirja malli, puhelinnumerolista

numerot = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"
           }

numerot["Olga"] = "044-123458"

for nimi in numerot:
    print(f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}")
