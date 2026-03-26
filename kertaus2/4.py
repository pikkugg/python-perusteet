#tulostetaan kuusi

def kuusi(koko):
    print("Tämä on kuusi!")
    for i in range(1, koko + 1):
        valit = koko - i
        tahdet = 2 * i - 1
        print(" " * valit + "*" * tahdet)
    print(" " * (koko - 1) + "*")  # runko

# pääohjelma
k = int(input("Anna kuusen koko: "))
kuusi(k)


