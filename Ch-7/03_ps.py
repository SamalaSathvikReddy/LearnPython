'''
Write a program to print multiplication table of a given number using while loop.
'''

k = int(input('Enter your Number: '))
i = 0

while (i<11):
    print(f'{k} * {i} = {k*i}')
    i += 1