def my_division(arg_1, arg_2):
    return arg_1 / arg_2


while True:

    arg_1 = int(input('Введите делимое: '))
    arg_2 = int(input('Введите делитель: '))

    if arg_2 == 0:
        print('На ноль делить нельзя.')
        arg_2 = int(input('Введите делитель: '))


    else:
        print(my_division(arg_1, arg_2))
        break
