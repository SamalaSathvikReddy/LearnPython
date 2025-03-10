class Employee:
    company = "ITC"

    def show(self):
        print(f'The name of Employee is {self.name} and the salary of employee is {self.salary}')

# Now if we want to create another class programmer in which it should contain all the methods of class Employee.
# There are 2 ways:
    # copy the code.
    # Inherit the code for the class Employee.

# Inheritance

# Where Employee is a parent class and Programmer is derived class.

class Programmer(Employee):

    company = "ITC Tech"

    def showLanguage(self):
        print(f'The name of programmer is {self.name} and he knows {self.language} language')

a = Employee()
b = Programmer()

print(a.company,b.company)
