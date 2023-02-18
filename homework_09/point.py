# 1. Создайте файл point.py. Делайте задание в этом файле.
# 2. Вам необходимо создать класс Point (точка на координатной плоскости), у которой будет два поля: x, y.
# 3. Добавьте метод distance_to_zero - который будет возвращать расстояние от точки до начала координат (0, 0).
# Например для точки Point(3, 4) это расстояние будет равно 5 (по теореме Пифагора)
# 4. Добавьте метод distance_to_point, который принимает другую точку, и ищет расстояние между ними.
# 5. Скопируйте код из комментария к слайду и проверьте, что он выводит ожидаемый результат.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        return (self.x**2 + self.y**2)**0.5

    def distance_to_point(self, p):
        return ((p.x - self.x)**2 + (p.y - self.y)**2)**0.5


p1 = Point(3, 4)
p2 = Point(3, 10)
p3 = Point(10, 10)

print('Distance between p1 and zero point:', p1.distance_to_zero())
print('Distance between p2 and zero point:', p2.distance_to_zero())
print('Distance between p3 and zero point:', p3.distance_to_zero())
print('Distance between p1 and p1:', p1.distance_to_point(p1))
print('Distance between p1 and p2:', p1.distance_to_point(p2))
print('Distance between p2 and p1:', p2.distance_to_point(p1))
print('Distance between p1 and p3:', p1.distance_to_point(p3))
print('Distance between p2 and p3:', p2.distance_to_point(p3))
