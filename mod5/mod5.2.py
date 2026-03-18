luvut = []

while True:
    numero = (input("Anna luku (tyhjä lopettaa pelin): "))
    if numero == "":
        break
    luku = int(numero)
    luvut.append(luku)

luvut.sort(reverse=True)
print("Viisi suurinta lukua on: ")
for luku in luvut[0:5]:
    print(luku)




    


