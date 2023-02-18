# 1. Создайте файл university.py. Делайте задание в этом файле.
# 2. Импортируйте класс Student из первого задания
# from student import Student
# 3. Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.
# 4. Посчитайте суммарную стипендию для всех студентов.
# 5. Посчитайте количество отличников (используйте метод is_excellent).
# 6.* Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count
from student import Student
students = [
           Student('Slava', 9),
           Student('Andrew', 5),
           Student('Angelina', 7),
           Student('Katya', 8)
]


def calc_sum_scholarship():
    sum_of_scholarships = students[0].get_scholarship()

    for i in students[1:]:
        sum_of_scholarships += i.get_scholarship()
    return sum_of_scholarships


def get_excellent_student_count():
    counter = 0
    for i in students:
        if i.is_excellent() is True:
            counter += 1
        return counter


print(calc_sum_scholarship())
print(get_excellent_student_count())
