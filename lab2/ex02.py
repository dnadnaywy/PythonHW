# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def isPrime(n: int) -> bool:
    if (n < 2):
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True

def primeNumbers(numbers: list) -> list:
    prime = list()
    for number in numbers:
        if (isPrime(number)):
            prime.append(number)
    return prime

numbers = [1, 3, 5, 8, 9, 11]
print(primeNumbers(numbers))