################################################################################################################################################
#                                                                                                                                              #
#   Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt    #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zu Aufgabe 2.3 - Algorithmen, Datenstrukturen und Programmiersprachen #

import os
import sys
import statistics

import numpy as np

import math
import random

N = 250 # Anzahl der Knoten im Graphen
N_trials = 100 # Anzahl der Realisierungen 

N_cols = 250 # Anzahl der Spalten
N_rows = 250 # Anzahl der Zeilen

N_path = 100 # Anzahl der Pfade im Greedy-Algorithmus
path_length = 0.0 # Variable für die gesamte Pfadlänge
minimum = 1000.0 # Variable für die (minimale) Pfadlänge zwischen dem aktuellen Knoten und dem nächsten Knoten

mu = 50 # Mittelwert der Pfadlänge zwischen benachbarten Pfaden
sigma = math.sqrt(1.0*mu) # Standardabweichung der Pfadlänge zwischen benachbarten Pfaden

sreg = [[0]*N_cols]*N_rows # Definition eines Arrays zur Darstellung eines Graphen G = (E,K,f)
count_path_length = []

path_length = 0.0
average_path_length = 0.0
variance = 0.0

for k in range(0, N_trials): # Iteriere über unterschiedliche Realisierungen

    path_length = 0.0 # Lege Pfadlänge wieder auf Null fest
    print(k)

    for i in range(0, N): # Generierung der Werte für den Graphen G = (E,K,f)

        sreg[i][i] = i # Diagonal Elemente repräsentieren Knotenpunkte e_i = i im Graphen G = (E,K,f)

        for j in range(0, N): # Nicht Diagonal Elemente repräsentieren Verbindungen k_i der Knotenpunkte e_i im Graphen G = (E,K,f)

            sreg[i][j] = random.gauss(mu,sigma) # Die Funktion f = random.gauss ordnet den Knotenpunkten einen zufälligen Wert zu

    k = 0 # Starte den Pfad bei e_1 (entspricht der Variablen k = 0)

    for i in range(0, N_path): # Greedy-Algorithmus - Durchlauf von N_path Pfaden im Graphen G

        minimum = 1000.0

        for j in range(0, N): # Greedy-Algorithmus - Finde bei jedem Knotenpunkt k im Pfad mit N Knoten den kürzesten Weg zum nächsten Pfad

            if (sreg[k][j] < minimum) : minimum = sreg[k][j]

        k = j # Setze den Pfad ab dem Punkt k = j (ab e_k) fort

        path_length = path_length + minimum # Berechne die gesamte Pfadlänge
    
    average_path_length = average_path_length + path_length # Berechne die mittlere Pfadlänge 
    count_path_length.append(path_length) # Speichere alle Pfadlängen der einzelnen Realisierungen

variance = statistics.variance(count_path_length) # Berechne die Varianz daraus

print('Mittlere Pfadlänge: ', average_path_length/float(N_trials)) # Mittlere Pfadlänge 
print('Varianz: ', math.sqrt(variance)) # Varianz aus der Modellierung von Pfadlängen
