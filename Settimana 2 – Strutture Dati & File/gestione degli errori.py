while True:
    try:
        numero = int(input("Inserisci un numero: "))
        print("Hai inserito:", numero)
        break
    except ValueError:
        print("Errore, inserisci un numero valido.")
