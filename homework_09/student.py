# 1. Создайте файл student.py. Делайте задание в этом файле.
# 2. Создайте класс Student, с полями full_name, agerage_mark (средняя оценка).
# 3. Добавьте в класс метод get_scholarship, который подсчитывает и возвращает стипендию данного студента по алгоритму:
# Если средняя оценка < 6 - вернуть 60 (рублей)
# Если средняя оценка >= 6, но < 8 - вернуть 80 (рублей)
# Если средняя оценка >= 8 - вернуть 100 (рублей)
# 4. Добавить в класс метод is_excellent, который возвращает bool:
# True, если средняя оценка >= 9
# False, иначе
class Student:
    def __init__(self, name, mark):
        self.full_name = name
        self.average_mark = mark

    def get_scholarship(self):
        if self.average_mark < 6:
            return 60
        elif 6 <= self.average_mark < 8:
            return 80
        elif self.average_mark >= 8:
            return 100

    def is_excellent(self):
        return self.average_mark >= 9
