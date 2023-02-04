# Напишите функцию generate_squares, которая принимает произвольное количество аргументов и возвращает список,
# состоящий из их квадратов. То есть generate_squares(1, 2, 3) -> [1, 4, 9]

def generate_squares(*nums) -> list:
    res: list = [i ** 2 for i in nums]
    return res


print(generate_squares(1, 3, 5, 7))
print(generate_squares(4, 7, 9, 5, 10))
