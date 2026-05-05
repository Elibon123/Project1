#Task manager
#from src.knihovna import zobrazit_knihy
ukoly = []
def hlavni_menu():
    print("Spravce ukolu - Hlavni menu")
    print("1. Pridat novy ukol")
    print("2. Zobrazit vsechny ukoly")
    print("3. Odstranit ukol")
    print("4. Konec programu")

    moznost = input("Vyberte moznost (1-4): ").strip()  
    while True:
        if moznost == "1":
            pridat_ukol()
        elif moznost == "2":
            zobrazit_ukoly()
        elif moznost == "3":
            odstranit_ukol()
        elif moznost == "4":
            print("Konec programu.")
        else:
            moznost = input(f"Neplatnou volbu. Vyberte moznost (1-4): ")

#if __name__ == "__main__":
##    conn = pripojeni_k_databazi()
#    if conn:
#        vytvoreni_tabulky(conn)
#        vytvor_data(conn)

#conn.close()

def pridat_ukol():
    while True:
        nazev_ukolu = input("Zadejte nazev ukolu: ")
        popis_ukolu = input("Zadejte popis ukolu: ")
        kontrola_nazvu = len(nazev_ukolu)
        kontrola_popisu = len(popis_ukolu)
        if kontrola_nazvu == 0:
            print("Zadan je prazdny nazev")
        elif kontrola_popisu == 0:
            print("Zadan je prazdny popis")
        else:
            number = len(ukoly) + 1
            ukoly.append({"number": number, "nazev": nazev_ukolu, "popis": popis_ukolu})
            print(f"Ukol '{nazev_ukolu}' byl pridan!")
            hlavni_menu()
            break

def zobrazit_ukoly():
        for ukol in ukoly:
            print("Seznam ukolu:")
            print(f"{ukol['number']}. {ukol['nazev']} - {ukol['popis']}")
            hlavni_menu()
            break


def odstranit_ukol():
    if not ukoly:
        print("Zadne ukoly nejsou k dispozici k odstraneni.")
    else:
        print("Seznam ukolu:")
        for ukol in ukoly:
            print(f"{ukol['number']}. {ukol['nazev']} - {ukol['popis']}")
        while True:
                volba = int(input("Zadejte cislo ukolu, ktery chcete odstranit: "))
                if 1 <= volba <= len(ukoly):
                    odstraneny_ukol = ukoly.pop(volba - 1)
                    print(f"Ukol '{odstraneny_ukol['nazev']}' byl odstraněn!")
                    hlavni_menu()
                    break
                else:
                    print(f"Neplatna volba. Zadejte cislo mezi 1 a {len(ukoly)}.")

hlavni_menu()


