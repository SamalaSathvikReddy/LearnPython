class Employee:
    language = 'Python'
    branch = 'CS'

    def __init__(self,name,salary,language): # Dunder method is automatically called.
        self.name = name
        self.salary = salary           # name != self.name
        self.language = language

    
    def getInfo(self):
        print(f'Langauge is {self.language} & Branch is {self.branch}')

    @staticmethod    
    def greet():
        print('Hello')

# Once __init__ function is created we must pass the 3 parameters into the object.



sathvik = Employee('SATHVIK',1200000,'Java')
sathvik.name = 'Sathvik'

print(sathvik.salary,sathvik.language)