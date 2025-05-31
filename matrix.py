n, m = int(input('Введите количество строк:')), int(input('Введите количество столбцов:'))
print('Введите строки матрицы:')
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for row in matrix:
    print(*row)


def total_min_max(matrix, n, m):
    total = 0
    total_row = []
    total_col = []
    maximum = matrix[0][0]
    minimum = matrix[0][0]
    min_ind = [0, ',', 0]
    max_ind = [0, ',', 0]
    
    for i in range(n):
        row = 0
        for j in range(m):
            total += matrix[i][j]
            row += matrix[i][j]
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
                max_ind[0] = i
                max_ind[2] = j
            if matrix[i][j] < minimum:
                minimum = matrix[i][j]
                min_ind[0] = i
                min_ind[2] = j
        total_row.append(row)    
    for j in range(m):
        col = 0
        for i in range(n):
            col += matrix[i][j]
        total_col.append(col)
    return total, total_row, total_col, maximum, minimum, max_ind, min_ind

total, total_row, total_col, maximum, minimum, max_ind, min_ind = total_min_max(matrix, n, m)
print('Сумма всех элементов:', total)
print('Суммы по строкам:', total_row)
print('Суммы по столбцам:', total_col)
print('Зеркальная матрица:')
for row in matrix:
    print(*row[::-1])
print('Максимум: ', maximum, ' в позиции (', *max_ind, ')', sep ='')
print('Минимум: ', minimum, ' в позиции (', *min_ind, ')', sep = '')
if n == m:
    symmetric = True
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                symmetric = False
                break
        if not symmetric:
            break
    print('Матрица симметрична по главной диагонали' if symmetric else 'Матрица не симметрична')
else:
    print('Матрица не квадратная → симметрию не проверяем')