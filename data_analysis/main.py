
from lab1 import operation_with_numbers
from lab1 import operation_with_matrices

while True:
    mode = input("""
Выберите режим работы:
1 - операции с числами
2 - операции c матрицами
Введите номер режима: """)
    if mode != '1' and mode != '2':
        print('Попробуйте заново')
    else:
        if int(mode) == 1:
            operation_with_numbers()
        elif int(mode) == 2:
            operation_with_matrices()
        break
