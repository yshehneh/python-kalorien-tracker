
essen_liste = []
kalorien_summe = 0

print("Hallo \nDieses kleine Programm hilft dir, deinen BMI und deine tägliche Kalorienmenge besser einzuschätzen.\n")
print("Dafür brauchen wir zuerst ein paar Informationen von dir.\n")


while True:
    try:
        groesse_cm = int(input("Bitte gib deine Körpergröße in cm ein: "))
        if groesse_cm < 150 or groesse_cm > 210:
            print("Größe unrealistisch.")
            continue

        gewicht = float(input("Bitte gib dein aktuelles Gewicht in kg ein: "))
        if gewicht < 30 or gewicht > 210:
            print("Gewicht unrealistisch.")
            continue

        break
    except:
        print("Bitte nur Zahlen eingeben.")


groesse_m = groesse_cm / 100
bmi = gewicht / (groesse_m ** 2)

if bmi < 18.5:
    status = "Untergewicht"
    kalorien_ziel = 2500
elif bmi < 25:
    status = "Normalgewicht"
    kalorien_ziel = 2200
elif bmi < 30:
    status = "Übergewicht"
    kalorien_ziel = 2000
else:
    status = "Adipositas"
    kalorien_ziel = 1800

print("\nErgebnis deiner Berechnung:")
print(f"- Dein BMI liegt bei: {bmi:.1f}")
print(f"- Einschätzung: {status}")
print(f"- Empfohlene tägliche Kalorienmenge: {kalorien_ziel} kcal")


while True:
    print("""
=========================
        HAUPTMENÜ
=========================
[1] Gegessenes Essen eintragen
[2] Tagesübersicht anzeigen
[3] Persönliche Daten ändern
[4] Neuer Tag (alles zurücksetzen)
[5] Programm beenden
=========================
""")

    wahl = input("Deine Wahl: ")

    
    if wahl == "1":
        try:
            name = input("Was hast du gegessen? ")
            kcal = int(input("Kalorien: "))
            essen_liste.append(f"{name} ({kcal} kcal)")
            kalorien_summe += kcal
            print("Essen wurde erfolgreich gespeichert.")
        except:
            print("Ungültige Eingabe.")

    
    elif wahl == "2":
        print("\n===== TAGESÜBERSICHT =====")
        print(f"Kalorienziel für heute: {kalorien_ziel} kcal")
        print(f"Bisher aufgenommen: {kalorien_summe} kcal")

        rest = kalorien_ziel - kalorien_summe
        prozent = (kalorien_summe / kalorien_ziel) * 100

        if rest >= 0:
            print(f"Übrig: {rest} kcal")
        else:
            print(f"Zu viel: {-rest} kcal")
            print("Achtung: Du hast dein tägliches Kalorienziel überschritten!")

        print(f"Verbrauch: {prozent:.1f}%")

        if essen_liste:
            print("\nGegessen:")
            for e in essen_liste:
                print("-", e)
        else:
            print("\nNoch kein Essen eingetragen.")

        print("===================")

    
    elif wahl == "3":
        while True:
            try:
                groesse_cm = int(input("Neue Größe in cm: "))
                if groesse_cm < 150 or groesse_cm > 210:
                    print("Größe unrealistisch.")
                    continue

                gewicht = float(input("Neues Gewicht in kg: "))
                if gewicht < 30 or gewicht > 210:
                    print("Gewicht unrealistisch.")
                    continue

                break
            except:
                print("Bitte nur Zahlen eingeben.")

        groesse_m = groesse_cm / 100
        bmi = gewicht / (groesse_m ** 2)

        if bmi < 18.5:
            status = "Untergewicht"
            kalorien_ziel = 2500
        elif bmi < 25:
            status = "Normalgewicht"
            kalorien_ziel = 2200
        elif bmi < 30:
            status = "Übergewicht"
            kalorien_ziel = 2000
        else:
            status = "Adipositas"
            kalorien_ziel = 1800

        print("\nDaten aktualisiert.")
        print(f"Neuer BMI: {bmi:.1f}")
        print(f"Neuer Status: {status}")
        print(f"Neues Kalorienziel: {kalorien_ziel} kcal")

    
    elif wahl == "4":
        essen_liste = []
        kalorien_summe = 0
        print("Ein neuer Tag wurde gestartet. Alle Tagesdaten wurden zurückgesetzt.")

    
    elif wahl == "5":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Auswahl.")
