################################################################################################################################################
#                                                                                                                                              #
#   Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright: IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt    #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zu Aufgabe 5.5 - Algorithmen, Datenstrukturen und Programmiersprachen #

import os
import sys
import math
import numpy
import random

N = 1000
K = 100

# Definiere Elemente der Blockchain:

B = ['']
M = [[[0.0]*N]*N]*K  # Blocks
A = [0.0]*K # Assets

T = [0.0]*K # Transaktionen
H = [0.0]*K # Hash-Keys

for k in range(0,K): # Modelliere die Blöcke und Assets der Blockchain

    for i in range(0,N):

        for j in range(0,N):

            M[k][i][j] = random.uniform(0.0,100000.0)
                
            if (i == j): A[k] = M[k][i][j]

for l in range(0,K): # Simuliere K zufällige Transaktionen

    k = random.randint(0,K-1) # Zufälliger Wert der Transaktion    
    T[l] = A[k]

    B.append(M[k]) # Generate Blockchain - Block
    B.append(T[l]) # Generate Blockchain - Asset

    H[l] = random.randint(0,1E10) # Generiere Hash-Key

print('Maximal Asset: ', max(T), 'at Index Nr. ', A.index(max(T)), 'with Hash Key: ', H[T.index(max(T))], ' and Blockchain Transaction Value', T[T.index(max(T))])
print('Minimal Asset: ', min(T), 'at Index Nr. ', A.index(min(T)), 'with Hash Key: ', H[T.index(min(T))], ' and Blockchain Transaction Value', T[T.index(min(T))])
