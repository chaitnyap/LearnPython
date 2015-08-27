from __future__ import division
import math
class ComplexNumber(object):
    '''class for complex numbers'''
    def __init__(self, C, D):
        self.C = C
        self.D = D
        
    def __str__(self):
        if self.C !=0 and self.D !=0:
            s = str("%.2f" %self.C)
            if self.D > 0:
                s += ' + ' + str("%.2fi" %abs(self.D))
            elif self.D < 0:
                s += ' - ' + str("%.2fi" %abs(self.D))
        elif self.D == 0:
            s = str("%.2f" %self.C)
        elif self.C == 0:
            s = str("%.2fi" %self.D)
        return s

    def __add__(self, other):
        r = self.C + other.C
        ir = self.D + other.D
        return ComplexNumber(r, ir)
    
    def __sub__(self, other):
        r = self.C - other.C
        ir = self.D - other.D
        return ComplexNumber(r, ir)
    
    def __mul__(self, other):
        r = (self.C * other.C) - (self.D * other.D)
        ir = (self.C * other.D) + (self.D * other.C)
        return ComplexNumber(r, ir)
    
    def __truediv__(self, other):
        r = ((self.C * other.C) + (self.D * other.D)) / ((other.C ** 2) + (other.D ** 2))
        ir = ((self.D * other.C) - (self.C * other.D)) / ((other.C ** 2) + (other.D ** 2))
        return ComplexNumber(r, ir)
    
    def modulus(self):
        return "%.2f" %math.sqrt((self.C ** 2) + (self.D ** 2))

r, ir = map(float, raw_input().strip().split())
c1 = ComplexNumber(r, ir)
r, ir = map(float, raw_input().strip().split())
c2 = ComplexNumber(r, ir)
print c1 + c2
print c1 - c2
print c1 * c2
print c1 / c2
print c1.modulus()
print c2.modulus()
