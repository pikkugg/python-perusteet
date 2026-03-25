def inventaario(tavarat):
    print("Sinulla on nämä tavarat repussa: ")
    for t in tavarat:
        print("- " + t)
    tavarat.clear()
    return


#pääohjelmassa
reppu = ["taskulamppu", "otsalamppu", "pöytälamppu"]
inventaario(reppu)

reppu.append("eväsleipä")
inventaario(reppu)
