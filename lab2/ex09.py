def seats(matrix: list) -> list:
    listOfTuples = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            for k in range(0, i):
                if matrix[i][j] <= matrix[k][j]:
                    tuple = (i, j)
                    listOfTuples.append(tuple)
                    break
    return listOfTuples


matrix = [[1, 2, 3, 2, 1, 1],

          [2, 4, 4, 3, 7, 2],

          [5, 5, 2, 5, 6, 4],

          [6, 6, 7, 6, 7, 5]]
print(seats(matrix))
