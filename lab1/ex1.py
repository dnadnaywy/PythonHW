numbers = list(map(int, input("Enter your numbers here: ").split()))

def cmmdc(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

cmmdc_nr = numbers[0]

for number in numbers:
    cmmdc_nr = cmmdc(number, cmmdc_nr)

print(cmmdc_nr)


