#sanakirja nimillä

ihmiset  = {"John" : ["John", 30, "insinööri"],
"Emily" : ["Emily", 25, "artisti"],
"Anna" : ["Anna", 22, "oppilas"]
            }

print("John nimi on:", ihmiset["John"][0])
print("John ikä on:", ihmiset["John"][1])
print("Emilyn ammatti on", ihmiset["Emily"][2])

#muokataaan ammattia
ihmiset ["Anna"][2] = "opettaja"
print("Annan uusi ammatti on:", ihmiset["Anna"][2])

#lisätään James
ihmiset ["James"] = ["James", 28, "kirjoittaja"]
print ("Kuka on James?", ihmiset["James"])

#lisätään Sophia
ihmiset ["Sophia"] = ["Sophia",35, "lääkäri"]
print("Kuka on Sophia?", ihmiset["Sophia"])

del ihmiset["Emily"]

#tulostetaan koko sanakirja
for i in ihmiset:
    print(f"Nimi: {ihmiset[i][0]}")
    print(f"Ikä: {ihmiset[i][1]}")
    print(f"Ammatti: {ihmiset[i][2]}")







