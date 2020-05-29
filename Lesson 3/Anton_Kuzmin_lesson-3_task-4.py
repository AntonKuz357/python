def my_func(x, y):
    return x ** y


while True:

    x = int(input('Введите действительное положительное число: '))
    y = int(input('Введите целое отрицательное число: '))

    if x > 0 and y < 0:
        print(my_func(x, y))
        break

    else: print('Неверно')
