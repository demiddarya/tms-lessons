my_list = list(map(str, input().split()))
sep = input()


def my_join(my_list, sep):
    sep_list = sep.join(my_list)
    from functools import reduce
    result = reduce(lambda i, r: i + r, sep_list)
    return result


print(my_join(my_list, sep))
