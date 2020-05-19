user_seconds = int(input('Введите количество секунд: '))

hours = user_seconds // 3600
minutes = (user_seconds % 3600) // 60
seconds = user_seconds % 60

hours = str(hours)
minutes = str(minutes)
seconds = str(seconds)

if len(hours) < 2:
    hours = '0' + hours

if len(minutes) < 2:
    minutes = '0' + minutes

if len(seconds) < 2:
    seconds = '0' + seconds

result = '{}:{}:{}'.format(hours, minutes, seconds)
print(result)
