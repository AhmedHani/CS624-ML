__author__ = 'Ahmed Hani Ibrahim'


class InputProcessing(object):
    def __init__(self, matrix):
        self.__matrix = matrix
        self.__u = []
        self.__v = []

    def get_matrix(self):
        return self.__matrix

    def set_matrix(self, matrix):
        self.__matrix = matrix

    def get_matrix_row_length(self):
        return len(self.__matrix)

    def get_matrix_column_length(self):
        return len(self.__matrix[0])

    def is_square_matrix(self):
        return self.get_matrix_column_length() == self.get_matrix_row_length()

    def get_u(self):
        return self.__u

    def get_v(self):
        return self.__v

    def set_u_sizes(self, row, column):
        self.__u = [[1.0 for i in range(0, column)] for j in range(0, row)]

    def set_v_sizes(self, row, column):
        self.__v = [[1.0 for i in range(0, column)] for j in range(0, row)]



