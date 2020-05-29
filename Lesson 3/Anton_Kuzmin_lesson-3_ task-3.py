def my_func(var_1, var_2, var_3):
    my_list = [var_1, var_2, var_3]
    my_list = sorted(my_list)
    my_list.pop(0)
    return (int(my_list[0] + my_list[1]))


var_1 = int(input('Введите первое число: '))
var_2 = int(input('Введите второе число: '))
var_3 = int(input('Введите третье число: '))

print(my_func(var_1, var_2, var_3))
