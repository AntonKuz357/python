my_list = []
num = 0
i = 0
num_max = int(input('Введите количество элементов списка: '))

while True:
    my_list.append(input('Введите элемент списка: '))
    num += 1
    if num == num_max:
        print('Заполнение списка окончено.')
        break

while i < len(my_list):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
    if len(my_list) - i == 1:
        break

print(my_list)
