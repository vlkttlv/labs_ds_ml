import numpy as np
from datetime import datetime
from sklearn.datasets import load_breast_cancer
from matrix import Matrix


class LogisticRegressionNumpy:
    
    def __init__(self, x, y):
        self.intercept = np.ones((x.shape[0], 1))
        self.x = np.concatenate((self.intercept, x), axis=1)
        self.weight = np.zeros(self.x.shape[1])
        self.y = y


    def sigmoid(self, x, weight):
        """Вычисление сигмоиды"""
        z = np.dot(x, weight)
        return 1 / (1 + np.exp(-z))
        

    def loss(self, h, y):
        """Вычисление функции потерь"""
        return np.mean((-y) * np.log(h) + (1 - y) * np.log(1 - h)) 

 
    def gradient_descent(self, X, h, y):
        """Вычисление градиента"""
        return (1/X.shape[0]) * np.dot((h -y ), X)
    

    def fit(self, lr , iterations):
        """Функция обучения"""
        for i in range(iterations):
            sigma = self.sigmoid(self.x, self.weight)
            loss = self.loss(sigma,self.y)
            dW = self.gradient_descent(self.x , sigma, self.y)
            #Updating the weights
            self.weight -= lr * dW  
        return print('fitted successfully to data')
    

    def predict(self, x_new , treshold):
        """Функция предсказания метки класса"""
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







class LogisticRegressionMatrix:
    def __init__(self, x, y):
        self.intercept = Matrix(x.shape[0], 1, fill_random=True, min_val=1, max_val=1)
        self.x = Matrix.concat(self.intercept, x, axis=1)
        self.weight = Matrix(self.x.cols, 1, fill_random=True, min_val=0, max_val=0)
        self.y = y

    def sigmoid(self, x, weight):
        """Вычисление сигмоиды"""
        z = x * weight
        # z = np.dot(x, weight)
        for i in range(z.rows):
            for j in range(z.cols):
                z.data[i][j] = 1 / (1 + np.exp(-1 * z.data[i][j]))
        return z


    def loss(self, h, y):
        """Вычисление функции потерь"""
        result = Matrix(h.rows, h.cols)
        for i in range(h.rows):
            for j in range(h.cols):
                h_new = h.data[i][j]
                result.data[i][j] = y * -1 * np.log(h_new) - (1 - y) * np.log(1 - h_new)
        return  result


 
    def gradient_descent(self, X, h, y):
        """Вычисление градиента"""
        result = (h - y).transpose() * X
        for i in range(result.rows):
            for j in range(result.cols):
                result.data[i][j] *= (1 / X.rows)
        return  result

        return (1/X.shape[0]) * np.dot((h - y), X)
    

    def fit(self, lr , iterations):
        """Функция обучения"""
        for i in range(iterations):
            sigma = self.sigmoid(self.x, self.weight)
            # loss = self.loss(sigma, self.y)
            dW = self.gradient_descent(self.x , sigma, self.y)
            #Updating the weights
            for i in range(self.weight.rows):
                for j in range(self.weight.cols):
                    self.weight.data[i][j] -= lr * dW.transpose().data[i][j]
        return print('fitted successfully to data')
    

    def predict(self, x_new , treshold):

  
        x_new = Matrix.concat(self.intercept, x_new, axis=1)
        result = self.sigmoid(x_new, self.weight)

        y_pred = Matrix(result.rows, 1, fill_random=True, min_val=0, max_val=0)
        for i in range(len(y_pred.data)):
            if result.data[i][0] >= treshold:
                y_pred.data[i][0] = 1
            else:
                continue
        return y_pred


def time_calculation(type: str):
    start_time = datetime.now()
    data = load_breast_cancer()
    x = data.data
    y = data.target

    if type == "numpy":
        regressor = LogisticRegressionNumpy(x, y)
    else:
        regressor = LogisticRegressionMatrix(x, y)

    regressor.fit(0.1, 5000)
    y_pred = regressor.predict(x, 0.5)
    print(f'accuracy -> {format(sum(y_pred == y) / y.shape[0])}')
    print(f'time {type}: {datetime.now() - start_time}')

time_calculation('numpy')
time_calculation('matrix')