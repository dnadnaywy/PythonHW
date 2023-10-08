def mostCommonLetter(words):
    words = words.lower()
    frecvArray = [0 for i in range(300)]

    for char in words:
        frecvArray[ord(char)] = frecvArray[ord(char)] + 1

    maxim = 0
    for i in range(ord("a"), ord("z") + 1):
        if (frecvArray[i] and frecvArray[i] > maxim and chr(i).isspace() == 0):
            maxim = frecvArray[i]
            letter = chr(i)

    print("[" + letter + "]" + " is the most common character with " + str(maxim) + " appearances")

words = input("Please type a string: ")
mostCommonLetter(words)