import math
class Operations:
    def Summ(self,a,b):
        return a + b
    def Diff(self,a,b):
        return a - b
    def Composition(self,a,b):
        return a * b
    def Division(self,a,b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Can't divide by zero!")
 
    def Expo(self,a,b):
        return a ** b
    def Log(self,a):
        return math.log(a)
    def Sin(self,a):
        return math.sin(a)
    def Cos(self,a):
        return math.cos(a)
    '''
    def Tan(self,a):
        return math.tan(a)
    '''