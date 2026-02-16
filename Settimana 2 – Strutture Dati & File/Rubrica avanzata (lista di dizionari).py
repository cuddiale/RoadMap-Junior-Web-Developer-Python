'''Argomenti
Tuple
Liste di dizionari
Strutture nidificate'''


'''Coordinate (x,y)
Lista contatti
Task: Rubrica avanzata (lista di dizionari)'''


# Coordinate (x, y)

punto = (5, 8)

x = punto[0]
y = punto[1]

print("X:", x)
print("Y:", y)

# Liste di Dizionari

utenti = [
    {"nome": "Mario", "eta": 25},
    {"nome": "Luca", "eta": 30},
    {"nome": "Anna", "eta": 22}
]

print(utenti[0]["nome"])  # Mario

for utente in utenti:
    print(utente["nome"], "-", utente["eta"])
    
    
# Task: Rubrica Avanzata (Lista di Dizionari)
    
rubrica = []

while True:
    scelta = input("1) Aggiungi  2) Visualizza  3) Cerca  4) Esci: ")
    
    if scelta == "1":
        nome = input("Nome: ")
        telefono = input("Telefono: ")
        email = input("Email: ")
        
        contatto = {
            "nome": nome,
            "telefono": telefono,
            "email": email
        }
        
        rubrica.append(contatto)
    
    elif scelta == "2":
        for contatto in rubrica:
            print(contatto["nome"], "-", contatto["telefono"])
    
    elif scelta == "3":
        nome = input("Nome da cercare: ")
        for contatto in rubrica:
            if contatto["nome"] == nome:
                print("Telefono:", contatto["telefono"])
                print("Email:", contatto["email"])
    
    elif scelta == "4":
        break

