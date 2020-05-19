number = int(input("Введите целое положительное число: "))

while number <= 0:

    print("Неправильно")
    number = int(input("Введите целое положительное число:  "))

if number > 0:

    digits = sorted(list(str(number)))
    the_biggest = digits[-1]
    print('Самая большая цифра в числе - это ' + the_biggest + '.')
