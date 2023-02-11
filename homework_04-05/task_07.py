# Напишите функцию generate_natural_cubes(n),
# которая принимает число n и возвращает список, состоящий из кубов первых n натуральных чисел.
# То есть [1**3, 2**3, 3**3, ..., n**3]. Обязательно использование генераторов списков.

n = int(input())


def generate_natural_cubes(n) -> list:
    a: list = [i ** 3 for i in range(1, n+1)]
    return a


print(generate_natural_cubes(n))
