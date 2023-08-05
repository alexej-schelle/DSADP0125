# Bearbeitet durch Noel Pascal Koeppen

def calculate_pi_leibniz(precision):
    pi = 0
    for i in range(precision * 10**5):  
        term = (-1)**i / (2*i + 1)      
        pi += term
    pi *= 4                             
    return round(pi, 10)                # Runde Pi auf 10 Stellen

print(calculate_pi_leibniz(100))
