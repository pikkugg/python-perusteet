#muokataan listasta pois parittomat luvut

def luvut(kokonaisluvut):
    parilliset = []
    for luku in kokonaisluvut:
        if luku % 2 == 0:
            parilliset.append(luku)

    return parilliset

kokonaisluvut = [2,3,7,8,9,10]
_parilliset = luvut(kokonaisluvut)

print("Alkuperäinen lista: ", kokonaisluvut)
print("Vain parilliset luvut: ", _parilliset)

