# Bearbeitet durch Julius Franke

import random

stackSize = 25
stack = []

for i in range(0,stackSize):
    randomNumber = random.randint(0,100)
    stack.append(randomNumber)

print(stack)
