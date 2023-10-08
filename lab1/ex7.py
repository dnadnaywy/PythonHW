def extractNumber(words):
    isNumberFound = False
    number = ""
    for i in range(0, len(words)):
        char = words[i]
        if (char >= '0' and char <= '9' and isNumberFound == False):
            isNumberFound = True
            while (char >= '0' and char <= '9'):
                number = number + char
                i = i + 1
                char = words[i]

    if (isNumberFound == False):
        print("Sorry, no number found!")
    else:
        number = int(number)
        print(number, type(number))

words = input("Write here your text: ")
extractNumber(words)