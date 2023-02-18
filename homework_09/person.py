# 1. Создайте файл person.py, делайте задание в этом файле.
# 2. Создайте класс Person. У класса должно быть три поля: full_name, age, gender, которые должны заполняться
# в конструкторе. Будем считать что поле gender имеет тип str и может быть либо 'M' (male), либо 'F' (female).
# 3. Добавьте в класс метод print_person_info, который печатает на экран строку:
# "Person: {full_name} ({gender}), {age} years old"
# 4. Добавьте метод get_birth_year, которая возвращает год рождения человека (рассчитанное как 2023 - age)
# 5.* Замените цифру 2023 на текущий год (чтобы ваша программа работала правильно даже через год).
# Текущий год можно взять с помощью модуля datetime (пример).
import datetime


class Person:
    def __init__(self, fn, a, g):
        self.full_name = fn
        self.age = a
        self.gender = g

    def print_person_info(self):
        print(f'Person: {self.full_name} ({self.gender}), {self.age} years old')

    def get_birth_year(self):
        now = datetime.datetime.now()
        return now.year - int(self.age)
