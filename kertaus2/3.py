#lasketaan sanojen pituus, yli 5 kirjaimen sanat

sanat = ["kukka", "aurinko", "sateenvarjo", "marja", "kevät", "vappu", "koira", "pääsiäinen"]

lista = 0

for s in sanat:
    if len(s) > 5:
        lista+=1

print("Yli 5 kirjaimen sanoja on: ", lista)


