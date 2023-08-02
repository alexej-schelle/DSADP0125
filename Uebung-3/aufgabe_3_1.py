# Bearbeitet durch Julius Franke

# Verifizieren Sie numerisch für Gauß-verteilte Variablen in Python, 
# dass die Summe von Gauß-verteilten Variablen wieder Gauß-verteilt ist. 
# Wie nennt man diesen Zusammenhang in der Mathematik?
#__________________________________________________________________________________________________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt

m = 0                                                                  # Mittelwert der Gauß-Verteilung
u = 50                                                                 # Standardabweichung der Gauß-Verteilung

list = []                                                              # Liste, um Gauß-verteilte Zufallsvariablen zu speichern
averageList = []                                                       # Liste, um die Mittelwerte der Gauß-verteilten Zufallsvariablen zu speichern

for _ in range(10000):                                                 # Schleife für 10000 Experimente
    sample = np.random.normal(m, u,10000)                              # Array mit 10000 Gauß-verteilten Zufallsvariablen
    list.append(sample)                                                # hinzufügen zur Liste
    averageList.append(np.sum(sample)/10000)                           # Berechnung des Mittelwerts der Gauß-verteilten Zufallsvariablen, hinzufügen zur Liste


# numerischer Beweis:
print(averageList)  
print(np.sum(averageList) / 10000)                                     # Sollte nah am Mittelwert m sein

# grafischer Beweis:
plt.hist(list[0], bins=50, density=True, color='pink')                 # Erstelle eines Histogramm der berechneten Summen
plt.xlabel('Summe der Gauß-verteilten Variablen')                       
plt.ylabel('Relative Häufigkeit')                                       
plt.title(f'Histogramm der Summe von {10000} Gauß-verteilten Variablen')  
plt.show()                                                              

# in der Mathematik nennt man die Eigenschafft, dass die Summe von gauusverteilten Variablen wieder gauusverteilt ist, 
# die Additive Normalverteilung oder Additive Gauss'sche Verteilung
