__author__ = 'Ahmed Hani Ibrahim'


def matrix_normalization(matrix, min_range, max_range):
    min = 1000
    max = 0.0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < min:
                min = matrix[i][j]
            if matrix[i][j] > max:
                max = matrix[i][j]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = (matrix[i][j] - min) / (max - min)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = (matrix[i][j] * (max_range - min_range)) + min_range

    return matrix
