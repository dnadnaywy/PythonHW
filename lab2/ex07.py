# Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element
# will be the greatest palindrome number.

def palindrome(n):
    copy = int(n)
    oglindit = 0
    while (copy > 0):
        oglindit = oglindit * 10 + copy % 10
        copy = copy // 10
    if oglindit == int(n):
        return True
    else:
        return False


def checkProperty(numbers: list):
    contor = 0
    maxim = -2e9
    for number in numbers:
        if palindrome(number):
            contor = contor + 1
            if (number > maxim):
                maxim = number
    tuple = (contor, maxim)
    return tuple

print(checkProperty([121, 12321, 34, 45, 243534]))
