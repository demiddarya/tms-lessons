import re


def generate_words(text):
    text = re.findall(r'[A-Za-zА-Яа-я][a-zа-я]+', text)
    for word in text:
        yield word


if __name__ == '__main__':
    text = 'мама+ мыла89 раму!'
    for w in generate_words(text):
        print(w)

    assert ['кошка', 'сидела', 'на', 'окошке'] == [i for i in generate_words('кошка! сидела678 на/ окошке-')]
