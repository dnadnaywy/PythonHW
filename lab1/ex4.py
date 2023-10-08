import sys

words = input("Please enter your string in UpperCamelCase: ")

newWord = ""

for char in words:
    if (char >= 'A' and char <='Z'):
        newWord = newWord + "_"
        newWord = newWord + char.lower()
    elif (char >= 'a' and char <='z'):
        newWord = newWord + char
    elif (char.isspace()):
        print("You cannot use spaces here!")
        sys.exit(0)

words = newWord[1:] # a '_' was added at the beginning and this deletes it
print(words)