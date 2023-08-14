# Bearbeitet durch Julius Franke

import random

# Nimmt einen String, Schlüssel und Zeichensatz entgegen und gibt einen verschlüsselten String zurück
def EncryptString(string, key, charset):
    string = string.lower()
    encryptedString = ""
    for char in string:
        if char in charset:
            oldIndex = charset.index(char)
            newIndex = (oldIndex + key) % 26
            encryptedString += charset[newIndex]
        else:
            encryptedString += char
    return encryptedString

# Nimmt einen verschlüsselten String, den Schlüssel und einen Zeichensatz entgegen und gibt den entschlüsselten String zurück
def DecryptString(encryptedString, key, charset):
    decryptedString = ""
    for char in encryptedString:
        if char in charset:
            oldIndex = charset.index(char)
            newIndex = (oldIndex - key) % 26
            decryptedString += charset[newIndex]
        else:
            decryptedString += char
    return decryptedString

# Der Zeichensatz welcher als Referenz für die Indexverschiebung dient
charset = "abcdefghijklmnopqrstuvwxyz"

# Der String welcher verschlüsselt werden soll
string = "Eine alte Dame geht heute einkaufen."

# Der Schlüssel welcher die Verschiebung angibt
key = random.randint(0, 1000)

# Der verschlüsselte String
encryptedString = EncryptString(string, key, charset)

# Der entschlüsselte String
decryptedString = DecryptString(encryptedString, key, charset)

# Ausgabe der Werte
print("Schlüssel: ", key)                       
print("Verschlüsselter Text: ", encryptedString)
print("Entschlüsselter Text: ", decryptedString)
