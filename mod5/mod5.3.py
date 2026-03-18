kokonaisluku = int(input("Anna kokonaisluku: "))

alkuluku = True

if kokonaisluku <= 1:
    alkuluku = False

else:
    for luku in range (2,kokonaisluku):
        if kokonaisluku % luku == 0:
            alkuluku = False
            break

if alkuluku:
    print("Luku on alkuluku")

else:
    print("Luku ei ole alkuluku.")