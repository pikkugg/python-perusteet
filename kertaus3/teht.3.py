#sanakirja kirjoistaa

kirjasto = {"Harry Potter" : ["J.K Rowling", 2010, "fantasia"],
            "ABC-kirja" : ["Micael Agricola", 1800, "oppikirja"],
            }

print("Harry Potterin on kirjoittanut", kirjasto["Harry Potter"][0])
print("ABC-kirjan genre on", kirjasto["ABC-kirja"][2])

#vaihdetaan genre
kirjasto["ABC-kirja"][2] = "tietokirja"

#lisätään uusi kirja
kirjasto ["Runokirja"] = ["Eino Leino", 1950, "kaunokirjallisuus"]

#poistetaan yksi kirja
del kirjasto["Harry Potter"]

#tulostetaan koko sanakirja
for k in kirjasto:
    print(f"Kirjailija: {kirjasto[k][0]}")
    print(f"Julkaisuvuosi: {kirjasto[k][1]}")
    print(f"Genre: {kirjasto[k][2]}")