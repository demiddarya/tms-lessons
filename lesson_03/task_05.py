# Пользователь вводит в консоль строку.
# Если выведенная строка является палиндромом - выведите True.
# Если не является - выведите False.

slovo = str(input())
a = slovo[::-1]
print(slovo == a)
