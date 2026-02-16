'''Argomenti

    Dizionari
    Chiave / valore
    get(), keys(), values()
'''

# Dizionario Utente

utente = {
    "username": "mario123",
    "email": "mario@email.com",
    "attivo": True
}

print("Username:", utente["username"])
print("Email:", utente["email"])

utente["eta"] = 30
utente["email"] = "nuova@email.com"


# Accesso ai dati con ciclo

for chiave, valore in utente.items():
    print(chiave, ":", valore)


# Task: Rubrica Contatti (in memoria)

rubrica = {}

rubrica["Mario"] = "3331234567"
rubrica["Luca"] = "3399876543"

print("Rubrica:", rubrica)

nome = "Mario"
print("Numero di", nome, ":", rubrica.get(nome))


# Versione Interattiva

rubrica = {}

while True:
    scelta = input("1) Aggiungi  2) Cerca  3) Esci: ")
    
    if scelta == "1":
        nome = input("Nome: ")
        numero = input("Numero: ")
        rubrica[nome] = numero
        
    elif scelta == "2":
        nome = input("Nome da cercare: ")
        numero = rubrica.get(nome, "Contatto non trovato")
        print(numero)
        
    elif scelta == "3":
        break

