class Employee:
    increament = 1.10
    emps = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname 
        self.lname = lname
        self.pay = pay
        self.increament = 1.4

        # Adding Employees
        Employee.emps += 1
    
    def increase(self):
        self.pay = self.pay * Employee.increament

    def more_increament(self):
        self.pay = self.pay * self.increament
    
        
emp_1 = Employee('Harry','Jack', 56000)
emp_2 = Employee('Rohan', 'Das', 48000) 

print(emp_1.__dict__)
emp_1.increase()
print(emp_1.pay)

emp_2.more_increament()
print(emp_2.pay)

print(emp_1.__dict__)

print(Employee.emps)