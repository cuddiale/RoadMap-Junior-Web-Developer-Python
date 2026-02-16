# programma che chiede all'utente di inserire un numero e dirà se quel numero è pari o dispari.

while True:

    # numero = int(input("Inserisci un numero e ti dirò se è pari o dispari: "))

    if ( numero := int(input("Inserisci un numero e ti dirò se è pari o dispari: "))) % 2 == 0:     #operatore tricheco
        print(f"il {numero} è pari \n")
        
    else:
        print(f"il {numero} è dispari \n")
        