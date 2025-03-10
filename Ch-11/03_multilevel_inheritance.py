class Employee:
    a = 10

class Programmer(Employee):
    b = 20

class Manager(Programmer):
    c = 30


a = Manager()
print(a.a,a.b,a.c)
