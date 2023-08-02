################################################################################################################################################
#                                                                                                                                              #
#   Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt    #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zu Aufgabe 3.5 - Algorithmen, Datenstrukturen und Programmiersprachen #

import os
from platform import java_ver
import sys
import math
import random
import numpy
import numpy as np
import pylab
import matplotlib.pyplot as plt
import operator

choose_numbers = {0,0,0,0,0,0}
numbers = {0,0,0,0,0,0}

profit = [0.0, 0.0, 0.0, 10.0, 50.0, 500.0, 10000.0]
random_number = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

sample_size = 2500
lot_numbers = 0

total_average_profit = 0.0

ticket_price = 2.50
paid_price = 0.0

price_1 = []
price_2 = []

for n in range(0, sample_size):

    total_profit = 0.0
    paid_price = 0.0
    rnd = 0

    lot_numbers = random.randint(1, sample_size)

    for k in range(1, lot_numbers):

        paid_price = paid_price + ticket_price

        for m in range(0, 7): # Definiere die Anzahl der Zahlen in der Lotterie
            
            rnd = random.randint(1, 49)
            if (rnd not in random_number) : random_number[m] = rnd

        numbers = {}
        numbers = {random_number[0], random_number[1], random_number[2], random_number[3], random_number[4], random_number[5], random_number[6]}

        for n in range(0, 6): # Wähle die Anzahl der Zahlen in der Lotterie
            
            rnd = random.randint(1, 49)
            if (rnd not in random_number) : random_number[n] = rnd

        choose_numbers = {}
        choose_numbers = {random_number[0], random_number[1], random_number[2], random_number[3], random_number[4], random_number[5]}

        if (len(numbers.intersection(choose_numbers)) in range(0, 6)) : total_profit = total_profit + profit[len(numbers.intersection(choose_numbers))]

    price_1.append(paid_price)    
    price_2.append(total_profit)    

plt.figure(10) # Initiiere die Figur 1 
plt.xlabel('Gezahlter Preis', fontsize = 10)
plt.ylabel('Mittlerer Gewinn', fontsize = 10)
plt.xlim(0.0,100.0)
plt.ylim(0.0,100.0)
plt.hist2d(price_1, price_2, bins = 25, cmap=plt.cm.BuPu) # Zeichnen der Figur 
plt.savefig('fig_3_5.png') # Speichere die Figur zum richtigen Pfad (finde den Pfad mit pwd)
