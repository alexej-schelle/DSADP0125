# Bearbeitet durch Jasper Sagawe
 
alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

buchstabenWert = {buchstabe: nummer // 2 for nummer, buchstabe in enumerate(alphabet)}


def stringZuWert(string):
    wert = 0
    for i in string:
        if i in buchstabenWert:
            wert += buchstabenWert[i]
    return wert


textstring = "Eine alte Dame geht heute einkaufen."

print(stringZuWert(textstring))
