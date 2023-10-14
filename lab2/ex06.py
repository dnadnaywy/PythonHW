# Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.
#
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4,
# 2 is in list 1 and 2, 3 is in lists 1 and 2.

def compute(x: int, *lists: list) -> list:
    dict = {}
    numbers = []

    for list in lists:
        for item in list:
            if (item in dict):
                y = dict.get(item)
                dict.update({item : y + 1})
            else:
                dict.setdefault(item,1)

    for item in dict:
        if (dict.get(item) == x):
            numbers.append(item)
    return numbers

x = 2
print(compute(x, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
