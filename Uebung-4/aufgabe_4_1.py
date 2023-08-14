# Bearbeitet durch Robyn Eismann

def CalculateFibonacci(index):                          # Fibonacci Algorithmus aus der Vorlesung:

    fibonacci = ['']*(index+1)                          # Definiere Python-Liste für Fibonacci-Zahlenfolge

    fibonacci[0] = 1                                    # Erstes Element der Fibonacci-Zahlenfolge
    fibonacci[1] = 1                                    # Zweites Element der Fibonacci-Zahlenfolge

    for k in range(2,index+1):
        fibonacci[k] = fibonacci[k-1] + fibonacci[k-2]  # Restliche Elemente der Fibonacci-Zahlenfolge

    return(fibonacci[index-1])                          # Rueckgabewert der Funktion CalculateFibonacci


def isPrime(number):

    for i in range (2, number):
        if (number % i) == 0:     
            return False
    
    return True


N = 25                                                  # 25-ste Fibonacci-Zahl der Fibonacci-Zahlenfolge
number = CalculateFibonacci(N)
print ("25. Fibonacci Zahl: " , number)

while not isPrime(number):
    number += 1
print ("erste Primzahl nach der 25. Fibonacci Zahl: " , number)
