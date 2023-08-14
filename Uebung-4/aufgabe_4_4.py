# Bearbeitet durch Jasper Sagawe

from urllib.request import urlopen

def sucheWorthaeufigkeit(string, suche):
    wortHaeufigkeit = {}

    einzelneWoerter = string.split()

    for wort in einzelneWoerter:
        wort = wort.strip(".,!?").lower()

        if wort in suche:
            if wort in wortHaeufigkeit:
                wortHaeufigkeit[wort] += 1
            else:
                wortHaeufigkeit[wort] = 1

    return wortHaeufigkeit

url = (
    "https://raw.githubusercontent.com/alexej-schelle/AlgDatPro/master/PythonString.txt"
)
urlOeffnen = urlopen(url)
string = urlOeffnen.read().decode("utf-8")

eingabe = (
    input("Welche Wörter werden gesucht? (Durch Leerzeichen getrennt)").lower().split()
)

worthaeufigkeit = sucheWorthaeufigkeit(string, eingabe)

for wort, anzahl in worthaeufigkeit.items():
    print(f"{wort}: {anzahl}")
