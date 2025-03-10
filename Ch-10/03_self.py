class Employee:
    language = 'Python'
    branch = 'CS'

    # This is a method.
    # self is must.

    def getInfo(self):
        print(f'Langauge is {self.language} & Branch is {self.branch}')

    @staticmethod
    # As greet function doesnot have interaction or use of object.
    # we use @staticmethod to avoid the object to pass through the function.
    def greet():
        print('Hello')




sathvik = Employee()
sathvik.name = 'Sathvik'
sathvik.exp = 5

# sathvik.getInfo() ---> Employee.getInfo(sathvik)
# for this we get a argument error so we give argument to function inside the class as self

sathvik.getInfo()
sathvik.greet()