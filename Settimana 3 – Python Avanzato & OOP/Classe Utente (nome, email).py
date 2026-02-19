# Classe Persona
# Creare oggetti

# creare classe persona

class Persona:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        

# creare oggetti
        
p1 = Persona("Mario", "mario@email.com")
p2 = Persona("Anna", "anna@email.com")

print(p1.nome)
print(p2.email)

# esercizio classe utente

class Utente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def mostra_dati(self):
        print("Nome:", self.nome)
        print("Email:", self.email)


# Creazione oggetto con input

nome = input("Inserisci il nome: ")
email = input("Inserisci l'email: ")

u1 = Utente(nome, email)
u1.mostra_dati()
