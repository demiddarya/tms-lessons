#  Напишите функцию get_most_frequent_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое часто встречающееся слово. Если таких слов несколько - верните любое.

text = input("Текст: ")


def get_most_frequent_word(text: str) -> str:
    txt: list[str] = text.split()
    frequent_word: str = ''
    for word in txt:
        if txt.count(word) > txt.count(frequent_word):
            frequent_word = word
    return word


print(get_most_frequent_word(text))
