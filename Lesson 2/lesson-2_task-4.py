line = input('Введите строку из нескольких слов, разделенных пробелами: ')

line_words = line.split( )

for i in range(len(line_words)):
    print(i + 1, line_words[i][:10])
