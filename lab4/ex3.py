class Matrix:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]


    def getElement(self, i, j):
        if (0 > i or i >= self.n) and (0 > j or j >= self.m):
            return None
        return self.matrix[i][j]

    def setElement(self, i, j, element):
        if (0 > i or i >= self.n) and (0 > j or j >= self.m):
            return None
        self.matrix[i][j] = element

    def transpose(self):
        matrixTransposed = [[0] * self.n for _ in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                element = self.matrix[i][j]
                matrixTransposed[j][i] = element
        return matrixTransposed

    def multiplicatipn(self, other):
        if (self.m != other.n):
            return None

        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result

    def iterate(self, lambdaFunction):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = lambdaFunction(self.matrix[i][j])

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])

if __name__ == "__main__":
    matrix = Matrix(2, 3)
    # matrix.setElement(0, 0, 1)
    matrix.setElement(0, 1, 2)
    matrix.setElement(1, 0, 4)
    matrix.setElement(1, 1, 1)
    matrix.setElement(1, 2, 0)

    print("The transpose of the matrix")
    print(matrix.transpose())
    print()

    print(matrix)
    matrix.iterate(lambda x: x + 3)
    print("Matrix after transformation:")
    print(matrix)

    matrix1 = Matrix(3, 2)
    # matrix.setElement(0, 0, 1)
    matrix1.setElement(0, 1, 2)
    matrix1.setElement(1, 0, 4)
    matrix1.setElement(1, 1, 1)
    print("\nThe multiplication of 2 matrix:")
    print(matrix.multiplicatipn(matrix1))