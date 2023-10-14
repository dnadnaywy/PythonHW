# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)

def solve(a: list, b: list) -> str:
    intersection = [val for val in a if val in b]

    reunion = []
    for item in a + b:
        if item not in reunion:
            reunion.append(item)

    aMinusB = [val for val in a if val not in b]
    bMinusA = [val for val in b if val not in a]

    return "Intersection: " + str(intersection) + ".\nReunion: " + str(reunion) + ".\nA minus B: " + str(aMinusB) + ".\nB minus A: " + str(bMinusA)

a = [1, 2, 3, 4, 5, 10]
b = [2, 3, 5, 6, 7]
print(solve(a,b))
