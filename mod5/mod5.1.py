import random

nopat = int(input("Kuinka montaa noppaa heitetään?"))

summa = 0
for noppa in range(nopat):
    heitto = random.randint(1,6)
    print(heitto)
    summa +=heitto

print("Silmälukujen summa on ", summa)