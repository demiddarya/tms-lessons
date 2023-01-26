# Пользователь вводит в консоли число секунд.
# Выведите число секунд в виде:
# дни:часы:минуты:секунды.

sec = int(input())
days = int(sec // (24*3600))
sec %= 24 * 3600
hours = int(sec // 3600)
sec %= 3600
min = int(sec // 60)
sec %= 60
print(str(days) + ':' + str(hours) + ':' + str(min) + ':' + str(sec))
