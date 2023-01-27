# Пользователь вводит число, выведите True если оно простое, иначе False.

n = int(input())
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            result: str = 'False'
            break
        else:
            result = 'True'
    return(result)
print(is_prime(n))
