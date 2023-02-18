# 1. Создайте файл friends.py. Делайте задание в этом файле.
# 2. Импортируйте класс Person из первого задания
# from person import Person
# 3. Создайте переменную my_friends - список из объектов класса Person.
# Добавьте в него некоторое количество вымышленных друзей с разными именами, возрастом и полом.
# 4. Выведите информацию о каждом друге на экран.
# 5.* Найдите среди друзей самого старшего, выведите информацию о нём на экран.
# 6.* Выведите на экран информацию о всех друзьях мужского пола (можно использовать функцию filter,
# либо генератор списков).
# 7.* Заверните код из пунктов 5 и 6 в функции get_oldest_pearson и filter_male_person соответственно.
from person import Person


my_friends = [
             Person('Petr Petrov', 20, 'M'),
             Person('Katya Utkina', 23, 'F'),
             Person('Sasha Ivanov', 18, 'M'),
             Person('Sasha Skirmunt', 25, 'F')
]


def get_oldest_person():
    older = my_friends[0]

    for j in my_friends[1:]:
        if j.age > older.age:
            older = j

    older.print_person_info()


def filter_male_person():
    male = list(filter(lambda person: person.gender == 'M', my_friends))

    for i in male:
        i.print_person_info()


my_friends[0].print_person_info()
my_friends[1].print_person_info()
my_friends[2].print_person_info()
my_friends[3].print_person_info()
get_oldest_person()
filter_male_person()
