# super().[function of parent class]

# This will also help to run the function of parent class.

class Employee:
    a = 10
    def __init__(self):
        print('Constructor for Employee.')    

class Programmer(Employee):
    b = 20
    def __init__(self):
        super().__init__()
        print('Constructor for Programmer.')

class Manager(Programmer):
    c = 30
    def __init__(self):
        super().__init__()
        print('Constructor for Manager.')


o = Manager()
o.a