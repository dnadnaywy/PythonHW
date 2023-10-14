def generate(*lists) -> list:
    maxim = -2e9
    for list in lists:
        if (len(list) > maxim):
            maxim = len(list)

    finalList = []

    for j in range(0, maxim):
        tuples = tuple()
        for i in range(0, len(lists)):
            if len(lists[i]) > j:
                tuples = tuples + (lists[i][j],)
            else:
                tuples = tuples + (None,)
            # print(lists[i][j])
        finalList.append(tuples)

    return finalList

print(generate([1, 2, 3], [5, 6, 7, 8], ["a", "b", "c"]))