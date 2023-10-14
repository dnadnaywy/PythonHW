# Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
# For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
# otherwise it should contain characters that have the ASCII code not divisible by x.
# Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must return list of lists.

def generate(listStrings: list, x=1, flag=True):
    generatedLists = []
    for string in listStrings:
        generatedList = []
        if flag == True:
            for char in string:
                if ord(char) % x == 0:
                    generatedList.append(char)
        else:
            for char in string:
                if ord(char) % x != 0:
                    generatedList.append(char)
        generatedLists.append(generatedList)
    return generatedLists

print(generate(["test", "hello", "lab002"], 2, False))