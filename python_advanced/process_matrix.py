def process_matrix(matrix: list[list[int]]) -> tuple:
    """Проверяет матрицу на квадратность и преобразует чётные элементы квадратной матрицы в None."""
    if any(len(row) != len(matrix) for row in matrix):
        return False, None
    new_matrix = []
    for row in matrix:
        new_row = [x if x % 2 != 0 else None for x in row]
        new_matrix.append(new_row)
    return True, new_matrix

matrix1 = [[1, 2], [3, 4, 5]]
matrix2 = [[4, 2, 9], [1, 5, 3], [7, 8, 6]]
print("Тест 1:", process_matrix(matrix1))
print("Тест 2:", process_matrix(matrix2))