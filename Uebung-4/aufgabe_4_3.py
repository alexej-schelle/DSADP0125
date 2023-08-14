# Bearbeitet durch Eric Böwer

import math

def alphabetPosition(letter):
    # lowercase every letter so that it is case-insensitive
    # and subtract 97 (ord('a)) so that the letter 'a' is actually 0 and not 97
    res = ord(str(letter).lower()) - ord('a')
    if res < 0 or res > 25:  # mod 26 - make sure it is in range
        return 0  # return 0 for numbers that do not fit the mod 26 range
    return res + 1  # add one so the letter 'a' is taken into account

if __name__ == '__main__':
    S = "Eine alte Dame geht heute einkaufen."
    stringLower = S.lower()

    # Compute length of characters (exclude whitespaces and special chars)
    # and compute the amount of letters coming up in the string S
    length = 0
    letterCounts = {}
    for letter in stringLower:
        if alphabetPosition(letter) != 0:  # Ensure non whitespaces and other special characters
            length += 1
            letterCounts[letter] = letterCounts.get(letter, 0) + 1
    # print(letterCounts)

    # Compute the probability of a letter coming up in the string S (p)
    probs = []
    for count in letterCounts.values():
        probs.append(count / length)
    # print(probs) # Ranging from 0 to 1

    # Compute the actual result (shannon entropy) -> https://www.biancahoegel.de/computer/lexikon/entropie.html
    result = 0
    for prob in probs:  # prob = p
        result += (-prob * math.log2(prob))

    print(result)
