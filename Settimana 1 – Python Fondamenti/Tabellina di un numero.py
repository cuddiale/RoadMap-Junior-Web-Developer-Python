while True:
    numero = int(input("Inserisci un numero e ti calcolo la tabellina fino al 10: "))
    
    tabellina = []
    
    for i in range(1, 11):
        tabellina.append(numero * i)
    
    print(f"La tabellina del {numero} è:")
    print(tabellina)

