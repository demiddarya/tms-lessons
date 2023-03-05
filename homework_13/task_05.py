import re


class WordIterable:
    def __init__(self, string):
        self.string = re.findall(r'[A-Za-zА-Яа-я][a-zа-я]+', string)

    def __iter__(self):
        self.new_word = 0
        return self

    def __next__(self):
        if self.new_word == len(self.string):
            raise StopIteration
        result = self.string[self.new_word]
        self.new_word += 1
        return result


if __name__ == '__main__':
    text = 'мама+ мыла34 раму!'
    for w in WordIterable(text):
        print(w)

    assert ['раз', 'два', 'три', 'четыре'] == [i for i in WordIterable('раз+ два! три89 четыре+')]
