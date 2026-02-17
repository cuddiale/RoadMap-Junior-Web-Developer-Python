# json.load()
# json.dump()
# Persistenza dati

import json

rubrica = {
    "Mario": "123456789",
    "Anna": "987654321"
}

with open("rubrica.json", "w") as file:
    json.dump(rubrica, file, indent=4)






with open("rubrica.json", "r") as file:
    rubrica = json.load(file)

print(rubrica)



import json

# 1️⃣ Creazione rubrica
rubrica = {}

while True:
    nome = input("Inserisci nome (o 'fine' per terminare): ")
    
    if nome == "fine":
        break
    
    telefono = input("Inserisci numero di telefono: ")
    rubrica[nome] = telefono

# 2️⃣ Salvataggio su file
with open("rubrica.json", "w") as file:
    json.dump(rubrica, file, indent=4)

print("Rubrica salvata!")

# 3️⃣ Lettura dal file
with open("rubrica.json", "r") as file:
    dati = json.load(file)

print("Contenuto della rubrica:")
print(dati)

