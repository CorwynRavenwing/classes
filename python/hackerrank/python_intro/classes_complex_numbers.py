import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        return
        
    def __add__(self, no):
        return Complex(
            self.real + no.real,
            self.imaginary + no.imaginary
        )
        
    def __sub__(self, no):
        return Complex(
            self.real - no.real,
            self.imaginary - no.imaginary
        )
        
    def __mul__(self, no):
        A = self.real
        B = self.imaginary
        C = no.real
        D = no.imaginary
        # (ac - bd) + i(ad + bc)
        return Complex(
            A*C - B*D,
            A*D + B*C
        )

    def __truediv__(self, no):
        A = self.real
        B = self.imaginary
        C = no.real
        D = no.imaginary
        # (C+Di)(C-Di)
        divisor = C**2 + D**2
        # (A+Bi)(C-Di)
        # same as mult, with D negated
        return Complex(
            (A*C + B*D)/divisor,
            (-A*D + B*C)/divisor
        )

    def mod(self):
        # SQRT( A**2 + B**2 )
        A2 = pow(self.real, 2)
        B2 = pow(self.imaginary, 2)
        return Complex(
            pow(A2 + B2, 1/2),
            0
        )

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

