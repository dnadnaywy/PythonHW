def vowels(words):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in words:
        if letter in vowels:
            count = count + 1
    print(count)

words = input("Please enter a statement: ")
vowels(words)