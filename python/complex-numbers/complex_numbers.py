import math


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        a, b = self.real, self.imaginary
        c, d = other.real, other.imaginary
        return ComplexNumber(a+c, b+d)

    def __mul__(self, other):
        a, b = self.real, self.imaginary
        c, d = other.real, other.imaginary
        return ComplexNumber(a*c-b*d, b*c+a*d)

    def __sub__(self, other):
        a, b = self.real, self.imaginary
        c, d = other.real, other.imaginary
        return ComplexNumber(a-c, b-d)

    def __truediv__(self, other):
        a, b = self.real, self.imaginary
        c, d = other.real, other.imaginary
        real = (a*c + b*d)/(c**2 + d**2)
        imaginary = (b*c - a*d)/(c**2 + d**2)
        return ComplexNumber(real, imaginary)

    def __abs__(self):
        a, b = self.real, self.imaginary
        return math.sqrt(a**2 + b**2)

    def conjugate(self):
        a, b = self.real, self.imaginary
        return ComplexNumber(a, -b)

    def exp(self):
        exa, b = math.exp(self.real), self.imaginary
        return ComplexNumber(exa*math.cos(b), exa*math.sin(b))

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __repr__(self):
        return f're:{self.real}, im:{self.imaginary}'

