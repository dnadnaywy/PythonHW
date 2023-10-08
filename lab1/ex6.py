def palindrome(n):
    if n.isdigit():
        copy = int(n)
        oglindit = 0
        while (copy > 0):
            oglindit = oglindit * 10 + copy % 10
            copy = copy//10
        if oglindit == int(n):
            print(True)
        else:
            print(False)
    else:
        print("Invalid input. Please enter a valid integer.")

number = input("Please enter your number: ")
palindrome(number)
