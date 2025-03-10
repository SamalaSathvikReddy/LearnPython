'''
Write a class 'Calculator' capable of finding square, cube and square root of a
number
'''


class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(self.n*self.n)

    def cube(self):
        print(self.n * self.n * self.n)

    def sqrt(self):
        print(self.n ** 0.5)



p = Calculator(45)
p.square()