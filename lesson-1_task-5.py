income = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))

if income > costs:
    print('Компания работает с прибылью.')

    profit = income - costs
    print('Прибыль составляет ' + str(profit) + ' руб.')

    profit_rate = int((profit / income) * 100)
    print('Рентабельность выручки составляет ' + str(profit_rate) + '%.')

    employees_qty = int(input('Введите количество сотрудников компании: '))
    profit_per_employee = int(profit / employees_qty)
    print('Прибыль в расчете на одного сотрудника составляет ' + str(profit_per_employee) + ' руб.')

if income < costs:
    print('Компания работает с убытком.')