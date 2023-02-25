import math


class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        self.__normalize()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'

    def __mul__(self, other: 'Rational'):
        return Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __floordiv__(self, other: 'Rational'):
        return Rational(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __add__(self, other):
        n_numerator = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        n_denominator = self.__denominator * other.__denominator
        return Rational(n_numerator, n_denominator)

    def __sub__(self, other):
        n_numerator = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        n_denominator = self.__denominator * other.__denominator
        return Rational(n_numerator, n_denominator)

    def __gt__(self, other: 'Rational'):
        return self.__numerator / self.__denominator > other.__numerator / other.__denominator

    def __lt__(self, other: 'Rational'):
        return self.__numerator / self.__denominator < other.__numerator / other.__denominator

    def __ge__(self, other: 'Rational'):
        return self.__numerator / self.__denominator >= other.__numerator / other.__denominator

    def __le__(self, other: 'Rational'):
        return self.__numerator / self.__denominator <= other.__numerator / other.__denominator

    def __eq__(self, other: 'Rational'):
        return self.__numerator / self.__denominator == other.__numerator / other.__denominator

    def __ne__(self, other: 'Rational'):
        return self.__numerator / self.__denominator != other.__numerator / other.__denominator

    def __normalize(self):
        if self.__denominator < 0 and self.__numerator < 0 or self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1

        gcd = math.gcd(self.__numerator, self.__denominator)
        if gcd > 1:
            self.__numerator //= gcd
            self.__denominator //= gcd


if __name__ == '__main__':
    num = Rational(3, 16)
    num2 = Rational(3, 8)
    assert num.numerator == 3
    assert num.denominator == 16
    assert num2.denominator == 8
    assert str(num) == '3 / 16'
    assert Rational(1, 2) > Rational(1, 3)
    assert Rational(1, 5) < Rational(3, 4)
    assert Rational(1, 4) >= Rational(1, 100)
    assert Rational(1, 45) >= Rational(1, 45)
    assert Rational(1, 400) <= Rational(1, 100)
    assert Rational(1, 4) <= Rational(1, 4)
    assert Rational(9, 45) == Rational(1, 5)
    assert Rational(19, 56) != Rational(1, 45)
    assert Rational(1, 4) + Rational(1, 4) == Rational(1, 2)
    assert Rational(3, 2) - Rational(1, 2) == Rational(1, 1)
    assert Rational(4, 9) * Rational(6, 12) == Rational(2, 9)
    assert Rational(7, 17) // Rational(49, 34) == Rational(2, 7)
    print(Rational(2, 4))
    print(Rational(-1, -2))
    print(Rational(3, -9))
    print(Rational(1, 4) * (Rational(3, 2) + Rational(1, 8)) + Rational(156, 100))
