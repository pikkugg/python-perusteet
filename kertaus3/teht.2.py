#tehdään sanakirja oppilaista

oppilaat = {"Saulus" : ["Saulus", 1, "matikka"],
            "Valto" : ["Valto", 3, "fysiikka"],
            "Miko" : ["Miko", 4, "ruotsi"]
            }

#tulostetaan jonkun opplaan vuosiluokka ja jonkun lempiaine
print("Sauluksen vuosiluokka on", oppilaat["Saulus"][1])
print("Valton lempiaine on",  oppilaat["Valto"][2])

#muokataan
oppilaat ["Valto"][2]  = "kuvataide"

#lisätään uusi oppilas
oppilaat ["Fanny"]  = ["Fanny", 3, "näyttelykerho"]

#poistetaan oppilas
del oppilaat["Saulus"]

#tulostetaan koko sanakirja
for o in oppilaat:
    print(f"Nimi: {oppilaat[o][0]}")
    print(f"Vuosiluokka: {oppilaat[o][1]}")
    print(f"Lempiaine: {oppilaat[o][2]}")