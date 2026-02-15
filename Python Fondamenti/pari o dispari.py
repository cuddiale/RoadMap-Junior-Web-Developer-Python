# programma che chiede all'utente di inserire un numero e dirà se quel numero è pari o dispari.

while True:

    numero = int(input("Inserisci un numero e ti dirò se è pari o dispari: "))

    if numero % 2 == 0:
        print(f"il {numero} è pari \n")
        
    else:
        print(f"il {numero} è dispari \n")
        