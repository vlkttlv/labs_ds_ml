import random

import numpy
from lab2_exceptions import MatrixDimensionError


class Matrix:

    def __init__(self, rows, cols, fill_random=False, min_val=0,
                 max_val=10):
        """Конструктор класса Матрица. Заполняет матрицу нулями или
        случайными числами, если это указано."""

        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        if fill_random:
            for i in range(rows):
                for j in range(cols):
                    self.data[i][j] = random.randint(min_val, max_val)

    def __str__(self):
        """Переопределение функции вывода на экран."""

        m = ''
        for i in range(self.rows):
            for j in range(self.cols):
                m += str(self.data[i][j])+' '
            m += ' \n'
        return m

    def __add__(self, other):
        """Переопределение операции сложения матриц."""
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixDimensionError
        sum_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                sum_matrix.data[i][j] = self.data[i][j] + other.data[i][j]

        return sum_matrix

    def __sub__(self, other):
        """Переопределение операции вычитания матриц."""
        if isinstance(other, numpy.ndarray):
            if self.rows != other.shape[0]:
                raise MatrixDimensionError
            sub_matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    sub_matrix.data[i][j] = self.data[i][j] - other[i]
            return sub_matrix
        else:
            if self.rows != other.rows or self.cols != other.cols:
                raise MatrixDimensionError
            sub_matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    sub_matrix.data[i][j] = self.data[i][j] - other.data[i][j]
            return sub_matrix

    def __mul__(self, other):
        """Переопределение операции умножения матриц."""
        
        if self.cols != other.rows:
            raise MatrixDimensionError
        mult_matrix = Matrix(self.rows, other.cols)
        for i, _ in enumerate(self.data):
            for j, _ in enumerate(other.data[0]):
                for k, _ in enumerate(other.data):
                    mult_matrix.data[i][j] += self.data[i][k] * \
                        other.data[k][j]

        return mult_matrix

    def transpose(self):
        """Функция транспонирования матрицы."""
        new_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.data[j][i] = self.data[i][j]

        return new_matrix

    
    @staticmethod
    def concat(matrix1, matrix2, axis=1):
        """Метод для конкатенации двух матриц по оси (1 - по столбцам, 0 - по строкам)."""

        if matrix1.rows != matrix2.shape[0]:
            raise MatrixDimensionError
        if isinstance(matrix2, numpy.ndarray):
            if axis == 1:
                # Создаем новую матрицу с тем же числом строк, но суммой числа столбцов
                result = Matrix(matrix1.rows, matrix1.cols + matrix2.shape[1])

                # Копируем элементы первой матрицы
                for i in range(matrix1.rows):
                    for j in range(matrix1.cols):
                        result.data[i][j] = matrix1.data[i][j]
                    
                # Добавляем элементы второй матрицы начиная со столбца после конца первой матрицы
                for i in range(matrix1.rows):
                    for j in range(matrix1.cols):
                        result.data[i][matrix1.cols + j] = matrix2[i][j]

            if axis == 0:
                result = Matrix(matrix1.rows + matrix2.shape[0], matrix1.cols)
                
                # Копируем элементы первой матрицы
                for i in range(matrix1.rows):
                    for j in range(matrix1.cols):
                        result.data[i][j] = matrix1.data[i][j]
                        
                # Добавляем элементы второй матрицы начиная со строки после конца первой матрицы
                for i in range(matrix2.shape[0]):
                    for j in range(matrix1.cols):
                        result.data[matrix1.rows + i][j] = matrix2[i][j]

            return result