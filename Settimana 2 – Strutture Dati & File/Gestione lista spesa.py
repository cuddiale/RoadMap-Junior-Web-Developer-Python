# crare una lista della spesa con input utente
# creare anche logica del calcellare se esiste e aggiungere se non esiste


# Indicizzazione

numeri = [10, 20, 30]

print(numeri[0])  # 10
print(numeri[1])  # 20


# Somma e media

numeri = [5, 10, 15, 20, 25]

somma = sum(numeri)
media = somma / len(numeri)

print("Somma:", somma)
print("Media:", media)


# Ricerca elemento

numeri = [5, 10, 15, 20, 25]

elemento = 15

if elemento in numeri:
    print("Elemento trovato!")
else:
    print("Elemento non trovato.")


# Gestione Lista Spesa con input utente

spesa = []

while True:
    prodotto = input("Inserisci prodotto (o 'fine' per uscire): ")
    
    if prodotto == "fine":
        break
    
    spesa.append(prodotto)

print("La tua lista della spesa:")
for item in spesa:
    print("-", item)
