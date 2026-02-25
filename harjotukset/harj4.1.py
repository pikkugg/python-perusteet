hinta = 5
kolikot = 0

while kolikot < 5:
    kolikot += 1
    print("Annettu", kolikot, "euroa")

print("Kahvi maksettu!")

--------

while True:
    kolikot += 1
    print("Annettu", kolikot, "euroa")
    if kolikot == hinta:
        break

print("Kahvi maksettu!")

##pitää käyttää vain jompaa kumpaa, tilttaa jos on molemmat while
