#funktio jonka parametrinä lista kokonaislukuja, ohjelma antaa listan lukujen summan

def laske_summa(kokonaisluvut):
    kokonaissumma = 0

    for luku in kokonaisluvut:
        kokonaissumma += luku
    return kokonaissumma

luvut = [4,8,10,19,20,1]
tulos = laske_summa(luvut)

print(f"Lukujen summa on: {tulos}")
