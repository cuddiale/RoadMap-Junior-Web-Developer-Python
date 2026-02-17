# Gestione input errato
# File mancante


# Gestione input errato

while True:
    try:
        eta = int(input("Inserisci età: "))
        break
    except ValueError:
        print("Devi inserire un numero valido!")


import json

#Caricamento sicuro file
try:
    with open("rubrica.json", "r") as file:
        rubrica = json.load(file)
except FileNotFoundError:
    rubrica = {}
    print("File non trovato. Creata nuova rubrica.")

#Inserimento contatti con controllo input
while True:
    nome = input("Inserisci nome (o 'fine'): ")
    
    if nome.lower() == "fine":
        break
    
    if nome.strip() == "":
        print("Il nome non può essere vuoto!")
        continue
    
    telefono = input("Inserisci numero: ")
    
    if not telefono.isdigit():
        print("Il numero deve contenere solo cifre!")
        continue
    
    rubrica[nome] = telefono

#Salvataggio sicuro
try:
    with open("rubrica.json", "w") as file:
        json.dump(rubrica, file, indent=4)
    print("Rubrica salvata correttamente!")
except Exception as e:
    print("Errore durante il salvataggio:", e)
