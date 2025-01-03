
def operation_with_numbers():
    while True:
        operation = input("""
Выберите операцию с числами:
1 - Сложение
2 - Вычитание
3 - Умножение
4 - Деление
Введите номер операции: """)
        if operation.isdigit() and (int(operation) == 1 or int(operation) == 2 or int(operation) == 3 or int(operation) == 4):
            operation = int(operation)
            while True:
                while True:
                    while True:
                        number1 = input("Введите первое число: ")
                        if number1.isdigit() and isinstance(int(number1), int):
                            number1 = int(number1)
                            break
                        else:
                            print('Введите норм число!')

                    while True:
                        number2 = input("Введите второе число: ")
                        if number2.isdigit() and isinstance(int(number2), int):
                            number2 = int(number2)
                            break
                        else:
                            print('Введите норм число!')

                    if operation == 1:
                        print(f"Результат: {number1 + number2}")
                        exit()
                    elif operation == 2:
                        print(f"Результат: {number1 - number2}")
                        exit()
                    elif operation == 3:
                        print(f"Результат: {number1 * number2}")
                        exit()
                    elif operation == 4:
                        if number2 == 0:
                            print('На ноль делить нельзя. Введи другое второе число')
                            while True:
                                number2 = input("Введите второе число: ")
                                if number2.isdigit() and isinstance(int(number2), int) and int(number2) != 0:
                                    number2 = int(number2)
                                    break
                                else:
                                    print('Введите норм число!')
                            print(f"Результат: {number1 / number2}")
                            exit()
                    else:
                        print(
                            "Введена некореектная цифра. Попробуйте заново :(")
        else:
            print('Вводите операцию адекватно!')


def operation_with_matrices():
    matrix_1 = []
    matrix_2 = []
    while True:
        rows_1 = (input("Введите количество строк первой матрицы: "))
        if rows_1.isdigit() is False or isinstance(int(rows_1), int) is False:
            print('Введите норм количество строк')
        else:
            rows_1 = int(rows_1)
            break
    while True:
        columns_1 = (input("Введите количество столбцов первой матрицы: "))
        if columns_1.isdigit() is False or isinstance(int(columns_1), int) is False:
            print('Введите норм количество строк')
        else:
            columns_1 = int(columns_1)
            break

    print(f"Введите матрицу размером {rows_1}x{columns_1} через пробел")

    for i in range(rows_1):
        while True:
            row = input(f"Строка {i+1}: ").split(' ')
            if all(element.isdigit() for element in row) and len(row) == columns_1:
                matrix_1.append([int(element) for element in row])
                break
            else:
                if len(row) != columns_1:
                    print("Введено неверное количество элементов!")
                else:
                    print("Введите строку нормально.")
    while True:
        rows_2 = (input("Введите количество строк второй матрицы: "))
        if rows_2.isdigit() is False or isinstance(int(rows_2), int) is False:
            print('Введите норм количество строк')
        else:
            rows_2 = int(rows_2)
            break
    while True:
        columns_2 = (input("Введите количество столбцов второй матрицы: "))
        if columns_2.isdigit() is False or isinstance(int(columns_2), int) is False:
            print('Введите норм количество строк')
        else:
            columns_2 = int(columns_2)
            break

    print(f"Введите матрицу размером {rows_2}x{columns_2} через пробел")

    for i in range(rows_2):
        while True:
            row = input(f"Строка {i+1}: ").split(' ')
            if all(element.isdigit() for element in row) and len(row) == columns_2:
                matrix_2.append([int(element) for element in row])
                break
            else:
                if len(row) != columns_2:
                    print("Введено неверное количество элементов!")
                else:
                    print("Введите строку нормально.")

    operation = (input("""
Выберите операцию с матрицами:
1 - Сложение
2 - Умножение
Введите номер операции: """))
    while True:
        if operation.isdigit() and (int(operation) == 1 or int(operation) == 2):
            if int(operation) == 1:
                summation_matrix(rows_1, columns_1, rows_2,
                                 columns_2, matrix_1, matrix_2)
                break
            elif int(operation) == 2:
                multiplication_matrix(rows_2, columns_1, rows_1,
                                      columns_2, matrix_1, matrix_2)
                break
        else:
            print('Введите норм операцию')


def summation_matrix(rows_1, columns_1, rows_2, columns_2, matrix_1, matrix_2):

    if rows_1 == rows_2 and columns_1 == columns_2:
        sum_matrix = [[] for x in range(rows_1)]

        for i in range(rows_1):
            for j in range(columns_1):
                sum_matrix[i].append(matrix_1[i][j] + matrix_2[i][j])
        print(f"Результат сложения матриц {sum_matrix}")
    else:
        print("Для сложения матрицы должны быть одинакового размера!")


def multiplication_matrix(rows_2, columns_1, rows_1, columns_2, matrix_1, matrix_2):
    if columns_1 == rows_2:
        mult_matrix = [[0]*columns_2 for x in range(rows_1)]
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[0])):
                for k in range(len(matrix_2)):
                    mult_matrix[i][j] += matrix_1[i][k]*matrix_2[k][j]

        print(f"Результат умножения матриц: {mult_matrix}")
    else:
        print(
            "Для умножения количество столбцов первой матрицы должно совпадать с количеством строк второй🥲")