'''
Write a program to find the greatest of four numbers entered by the user
'''


a = float(input('Enter your number:'))
b = float(input('Enter your number:'))
c = float(input('Enter your number:'))
d = float(input('Enter your number:'))

if a > b and c and d:
    print(a)

elif b > c and a and d:
    print(b)

elif c > b and a and d:
    print(c)

elif d > a and b and c:
    print(d)

elif a == b and c and d:
    print(a)

 
# Else statement is not mandatory