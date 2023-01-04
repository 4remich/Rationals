import math

class Rational:

    def __init__(self, a: int, b: int):

        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('You must enter an integer number. Repeat the entry, please')
        if b == 0:
            raise ValueError('You cannot divide by 0. Enter another number, please')

        self.a = a
        self.b = b

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        a = self.a * other.a
        b = self.b * other.b
        return Rational(a, b)

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        a = self.a * other.b + other.a * self.b
        b = self.b * other.b
        return Rational(a, b)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        a = self.a * other.b - other.a * self.b
        b = self.b * other.b
        return Rational(a, b)

    def __floordiv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        a = self.a * other.b
        b = other.a * self.b
        return Rational(a, b)

    def __str__(self):

        d = math.gcd(self.a, self.b)
        a = self.a // d
        b = self.b // d

        if a == b:
            return '1'

        if not a % b:
            return f'{a // b}'

        while a < 0 and b < 0:

            if abs(a) < abs(b):
                return f'{abs(a)}/{abs(b)}'

            if abs(a) > abs(b):
                return f'{abs(a) // abs(b)} {abs(a) - abs(a) // abs(b) * abs(b)}/{abs(b)}'

        while a < 0 or b < 0:

            if abs(a) < abs(b):
                return '-' f'{abs(a)}/{abs(b)}'

            if abs(a) > abs(b):
                return '-' f'{abs(a) // abs(b)} {abs(a) - abs(a) // abs(b) * abs(b)}/{abs(b)}'

        if abs(a) > abs(b) and a > 0 and b > 0:
            return f'{abs(a) // abs(b)} {abs(a) - abs(a) // abs(b) * abs(b)}/{abs(b)}'

        return f'{a}/{b}'

x = Rational(-8, 2)
y = Rational(-1, 4)


print(x)
print(y)
print(x * y)
print(x + y)
print(x - y)
print(x // y - 2)

