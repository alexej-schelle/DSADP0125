import random

def shift_left (queue):
    queue.pop(0)                                    # entfernen des des ersten Elements
    queue.append('0')                               # auffüllen mit '0'
    return queue

def shift_right(queue):
    queue.pop()                                     # entfernen des letzten Elements
    queue.insert(0,'0')                             # auffüllen mit '0'
    return queue

queue = [random.randint(0,1001) for _ in range(50)] # anlegen der Queue mit 50 Einträgen

print ("queue")
print(queue)

queue_left = queue.copy()                           # kopieren
queue_right = queue.copy()

print("\n25 mal shift nach links ")

for _ in range(25):                                 # Schiebergesiter nach links
    shift_left(queue_left)
print(queue_left)


print("\n25 mal shift nach rechts ")

for _ in range(25):                                 # Schieberegister nach rechts
    shift_right(queue_right)    
print(queue_right)





