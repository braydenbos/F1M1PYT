import time
print("Je bent net wakker en je hebt al je eerste keuze")
time.sleep(1.0)
print("De eerste keuze die je moet maken is of je sap gaat drinken of thee")
time.sleep(1.0)
drinken = input("Type THEE of SAP: ")
if drinken == 'THEE':
    print("Je begint thee te maken")
    print("Maar hier is al je tweede keuze")
    print("Wat doe je in de thee honing, suiker of niks")
    time.sleep(1.0)
    Thee = input("Type HONING, SUIKER of NIKS: ")
    if Thee == 'HONING':
        print("Je doet honig in de thee")
        time.sleep(1.0)
    elif Thee == 'SUIKER':
        print("Je doet een beetje suiker in je thee")
        time.sleep(1.0)
    elif Thee == 'NIKS':
        print("Je deed niks in je thee maar het smaakt nog steeds goed")
        time.sleep(1.0)
    else:
        print("Je wist niet wat je wou dus je deed honing en suiker")
        time.sleep(1.0)
        print("Het was een beetje te zoet")
        time.sleep(1.0)
elif drinken == 'SAP':
    print("Je gaat wat sap pakken")
    print("Maar wat voor sap wordt het?")
    time.sleep(1.0)
    Sap = input("Type SINAS, APPEL of GRAS: ")
    if Sap == 'SINAS':
        print("Je schonk voor je zelf een glas sinasappelsap")
    elif Sap == 'APPEL':
        print("Je schonk een vers glas appelsap")
    elif Sap == 'GRAS':
        print("-_- WaT??")
    else:
        print("Je wist niet wat voor sap dus dan maar alle 3")
        time.sleep(1.0)
        print("o_O het smaakt interesant")
else:
    print("Je wist niet wat je wou dus je maakte maar koffie")
time.sleep(1.0)
print("Nudat je wat hebt gedronken ga je iets eten")
print("Maar waar heb je zin in")
eten = input("Type BROOD, CORNFLAKES of LEFTOVERS: ")
if eten == 'BROOD':
    print("Je eet een broodje kaas")
elif eten == 'CORNFLAKES':
    print("Je eet een hele bak cornflakes")
elif eten == 'LEFTOVERS':
    print("je eet een hele pizza")
else:
    print("Jet was zo een moeilijke vraag dat je niet kon kieze")
    time.sleep(1.0)
    print("Dus je at alles in je koelkast")
time.sleep(1.0)
print("Nadat je wat hebt gegeten denk je")
print("Het is het weekend dus wat ga ik nu doen")
doen = input("Type WERKEN, GAMEN of NIKSEN: ")
if doen == 'WERKEN':
    print("Je hebt het hele weekend gewerked en je ben heel productief geweest")
elif doen == 'GAMEN':
    print("Je bet gaan gamen want soms moet je iets voor je zelf doen")
elif doen == 'NIKSEN':
    print("Je hebt de hele dag niks gedaan")
    print("Heel productief")
else:
    print("Je wist niet wat je wou doen dus je ging je vrienden bellen")
time.sleep(1.0)
print("Je weekend is voorbij en morgen heb je weer school")
print("Wat ga je doen voordat je gaat slapen")
slapen = input("Type YOUTUBE of ZZZ: ")
if slapen == 'ZZZ':
    print("Je ging vroeg slapen en werd uitgerust wakker")
elif slapen == 'YOUTUBE':
    print("je zocht de hele nacht youtube videos op en sliep niet")
print("dat was het einde dit waren jouw keuzens")
time.sleep(2.0)
print("Drinken = " + drinken)
time.sleep(1.0)

if drinken == 'THEE':
    print("In je Thee had je = "+ Thee)
    time.sleep(1.0)
elif drinken == 'SAP':
    print("Je sap keuze was = "+ Sap)
    time.sleep(1.0)
print("Eten = " + eten)
time.sleep(1.0)
print("tijdends het weekend = " + doen)
time.sleep(1.0)
print("voor het slapen = " + slapen)
time.sleep(1.0)