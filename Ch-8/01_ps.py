'''
Write a program using functions to find greatest of three numbers.
'''

def greatest(a,b,c):
    if (a > b and c):
        print(f'{a} is the greatest number.')
    elif (b > c and a):
        print(f'{b} is the greatest number.')
    elif (c > a and b):
        print(f'{c} is the greatest number.')
    else: # a = b = c
        print(f'{a} is the greatest number.')


greatest(22,654,1234567898765412345679876543123456798765432)