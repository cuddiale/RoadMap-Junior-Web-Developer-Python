# in base all'input dell'utente verificare se password coincide

# stampare Numero pari/dispari
# stampare Maggiore/minore

password = input("Inserisci la tua Password: ")
ripeti = input("Inserisci la tua Password: ")

if password == ripeti:
    print("La password è CORRETTA, procediamo!")
    numero = int(input("inserisci un numero e ti dirò se pari o dispari."))
    
    if numero % 2 == 0:
     print(f"Il numero {numero} è PARI")
     
    else:
     print(f"Il numero {numero} è DISPARI")
     
    numero2 = int(input("inserisci un secondo numero e ti dirò quale dei due è maggiore dell'altro."))
    
    if numero > numero2 :
        print(f"{numero} è maggiore di {numero2}!")
        
    elif numero == numero2:
        print(f"I due numeri sono uguali!")
        
    else:
        print(f"il {numero2} è maggiore di {numero}!")     
    
     
         
else:
    print("La password è SBAGLIATA.")
    

#più avanti con i loop ed eccezioni si può modificare
    




