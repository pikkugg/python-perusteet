sukupuoli = input("Mikä on sinun biologinen sukupolesi? ")
hemoglobiini = int(input("mikä on hemoglobiiniarvosi? "))

if sukupuoli == "nainen":
        if hemoglobiini < 117:
            print("Hemoglobiinisi on alhainen")
        elif 117 <= hemoglobiini <= 175:
            print("Hemoglobiinisi on normaaali")
        else:
            print("hemoglobiinisi on korkea")

if sukupuoli == "mies":
        if hemoglobiini < 134:
            print("Hemoglobiinisi on alhainen")
        elif 134 <= hemoglobiini <= 195:
            print("Hemoglobiinisi on normaaali")
        else:
            print("hemoglobiinisi on korkea")
