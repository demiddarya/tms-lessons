letters = list(map(str, input().split()))


def map_to_tuples(letters):
    my_list = list(map(lambda x: (x.upper(), x.lower()), letters))
    return my_list


print(map_to_tuples(letters))
