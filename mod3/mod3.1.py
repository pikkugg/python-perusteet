pituus = float(input("kuinka pitkä kuha on?"))
if  pituus <  37:
    print("kuha on alamittainen")
    print(f"{37 - pituus}cm alle sallitun pituuden")

else:
    print("kuha on sopivan mittainen, voit pitää sen!")
