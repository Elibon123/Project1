#Task manager
#Funkce hlavni_menu zobrazuje hlavni menu spravce ukolu a poskytuje uzivateli moznosti 
# pridat, zobrazit nebo odstranit ukoly, nebo ukoncit program.
def hlavni_menu():
    ukoly = []
    while True:
        print("Spravce ukolu - Hlavni menu")
        print("1. Pridat novy ukol")
        print("2. Zobrazit vsechny ukoly")
        print("3. Odstranit ukol")
        print("4. Konec programu")

        moznost = input("Vyberte moznost (1-4): ").strip()  
        if moznost == "1":
            pridat_ukol(ukoly)
        elif moznost == "2":
            zobrazit_ukoly(ukoly)
        elif moznost == "3":
            odstranit_ukol(ukoly)
        elif moznost == "4":
            print("Konec programu.")
            break
        else:
            print(f"Neplatnou volbu. Vyberte moznost (1-4): ")



#Funkce pridava novy ukol do seznamu ukolu, 
# pokud je nazev nebo popis prazdny, vypise hlasku "Zadan je prazdny nazev" 
# nebo "Zadan je prazdny popis" 
def pridat_ukol(ukoly):
    while True:
        nazev_ukolu = input("Zadejte nazev ukolu: ").strip()
        popis_ukolu = input("Zadejte popis ukolu: ").strip()
        kontrola_nazvu = len(nazev_ukolu)
        kontrola_popisu = len(popis_ukolu)
        if kontrola_nazvu == 0:
            print("Zadan je prazdny nazev")
        elif kontrola_popisu == 0:
            print("Zadan je prazdny popis")
        else:
            cislo = len(ukoly) + 1
            ukoly.append({"cislo": cislo, "nazev": nazev_ukolu, "popis": popis_ukolu})
            print(f"Ukol '{nazev_ukolu}' byl pridan!")
            break

#Funkce zobrazuje seznam ukolu, pokud nejsou zadne ukoly, vypise hlasku "Zadne ukoly"
def zobrazit_ukoly(ukoly):
    if not ukoly:
        print("Zadne ukoly")
    else:
        print("Seznam ukolu:")
        for cislo, ukol in enumerate(ukoly, 1):
            print(f"{cislo}. {ukol['nazev']} - {ukol['popis']}")



#Funkce odstranuje ukol podle zadaneho cisla
def odstranit_ukol(ukoly):
    if not ukoly:
        print("Zadne ukoly nejsou k dispozici k odstraneni.")
    else:
        print("Seznam ukolu:")
        for cislo, ukol in enumerate(ukoly, 1):
            print(f"{cislo}. {ukol['nazev']} - {ukol['popis']}")
        while True:
            volba = int(input("Zadejte cislo ukolu, ktery chcete odstranit: "))
            if 1 <= volba <= len(ukoly):
                odstraneny_ukol = ukoly.pop(volba - 1)
                print(f"Ukol '{odstraneny_ukol['nazev']}' byl odstraněn!")
                break
            else:
                print(f"Neplatna volba. Zadejte cislo mezi 1 a {len(ukoly)}.")

hlavni_menu()


