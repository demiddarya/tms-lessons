# Напишите функцию is_year_leap, которая принимает число (год)
# и возвращает True если год високосный
# (см. комментарий к слайда), False если нет.

y = int(input())


def is_year_leap(y) -> bool:
    return y % 4 == 0 and y % 100 != 0


print(is_year_leap(y))
