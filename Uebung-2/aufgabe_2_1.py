# Bearbeitet durch Julius Franke

import random

# Erstellen einer leeren Liste
randomStack = []
print(randomStack)

# Fügt der Liste iterativ 25 zufällige Ganzzahlen hinzu
for i in range(0, 25):
    randomStack.append(random.randint(0, 100))
    print(randomStack)

# Entfernt iterativ die Elemente aus der Liste, beginnend beim zuletzt hinzugefügten Element (LIFO)
for i in range(0, 25):
    randomStack.pop()
    print(randomStack)

# Die Warscheinlichkeit dass genau diese eine Liste aus 25 zufälligen Werten zwischen 0 und 100 auftritt, beträgt 1/(101^25).
# Das ist eine extrem große Zahl und damit eine sehr geringe Warscheinlichkeit.
