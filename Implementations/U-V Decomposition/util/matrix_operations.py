__author__ = 'Ahmed Hani Ibrahim'


def matrix_multiplication(matrix1, matrix2):
    result = [[0.0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]

    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix2[0])):
            for k in range(0, len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
