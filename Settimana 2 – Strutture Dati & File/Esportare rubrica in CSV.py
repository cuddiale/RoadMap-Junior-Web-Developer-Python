# CSV reader
# CSV writer

import csv

with open("rubrica.csv", "r") as file:
    reader = csv.reader(file)
    
    for riga in reader:
        print(riga)


import csv

with open("rubrica.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["nome", "telefono", "email"])
    writer.writerow(["Mario", "123456789", "mario@email.com"])
    writer.writerow(["Anna", "987654321", "anna@email.com"])



import csv

with open("rubrica.csv", "r") as file:
    reader = csv.reader(file)
    
    next(reader)  # Salta intestazione
    
    for nome, telefono, email in reader:
        print(f"Nome: {nome} - Telefono: {telefono} - Email: {email}")
        
        
# esportazione in CSV
        
import csv

rubrica = {
    "Mario": {"telefono": "123456789", "email": "mario@email.com"},
    "Anna": {"telefono": "987654321", "email": "anna@email.com"}
}

with open("rubrica.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # intestazione
    writer.writerow(["nome", "telefono", "email"])
    
    # dati
    for nome, dati in rubrica.items():
        writer.writerow([nome, dati["telefono"], dati["email"]])

print("Rubrica esportata in CSV!")

