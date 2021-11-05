matrix_size = int(input("Розмір матриці:"))
matrix = []
for i in range(matrix_size):
    row = []
    for j in range(matrix_size):
        row.append(0)
    matrix.append(row)

one_am = int(input("Кількість одиниць в матриці:"))
print("Введіть координати одиниць")
for k in range(one_am):
    i = int(input(f"№{k}: рядок ="))
    j = int(input(f"№{k}: стовпець ="))
    matrix[i][j] = 1
print("Початкова матриця")
for i in range(matrix_size):
    print(matrix[i])


def trans_closure(matrix, matrix_size):
    for k in range(matrix_size):
        for i in range(matrix_size):
            if i != k and matrix[i][k] == 1:
                for j in range(matrix_size):
                    matrix[i][j] = matrix[i][j] | matrix[k][j]
    return matrix


matrix = trans_closure(matrix, matrix_size)


def simetric(matrix, matrix_size):
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] == 1:
                matrix[j][i] = 1
    return matrix


matrix = simetric(matrix, matrix_size)


def test(matrix, matrix_size):
    while True:
        if matrix == trans_closure(matrix, matrix_size):
            break
        else:
            matrix = trans_closure(matrix, matrix_size)
            matrix = simetric(matrix, matrix_size)
    return matrix


matrix = test(matrix, matrix_size)


def diagonal(matrix, matrix_size):
    for i in range(matrix_size):
        for j in range(matrix_size):
            if i == j:
                matrix[i][j] = 1
    return matrix


matrix = diagonal(matrix, matrix_size)

print("Кінцева матриця")
for i in range(matrix_size):
    print(matrix[i])
