# Von Robyn Eismann

number = 2                          # 2 ist 1. Primzahl
primeCounter = 1                    # counter start bei 1 wegen ersten Primzahl 2

while primeCounter != 1000:     
    number += 1                     # zählt die Zahlen
    primeNumber = True            
    for i in range (2,number):      # testet ob number eine Primzahl ist
        if (number % i) == 0:       
            primeNumber = False     # dann ist number keine Primzahl
            break
    if primeNumber == True:         
        primeCounter += 1           # ist eine Primzahl, also imkrementieren wir den Counter  

print (number)                      # gibt 1000. Primzahl raus
