#muunnaa gallonat litroiksi parametrien avulla


def muunnos(gallonat):
    litrat = gallonat * 3.785
    return litrat

gallonat = int(input("Kuinka monta gallonaa (negatiivinen lopettaa)?: "))
while gallonat >= 0:
    litrat = muunnos(gallonat)
    print("Sinulla on litroina: ", litrat)
    gallonat = int(input("Kuinka monta gallonaa (negatiivinen lopettaa)?: "))

print("Negatiivinen luku, lopetetaan")
