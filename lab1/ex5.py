n = 4
word = ""

matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

for k in range(0, (n + 1) // 2):
    for i in range(k, (n - k)):
        word = word + matrix[k][i]
    for i in range(k + 1, (n - k)):
        word = word + matrix[i][n - k - 1]
    for i in range(n - k - 1 - 1, k, -1):
        word = word + matrix[n - k - 1][i]
    for i in range(n - k - 1, k, -1):
        word = word + matrix[i][k]

print(word)