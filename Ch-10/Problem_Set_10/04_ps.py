'''
Add a static method in problem 2, to greet the user with hello.

'''

class Main:
    a = 25

    @staticmethod
    def greet():
        print('Hello')


object = Main()
object.a = 0

print(object.a)
Main.greet()
Main.a