# creo le funzioni avvio / stop / pausa 

def avvio():
    print("Programma avviato")

def stop():
    print("Programma fermato")

def pausa():
    print("Programma in pausa") 


# utilizzo match 

scelta = input("Scegli un'opzione (start, stop, pausa): ")

match scelta:

    case "start":
        avvio()
        
    case "stop":
        
        stop()
    case "pausa":        
        pausa()
        
    case _:
        print("Comando non valido!")
        
# possibile upgrade implementare un ciclo, che ripete finchè l'utente non inserisce quello scelto
 
                
        

