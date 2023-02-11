letters = list(map(str, input().lower().split()))
vowels = ['a', 'e', 'i', 'o', 'u']


def remove_vowels(letters):
    my_list = list(filter(lambda i: i not in vowels, letters))
    return my_list


print(remove_vowels(letters))
