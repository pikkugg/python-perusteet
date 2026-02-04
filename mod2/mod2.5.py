leiviskat = int(input("kuinka monta leiviskää?: "))
naulat = int(input("kuinka monta naulaa?: "))
luodit = int(input("kuinka monta luotia?: "))

luotig = 13.3
naulaluot = 32
leiviskaluot = 640

kokonaisluodit = leiviskat * 640 + naulat * 32 + luodit

kokonaisgrammat = kokonaisluodit * 13.3
kilot = kokonaisgrammat // 1000
grammat = kokonaisgrammat % 1000

print(f"Massa olisi nykymitoissa {kilot}kg ja {grammat}g")
