class Employee:
    increament = 1.10
    emps = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname 
        self.lname = lname
        self.pay = pay

        # Adding Employees
        Employee.emps += 1
    
    def increase(self):
        self.pay = self.pay * self.increament

    @classmethod
    def change_increament(cls, amount):
        cls.increament = amount       
    
        
emp_1 = Employee('Harry','Jack', 56000)
emp_2 = Employee('Rohan', 'Das', 48000) 

print(emp_1.pay)
Employee.change_increament(2)
emp_1.increase()
print(emp_1.pay)