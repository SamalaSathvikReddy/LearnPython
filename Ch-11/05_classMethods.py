class Employee:
    a = 10
    @classmethod
    
    # Class method enables you to check directly in class Attribute rather than checking first in instance Attribute.
    # While using @classmethod make sure to change the parameter of function from self to cls.
    
    def show(cls):
        print(f'The value of class Attribute is {cls.a}')

p = Employee()
p.a = 90
p.show()