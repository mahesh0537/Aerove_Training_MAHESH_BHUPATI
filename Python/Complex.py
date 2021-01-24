import math
class Complex:
    def __init__ (self, x, y):
        self.real = x
        self.imaginary = y
    
    def display(self):
        if self.imaginary >= 0:
            print(str(self.real)+' + '+ str(self.imaginary)+ 'i')
        else:
            print(str(self.real)+" - "+str(-1*self.imaginary)+'i')
        
    def conjugate(self):
        return Complex(self.real, -1*self.imaginary)

    def add(self, complex_object):
        return Complex(self.real + complex_object.real, self.imaginary + complex_object.imaginary)

    def sub(self, complex_object):  #b.sub(a) == b - a
        return Complex(self.real - complex_object.real, self.imaginary - complex_object.imaginary)

    def mod(self):
        return (math.sqrt(self.real*self.real + self.imaginary*self.imaginary))

    def multiply(self, complex_object):
        return Complex((self.real*complex_object.real - self.imaginary*complex_object.imaginary),
        (self.real*complex_object.imaginary + self.imaginary*complex_object.real))
    
    def inverse(self):
        magnitude = 1.0/self.mod()
        return Complex(magnitude*self.real, -1*magnitude*self.imaginary)