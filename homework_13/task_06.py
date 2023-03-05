def generate_words(text):
    text = [word for word in text.split()]
    for word in text:
        yield word


if __name__ == '__main__':
    text = 'мама мыла раму'
    for w in generate_words(text):
        print(w)

    assert ['кошка', 'сидела', 'на', 'окошке'] == [i for i in generate_words('кошка сидела на окошке')]