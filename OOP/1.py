class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname 
        self.lname = lname
        self.pay = pay
        
emp_1 = Employee('Harry','Jack', 56000)
emp_2 = Employee('Rohan', 'Das', 48000)

print(emp_1.fname)