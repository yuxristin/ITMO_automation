# программа проверяет является ли число положительным
# или отрицательным и выводит соответствующий результат

num = 3

# так же по пробуем следующие вариации

# num = -5
# num = 0

if num >= 0:
    print('число больше или равно 0')
else:
    print('чик')


def da(str_1: str = 'test',
       str_2: str = 'test1') -> None:
    if str_1 in str_2:
        print('da')
    else:
        print('nicht')
da()
