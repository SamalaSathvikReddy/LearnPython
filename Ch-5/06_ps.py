'''
Create an empty dictionary. Allow 3 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.
'''

s = {}
f1 = input('Enter your name:')
k1 = input('Enter your language')
f2 = input('Enter your name:')
k2 = input('Enter your language')
f3 = input('Enter your name:')
k3 = input('Enter your language')


s.update({f1:k1,f2:k2,f3:k3})
print(s)
