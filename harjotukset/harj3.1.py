raha = float(input("kuinka paljon sinulla on rahaa? "))

if raha >= 5:
    print("voit ostaa kahvin!")
    print(f"saat takaisin {raha - 5} euroa")

print("kiitos hei!")

## toinen esimerkki

pituus = float(input("kuinka pitkä olet?"))

if 160 <= pituus < 180:
    print("olet samanmittainen kuin suurin osa!")
