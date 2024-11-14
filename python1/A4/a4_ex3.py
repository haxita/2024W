def multiply_matrix(matrix1: list, matrix2: list) -> list:
    num_cols_matrix1 = len(matrix1[0])
    num_rows_matrix2 = len(matrix2)

    if num_cols_matrix1 != num_rows_matrix2:
        return None

    num_rows_matrix1 = len(matrix1)
    num_cols_matrix2 = len(matrix2[0])

    result_matrix = [[0 for _ in range(num_cols_matrix2)] for _ in range(num_rows_matrix1)]

    for i in range(num_rows_matrix1):
        for j in range(num_cols_matrix2):
            for k in range(num_cols_matrix1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix


