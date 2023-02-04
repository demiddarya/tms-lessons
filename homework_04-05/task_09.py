# Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.

text = input("Текст: ")


def get_longest_word(text: str) -> str:
    txt: list[str] = text.split()
    biggest_word: str = ''
    for word in txt:
        if len(word) > len(biggest_word):
            biggest_word = word
    return word


print(get_longest_word(text))
