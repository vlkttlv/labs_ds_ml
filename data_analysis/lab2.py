import random

from lab2_exceptions import MatrixDimensionError
import numpy as np



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
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixDimensionError
        sub_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                sub_matrix.data[i][j] = self.data[i][j] - other.data[i][j]
        return (sub_matrix)

    def __mul__(self, other):
        """Переопределение операции умножения матриц."""
        if self.cols != other.rows:
            raise MatrixDimensionError
        mult_matrix = Matrix(self.rows, other.cols)
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
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
        return np.concatenate((matrix1, matrix2), axis=axis)


class LogisticRegression:
    def __init__(self, x, y):
        self.intercept = np.ones((x.shape[0], 1))
        self.x = np.concatenate((self.intercept, x), axis=1)
        self.weight = np.zeros(self.x.shape[1])
        self.y = y

    # Вычисление сигмоиды
    def sigmoid(self, x, weight):
        z = np.dot(x, weight)
        return 1 / (1 + np.exp(-z))

    # Вычисление функции потерь
    def loss(self, h, y):
        return -np.mean(y * np.log(h + 1e-10) + (1 - y) * np.log(1 - h + 1e-10))

    # Вычисление градиента
    def gradient_descent(self, X, h, y):
        return np.dot(X.T, (h - y)) / y.size

    # Функция обучения
    def fit(self, lr, iterations):
        for i in range(iterations):
            sigma = self.sigmoid(self.x, self.weight)
            loss = self.loss(sigma, self.y)
            dW = self.gradient_descent(self.x, sigma, self.y)
            # Updating the weights
            self.weight -= lr * dW
        return print('fitted successfully to data')

    # Функция предсказания метки класса
    def predict(self, x_new, treshold):
        x_new = np.concatenate((self.intercept, x_new), axis=1)
        result = self.sigmoid(x_new, self.weight)
        result = result >= treshold
        y_pred = np.zeros(result.shape[0])
        for i in range(len(y_pred)):
            if result[i] == True:
                y_pred[i] = 1
            else:
                continue
        return y_pred


def test_matrix_operations():
    # Тестирование создания и вывода матрицы
    m1 = Matrix(2, 2)
    assert m1.rows == 2 and m1.cols == 2, "Ошибка: размеры матрицы некорректны"
    # Тестирование сложения матриц
    m2 = Matrix(2, 2)
    m1.data = [[1, 2], [3, 4]]
    m2.data = [[5, 6], [7, 8]]
    result = m1 + m2
    assert result.data == [[6, 8], [10, 12]
                           ], "Ошибка: сложение матриц выполнено неправильно"
    # Тестирование вычитания матриц
    result = m1 - m2
    assert result.data == [[-4, -4], [-4, -4]
                           ], "Ошибка: вычитание матриц выполнено неправильно"
    # Тестирование умножения матриц
    m3 = Matrix(2, 2)
    m3.data = [[1, 0], [0, 1]]
    result = m1 * m3
    assert result.data == [[1, 2], [3, 4]
                           ], "Ошибка: умножение матриц выполнено неправильно"
    # Тестирование транспонирования матрицы
    result = m1.transpose()
    assert result.data == [
        [1, 3], [2, 4]], "Ошибка: транспонирование матрицы выполнено неправильно"
    # Тестирование исключения при сложении матриц разного размера
    m4 = Matrix(3, 2)
    try:
        result = m1 + m4
    except MatrixDimensionError:
        print("Тест пройден: исключение при сложении матриц разного размера")
    else:
        assert False, "Ошибка: не выброшено исключение при сложении матриц разного размера"
    # Тестирование исключения при умножении матриц с несовместимыми размерами
    m5 = Matrix(3, 2)
    try:
        result = m1 * m5
    except MatrixDimensionError:
        print("Тест пройден: исключение при умножении матриц с несовместимыми размерами")
    else:
        assert False, "Ошибка: не выброшено исключение при умножении матриц с несовместимыми размерами"
    print("Все тесты успешно пройдены!")


test_matrix_operations()