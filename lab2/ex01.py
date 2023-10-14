# 1. Write a function to return a list of the first n numbers in the Fibonacci string.
def fibonacci(n):
    fibo = list()
    f1 = 1
    f2 = 1
    if n == 0:
        print("No fibonacci numbers for you")
    elif n == 1:
        fibo.append(f1)
    elif n == 2:
        fibo.append(f1)
        fibo.append(f2)
    else:
        fibo.append(f1)
        fibo.append(f2)
        for i in range(n-2):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            fibo.append(f3)
    return fibo

print(fibonacci(12))