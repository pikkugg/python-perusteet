vuosi = int(input("anna vuosiluku: "))

if vuosi % 4 == 0:
    print("Kyseessä on karkausvuosi")
elif vuosi % 100 == 0:
    print("Kyseessä ei ole karkausvuosi")
elif vuosi % 4 == 0:
    print("Kyseessä on karkausvuosi")
else:
    print("Kyseessä ei ole karkausvuosi")