import math

class Rational:

    def __init__(self, a: int, b: int):

        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('You must enter an integer number. Repeat the entry, please')
        if not b:
            raise ZeroDivisionError('You cannot divide by 0. Enter another number, please')

        self.a = a
        self.b = b

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        sign = 1 if self.a * self.b > 0 else -1

        a = self.a * other.a
        b = self.b * other.b
        return Rational(sign * a, b)

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        sign = 1 if self.a * self.b > 0 else -1

        a = self.a * other.b + other.a * self.b
        b = self.b * other.b
        return Rational(sign * a, b)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        sign = 1 if self.a * self.b > 0 else -1

        a = self.a * other.b - other.a * self.b
        b = self.b * other.b
        return Rational(sign * a, b)

    def __floordiv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        sign = 1 if self.a * self.b > 0 else -1

        a = self.a * other.b
        b = other.a * self.b
        return Rational(sign * a, b)

    def __str__(self):

        sign = '' if self.a * self.b > 0 else '-'
        a, b = abs(self.a), abs(self.b)
        d = math.gcd(self.a, self.b)
        a //= d
        b //= d

        if a == b:
            return f'{sign}1'
        if b == 1:
            return f'{sign}{a}'
        if a > b:
            return f'{sign}{a // b} {a - a // b * b}/{b}'
        return f'{sign}{a} / {b}'

x = Rational(1, 2)
y = Rational(-1, 4)


print(x)
print(y)
print(x * y)
print(x + y)
print(x - y)
print(x // y)
print(x - 2 - y)

