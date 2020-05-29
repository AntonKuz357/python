text = input('Введите слово: ')


def int_func(text):
    text = str(text.lower())
    return text[0].upper() + text[1:]


print(int_func(text))
