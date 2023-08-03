# Bearbeitet durch Jasper Sagawe

import random

def lotterie(anzahl):
    kosten = 0
    gewinne = 0
    for _ in range(anzahl):
        kosten += 2

        lotterieNummern = random.sample(range(1, 50), 6)

        spielerEinsatz = random.sample(range(1, 50), 6)

        richtigeZahlen = len(set(lotterieNummern) & set(spielerEinsatz))

        if richtigeZahlen == 6:
            gewinne += 1000000000
        elif richtigeZahlen == 5:
            gewinne += 1000000
        elif richtigeZahlen == 4:
            gewinne += 10000
        elif richtigeZahlen == 3:
            gewinne += 1000
        elif richtigeZahlen == 2:
            gewinne += 10
        elif richtigeZahlen == 1:
            gewinne += 1
        elif richtigeZahlen == 0:
            gewinne += 0

    gewinneProzentual = gewinne / kosten
    return gewinneProzentual


anzahlTeilnahmen = lotterie(1000)

print(f"{anzahlTeilnahmen:.2f}%")
