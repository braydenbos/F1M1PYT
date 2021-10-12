import time

def berekenmaandkosten(km_per_maand):
    prijs=l * lpkm * km + verzekering
    print("Je hebt deze maand " +str(prijs)+ "€ aan scooters kosten bataald")
    return prijs

verzekering = "";

while not isinstance(verzekering, float):

    try:
        verzekering = input("Hoeveel geld geef je uit aan scooter verzekering je per maand?: ")
        
        verzekering = float(verzekering)

        print("Je betaald " + str(verzekering) + "€ aan scooter verzekering")
        time.sleep(1.0)


    except ValueError:
        print(verzekering + " is geen geldig getal!")

l = "";

while not isinstance(l, float):

    try:
        l = input("Hoeveel kost 1 liter benzine?: ")
        
        l = float(l)

        print("1 liter benzine kost " + str(l) + "€")
        time.sleep(1.0)

    except ValueError:
        print(l + " is geen geldig getal!")

lpkm = "";

while not isinstance(lpkm, float):

    try:
        lpkm = input("Hoeveel liter kost het om 1 kilometer te reizen?: ")
        
        lpkm = float(lpkm)

        print(str(lpkm) + " liter per kilometer")
        time.sleep(1.0)

    except ValueError:
        print(lpkm + " is geen geldig getal!")

km = "";

while not isinstance(km, float):

    try:
        km = input("Hoeveel kilometer rij je per maand?: ")
        
        km = float(km)

        print("Je hebt " + str(km) + " kilometer gereden")
        time.sleep(1.0)

    except ValueError:
        print(km + " is geen geldig getal!")
berekenmaandkosten(l * lpkm * km + verzekering)
time.sleep(1.0)