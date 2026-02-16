# ciclo for da 1 a 100
# somma numeri da 1 a n che selezione l'utente

contatore = 0
for i in range(101):
    print(f"{contatore} volte arrivo a 100")
    contatore+=1
    

n = int(input("inserisci un numero che vuoi sommare "))
somma = (n*(n+1))/2
print(f"la somma è {somma}")