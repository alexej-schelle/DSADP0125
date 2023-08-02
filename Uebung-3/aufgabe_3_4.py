import random

# Dieses Programm Simuliert in zwei Fällen das Monty-Hall-Problem

# Fall 1: Der Spieler bleibt bei seiner Wahl
def Fall1():
    
    winCounter = 0      # Anzahl wie oft der Spieler gewonnen hat
    trys = 100000       # Anzahl der Durchläufe

    # Schleife für die Spieldurchläufe
    for _ in range(0, trys):

        doors = [0, 0, 0]                   # Repräsentation der "Türen"
        choice = random.randint(0, 2)       # Die Wahl des Spielers ausgedrückt durch einen Index 
        winningDoor = random.randint(0, 2)  # Index der "Tür" welche den Preis enthält
        doors[winningDoor] = 1              # Zuweisung des Wertes 1 zur Tür

        # Zuweisung des Wertes 2 zu der Tür welche geöffnet und dem Spieler gezeigt wird
        # Die Tür entspricht dabei nicht der Wahl des Spielers und enthält eine Niete
        while(True):
            openDoor = random.randint(0, 2)

            if(doors[openDoor] == 0 and openDoor != choice):
                doors[openDoor] = 2
                break

        # Der Spieler entscheidet sich dafür seine Wahl nicht zu ändern.
        # Wenn er richtig liegt wird der Counter erhöt.          
        if(doors[choice] == 1):
            winCounter += 1

    # Ausgabe der Gewinnhäufigkeit nach x Durchläufen
    print("Gewinnhäufigkeit für Fall 1:")
    winProbability = winCounter / trys
    print(winProbability)


# Fall 2: Der Spieler entscheidet sich nochmal um.
# Der Code hier ist fast identisch zu obigem Beispiel. 
def Fall2():
    
    winCounter = 0      
    trys = 100000      
    
    for _ in range(0, trys):

        doors = [0, 0, 0]
        choice = random.randint(0, 2)
        winningDoor = random.randint(0, 2)
        doors[winningDoor] = 1

        while(True):
            openDoor = random.randint(0, 2)

            if(doors[openDoor] == 0 and openDoor != choice):
                doors[openDoor] = 2
                break

        # Hier entscheidet sich der Spieler nochmal für eine andere Tür.         
        for i in range(0, 3):

            # Es darf sich natürlich nicht für die offene Tür oder die Ursprüngliche entschieden werden.
            # In diesem Fall kann i nur einen wahren Wert haben.
            if(i != choice and doors[i] != 2):      
                choice = i
                break

        if(doors[choice] == 1):
            winCounter += 1

    # Ausgabe der Gewinnhäufigkeit nach x Durchläufen   
    print("Gewinnhäufigkeit für Fall 2:")
    winProbability = winCounter / trys
    print(winProbability)

# Ausführen der beiden Fälle
Fall1()
Fall2()

# Die Gewinnhäufigkeiten beider Fälle repräsentieren bei ausreichend vielen Durchläufen relativ präzise die Gewinnwarscheinlichkeit 
# Für Fall 1 liegt diese bei 1/3 und für Fall 2 bei 2/3
