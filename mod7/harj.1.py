my_list = [4,13,11,2,8,10,9]
tyhja_lista = []

#monikko rakenne

my_tuple = ("kevät", "kesä","syksy", "talvi")


#viikonpäivät esimerkki

viikko = ("ma","ti", "ke", "to", "pe","la", "su")
paiva = int(input("Anna viikonpäivän järjestysnumero (1-7): "))

vkpaiva = viikko[paiva -1]

print(f"Viikon {paiva}. päivä on {vkpaiva}")

#joukkorakenne
my_set = {"audi", "bmw", "nissan"}
tyhja_joukko = set()

#sanakirja

my_dictionary = {
    "Matti" : [2, 1, 4, 2, 1],
    "Pekka" : [4, 3, 2, 3, 4],
    "Teppo" : [0, 5, 4, 5]
}

