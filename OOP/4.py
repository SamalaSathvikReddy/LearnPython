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

    @classmethod
    def from_str(cls, data):
        fname, lname, pay = data.split('-') 
        return Employee(fname, lname, pay)      
    
        
emp_1 = Employee('Harry','Jack', 56000)
emp_2 = Employee('Rohan', 'Das', 48000)
emp_3 = Employee.from_str('Allen-Jackson-72000')

print(Employee.emps)
print(emp_3.__dict__)