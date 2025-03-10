'''
Create a class 'Programmer' for storing information of few programmers
working at Microsoft.
'''

class Programmer:
    company = 'Microsoft'

    def __init__(self,name,salary,location):
        self.name = name
        self.salary = salary
        self.location = location


p = Programmer('Sathvik',2000000,500097)

print(p.company,p.location,p.name,p.salary)
