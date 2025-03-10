class Employee:
    company = "ITC"
    name = 'Default Name'
    def show(self):
        print(f'The name of Employee is {self.name} and the company of employee is {self.company}')


class coder:
    language = 'python'
    def printLanguages(self):
        print(f'out of all language your language is {self.language}')

        

class Programmer(Employee,coder):

    company = "ITC Tech"

    def showLanguage(self):
        print(f'The name of programmer is {self.company} and he knows {self.language} language')


a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguages()