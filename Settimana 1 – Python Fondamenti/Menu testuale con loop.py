"""" 
Creare Menu testuale stampato con loop 
Stampa numeri 1–10
Somma numeri stampati

for
while
range()

"""

# creo variabile menù
 
menu = ["pizza", "pasta", "carne", "pesce"]

# stampo col ciclo for tutti gli elementi della lista

for x in menu:
    print(x)
    
    
# stampare numeri da 1 a 10
    
for i in range(11):
    print(i)
    
# stampiamo i numeri da 1 a 10 col ciclo while

i= 0 #dichiaro variabile i è la imposto a 0
while i <11:
    print(i)
    i+=1
    
#somma numeri stampati

somma = 0

for i in range(1, 11):
    print(i)
    somma += i

print("Somma:", somma)



    
