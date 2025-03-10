class Employee:
    language = 'Python'
    branch = 'CS'

# object intiation 
sathvik = Employee()

# Here name and exp are object-attribute (also known as instance attribute).
sathvik.name = 'Sathvik'
sathvik.exp = 5

# Instance attribute >> class attribute.
# Checks in object first.
# Checks in class later.

sathvik.language = 'Javascript'

print(sathvik.language)

