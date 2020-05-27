user_answer = int(input('Введите число месяца, от 1 до 12: '))

while True:

    if user_answer < 1 or user_answer >= 13:
        print('Неверно.')
        user_answer = int(input('Введите число месяца, от 1 до 12: '))

    elif user_answer == 1 or user_answer == 2 or user_answer == 12:
        print('Это месяц зимы.')
        break

    elif user_answer == 3 or user_answer == 4 or user_answer == 5:
        print('Это месяц весны.')
        break

    elif user_answer == 6 or user_answer == 7 or user_answer == 8:
        print('Это месяц лета.')
        break

    elif user_answer == 9 or user_answer == 10 or user_answer == 11:
        print('Это месяц осени.')
        break
