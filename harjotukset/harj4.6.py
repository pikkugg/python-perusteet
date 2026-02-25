kasky = input("Annetaanko lisää rahaa (ei lopettaa)?")

while kasky != "ei":
    if kasky == "Ryöstö!":
        print("Kaikki rahat viety!")
        break
    print("Annettu kolikko lisää")
    kasky = input("Annetaanko lisää rahaa (ei lopettaa)?")
else:
    print("Hyvästi!")

print("Ohjelma loppuu")


