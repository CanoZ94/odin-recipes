  # Taschenrechner mit Wiederholungsschleife
while True:
     print("\n" + "="*30)
     print("NEUE RECHNUNG")
     print("="*30)
     zahl1 = float(input("Gib die erste Zahl ein:"))
     zahl2 = float(input("Gib die zweite Zahl ein:"))

     print("\nWähle eine Operation:")
     print("1 - Addition (+)")
     print("2 - Subtraktion (-)")
     print("3 - Multiplikation (*)")
     print("4 - Division (/)")
     print("5 - Programm beenden")

     operation = input("Deine Wahl (1/2/3/4/5)")

     if operation == "5":
        print("Programm wird beendet. Tschüss!")
        break

     if operation == "1":
        ergebnis = zahl1 + zahl2
        print(f"{zahl1} + {zahl2} = {ergebnis}")
     elif operation == "2":
        ergebnis = zahl1 - zahl2
        print(f"{zahl1} - {zahl2} = {ergebnis}")
     elif operation == "3":
        ergebnis = zahl1 * zahl2
        print(f"{zahl1} * {zahl2} = {ergebnis}")
     elif operation == "4":
         if zahl2 != 0:
            ergebnis = zahl1 / zahl2
            print(f"{zahl1} / {zahl2} = {ergebnis}")
         else:
            print("Fehler: Division durch Null ist nicht erlaubt!")
     else:
        print("Ungültige Eingabe! Bitte 1-5 wählen.")

input("Drücke Enter zum Beenden...")    