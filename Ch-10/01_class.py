# Defining class is like a template and when data is give it becomes the object.

# Employee is a class.

# sathvik is object.

# language and branch are class-attributes.

class Employee:
    language = 'Python'
    branch = 'CS'

# object intiation 
sathvik = Employee()

# Here name and exp are object-attribute (also known as instance attribute).
sathvik.name = 'Sathvik'
sathvik.exp = 5

print(sathvik.name,sathvik.language,sathvik.branch,sathvik.exp)