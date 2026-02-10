# in questo script ci concentreremo nel chiedere due input all'utente e calcolare l'età futura 

#creato variabili con conversione degli input

nome = str(input("Come ti chiami??  "))
eta = int(input("Quanti anni hai??  ")) 
anno = int(input("Fra quanti anni vuoi calcolare la tua età??  "))
calcolo = int(eta + anno)

print(f"Ciao {nome}, complimenti per i tuoi {eta} anni.") 
print(f"Fra {anno} anni, avrai {calcolo} anni")


# miglioramento possibile futuro la gestione degli errori