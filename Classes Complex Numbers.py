import math

class ComplexNo(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return ComplexNo(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return ComplexNo(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return ComplexNo(real, imaginary)

    def __div__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * ComplexNo(no.real, -no.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return ComplexNo(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return ComplexNo(real, 0)
# can also use __repr__ in place of __str__
    def __str__(self):
        return "{0:.2f}{1:+.2f}i".format(self.real,self.imaginary)

C = map(float, raw_input().split())
D = map(float, raw_input().split())
x = ComplexNo(*C)
y = ComplexNo(*D)
final = [x+y, x-y, x*y, x/y, x.mod(), y.mod()]
print '\n'.join(map(str, final))