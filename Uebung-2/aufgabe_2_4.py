# Bearbeitet durch Jasper Sagawe

import random

Matrix = {}


# Knoten ohne Verbindungen von 1 bis kn werden erstellt.
def erstelleKnoten(kn):
    for i in range(1, kn + 1):
        Matrix[str(i)] = []
    return Matrix


# Jedem Knoten werden zufällige Knoten-Nachbarn zugeschrieben.
def erstelleNachbarn():
    for knoten in Matrix:
        # Jeder Knoten hat mindestens 1 Nachbarknoten, aber maximal 5
        anzahlNachbarn = random.randint(1, min(5, len(Matrix) - 1))

        # Ausschließen des aktuellen Knotens von den potenziellen Nachbarn.
        moeglicheNachbarn = [
            ausgewaehlterKnoten
            for ausgewaehlterKnoten in Matrix.keys()
            if ausgewaehlterKnoten != knoten
        ]

        # Zufällige Auswahl von Nachbarn aus den potenziellen Nachbarn.
        nachbarn = random.sample(moeglicheNachbarn, anzahlNachbarn)
        Matrix[knoten] = nachbarn
    return Matrix


# Für alle benachbarten Knoten werden Kanten erstellt und der Wert 1 zugewiesen.
def erstelleKanten(Matrix):
    kanten = []
    for knoten in Matrix:
        for knotenNachbar in Matrix[knoten]:
            wert = 1
            kanten.append((knoten, knotenNachbar, wert))
    return kanten


erstellteKnoten = erstelleKnoten(50)
erstellteNachbarn = erstelleNachbarn()
erstellteKanten = erstelleKanten(Matrix)

# Aus allen Kanten werden 100 zufällig ausgewählt.
zufaelligeKanten = random.sample(erstellteKanten, 100)


def sucheGerichteteVerbindung(kanten):
    for i, (kanteEinsKnoten, kanteEinsNachbar, wert) in enumerate(kanten):
        for j, (kanteZweiKnoten, kanteZweiNachbar, wert) in enumerate(kanten):
            if (
                i != j
                and kanteEinsKnoten == kanteZweiNachbar
                and kanteZweiKnoten == kanteEinsNachbar
            ):
                kanten[i] = (kanteEinsKnoten, kanteEinsNachbar, 0)
                kanten[j] = (kanteZweiKnoten, kanteZweiNachbar, 0)
                break
    return kanten


kantenGetrennt = sucheGerichteteVerbindung(zufaelligeKanten)
gerichteteKanten = {}
ungerichteteKanten = {}


for kante, (knoten, nachbar, wert) in enumerate(kantenGetrennt):
    if wert == 1:
        gerichteteKanten[kante] = (knoten, nachbar, wert)
    else:
        ungerichteteKanten[kante] = (knoten, nachbar, wert)


print("gerichtete Verbindungen:", gerichteteKanten)
print("ungerichtete Verbindungen:", ungerichteteKanten)
