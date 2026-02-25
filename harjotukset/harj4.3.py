kuha = int(input("Kuinka suuren kuhan sait? "))

while kuha > 0:
    if kuha < 37:
        puutos = 37 - kuha
        print("Kuhasi oli", puutos, "senttiä liian lyhyt.")
    else:
        print("Hieno kuha!")

    kuha = int(input("Kuinka suuren kuhan sait? "))

print("Lopetetaan...!")
