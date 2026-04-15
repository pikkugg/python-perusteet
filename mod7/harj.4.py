#joukkorakenne pelit

pelit = {"matopeli", "minecraft", "clash royale"}
print(pelit)

pelit.add("world of warcraft")
print(pelit)

pelit.remove("matopeli")
print(pelit)

for p in pelit:
    print(p)