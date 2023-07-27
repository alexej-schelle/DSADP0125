import numpy as np
import random

# Dimension der Matrix
n = 100

# Initialisieren einer n x n Matrix mit Nullen
graph = np.zeros((n, n))

# Bearbeitet durch Julius Franke

# Füllen der Matrix mit 50 zufällig veteilten gerichteten Kanten
for _ in range(0, 50):

    while (True):

        firstNode = random.randint(0, 99)
        secondNode = random.randint(0, 99)

        # Verhindert Schleifen und das Überschreiben einer bereits gesetzten Kante
        if ((firstNode != secondNode) and (graph[firstNode, secondNode] == 0)):

            graph[firstNode, secondNode] = 1

            break

# Ausgabe des Graphen
print(graph)

# Zu Aufgabe 5
#
# Man könnte berechnen ob es oberhalb der Diagonalen genauso viele 1en gibt wie unterhalb der Diagonalen.
# Zusätzlich könnte man über die Matrix iterieren und prüfen ob graph[i, j] = graph[j, i] ist.

isSymmetric = True

for i in range(0, 100):

    if not isSymmetric:
        break

    for j in range(i+1, 100):

        if graph[i, j] != graph[j, i]:
            
            print("Der Graph ist nicht symmetrisch!")
            isSymmetric = False
            break
