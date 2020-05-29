def private_data(name, last_name, year_of_birth, resindential_city, email, phone):
    return (f'Имя, фамилия: {name}, {last_name}, {year_of_birth} года рождения, место проживания - {resindential_city}, контактные данные: {phone}, {email}.')


name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
year_of_birth = input('Введите год рождения: ')
resindential_city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите номер телефона: ')

print(private_data(name, last_name, year_of_birth, resindential_city, email, phone))
