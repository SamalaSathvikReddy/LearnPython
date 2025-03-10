'''
Create a class with a class attribute a; create an object from it and set 'a'
directly using 'object.a = 0'. Does this change the class attribute?
'''

class Main:
    a = 25

object = Main()
object.a = 0

print(object.a)
print(Main.a)

# Class attribute doesn't change.
# A New instance attribute is created.