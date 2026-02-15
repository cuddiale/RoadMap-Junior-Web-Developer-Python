
import unittest

# definisco le funzioni

# Funzione somma
# Funzione sottrazione
# Funzione prodotto
# Funzione divisione


def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return "Errore: non puoi dividere per zero!"
    return a / b


# creare ciclo infinito e scelta utente cosa vuole fare

while True:

    print("Seleziona operazione:")
    print("1 - Somma")
    print("2 - Sottrazione")
    print("3 - Moltiplicazione")
    print("4 - Divisione")
    print("0 - Uscire \n")

    scelta=str(input("Inserisci la tua scelta, [1] [2] [3] [4] per le operazioni oppure premi [0] per uscire. ")).lower
    
    if scelta == "1" or scelta == "2" or scelta == "3" or scelta == "4" or scelta == "0":
        numero = str(input("Inserisci il primo numero: "))
        numero_2 = str(input("Inserisci il secondo numero: "))
              
  
        if scelta == "0":
            uscita_loop = input("Confermi di uscire? Y o N ").lower()
                if uscita_loop == "y":    #inserito una doppia conferma per l'uscita
                    print("Il programma si sta chiudendo!")
                    print("Grazie per aver usato la calcolatrice!")
                    break   
                else:
                    continue     
                
        elif scelta == "1":
            print("Il risultato della somma è:",somma(numero, numero_2))
    
        elif scelta == "2":
            print("Il risultato della sottrazione è:",sottrazione(numero, numero_2))
         
        elif scelta == "3":
            print("Il risultato della moltiplicazizone è:",moltiplicazione(numero, numero_2))
         
        elif scelta == "4":
         print("Il risultato della divisione è:",divisione(numero, numero_2))

    else:
        print("Operazione non valida.")
        continue