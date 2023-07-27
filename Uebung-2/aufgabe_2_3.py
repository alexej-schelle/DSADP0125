# Bearbeitet durch Julius Franke

import numpy as np

# Dimension der Matrix (Anzahl der Knoten)
n = 100

# Initialisierung einer n x n - Adjazenzmatrix aus Nullen
# Jede Zelle stellt eine Kante zwischen zwei Knoten dar
graph = np.zeros((n, n))

# Iteration über die einzelnen Zellen der Matrix
for i in range(0, n):
    for j in range(i+1, n):

        # Erzeugung eines Zufallswertes aus der Normalverteilung mit Mittelwert 50 und Standardabweichung sqrt(50)
        value = np.random.normal(50, np.sqrt(50))

        # Sicherstellen das der Wert nicht negativ ist
        value = max(1, value)

        # Zuweisung des Wertes zu den entsprechenden Kanten
        # Da der Graph ungerichtet ist haben (i, j) und (j, i) die gleiche Kante
        graph[i, j] = value
        graph[j, i] = value

        # Die Diagonale wird auf "nan" gesetzt damit die Kante (i, i) später vom Algorithmus ignoriert werden kann
        np.fill_diagonal(graph, np.nan)

# Ausgabe der Matrix
print(graph)

# Greedy Algorithmus
def Greedy(graph, start, steps):

    # current ist der aktuelle Knoten,
    # path ist der zurückgelegte Pfad
    # und totalValue der Gesamtwert aller durchlaufenen Kanten
    current = start
    path = [current]
    totalValue = 0

    # Durchläuft den Graphen in N = 50 Schritten
    for _ in range(0, steps):
        neighbours = graph[current]             # Zeigt die Kanten der benachbarten Knoten
        nextNode = np.nanargmin(neighbours)     # Gibt den Index des nächsten Knoten zurück, bei welchem der Wert der Kante am niedrigsten ist und ignoriert "nan" - Werte
        totalValue += graph[current, nextNode]  # Der Wert des Pfads wird zum Gesamtwert angerechnet
        path.append(nextNode)                   # Der neue Knoten wird zur Historie hinzugefügt
        current = nextNode                      # Der alte Knoten wird mit dem neuen Knoten überschrieben

    return path, totalValue

# Ausführen des Algorithmus
path, totalValue = Greedy(graph, 0, 50)

# Ausgabe der Werte
print("Zurückgelegter Pfad:")
print(path)

print("Gesamtwert:")
print(totalValue)
