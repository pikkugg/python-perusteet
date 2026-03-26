#tehdään listat pyydetyistä numeroista

luvut = []

while True:
    luku = int(input("Anna jokin luku (0 lopettaa): "))
    if luku == 0:
        break

    luvut.append(luku)
    print("Numerot lisäysjärjestyksessä: ", luvut)
    print("Numerot pienimmästä alkaen: ", sorted(luvut))