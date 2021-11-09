class Complex:

    def __init__(self,real,imag):
        
        self.real = real
        self.imag = imag

    def __add__(self,next):

        real = self.real + next.real
        imag = self.imag + next.imag

        return ("%.3f + %.3f i") % (real,imag)

a = Complex(1,2)
b = Complex(2,3)

print(a+b)
