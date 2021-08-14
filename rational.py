import math
import sys

class Rational:
    def __init__(self, p, q):
        self.numerator = p
        self.denominator = q

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def negate(self):
        if self.numerator < 0 and self.denominator < 0:
            new_numerator = self.numerator * -1
            new_denominator = self.denominator
        if self.numerator > 0 and self.denominator > 0:
            new_numerator = self.numerator * -1
            new_denominator = self.denominator
        elif self.numerator < 0 and self.denominator > 0:
            new_numerator = self.numerator * -1
            new_denominator = self.denominator
        elif self.numerator > 0 and self.denominator < 0:
            new_numerator = self.numerator * -1
            new_denominator = self.denominator * -1
        return Rational(new_numerator, new_denominator)

    def invert(self):
        if self.numerator == 0: 
            return None
        else:
            new_numerator = self.denominator
            new_denominator = self.numerator
        return Rational(new_numerator, new_denominator)

    def reduce(self):
        if self.numerator != 0:
            divisor = math.gcd(self.numerator, self.denominator)
            new_numerator = self.numerator // divisor
            new_denominator = self.denominator // divisor
        return Rational(new_numerator, new_denominator)
        if self.numerator == 0:
            return None

    def add(self, num):
        new_numerator_1 = self.numerator * num.denominator
        new_numerator_2 = num.numerator * self.denominator
        new_denominator = self.denominator * num.denominator
        result = Rational(new_numerator_1 + new_numerator_2, new_denominator)
        return result.reduce()

    def mul(self, num):
        new_numerator = self.numerator * num.numerator
        new_denominator = self.denominator * num.denominator
        result = Rational(new_numerator, new_denominator)
        return result.reduce()

    def exp(self, n):
        new_numerator = self.numerator 
        new_denominator = self.denominator
        if n == -1:
            return Rational(new_denominator, new_numerator)
        elif n == 0:
            return Rational(1, 1)
        else:
            return Rational(new_numerator**n, new_denominator**n)

def geometric(n, a, r):
    if n == 1: 
        a = a.mul(r.exp(n)) 
        return a
    else: 
        return a.mul(r.exp(n)) 
        

