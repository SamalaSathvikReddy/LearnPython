'''
Write a program to print multiplication table of n using for loops in reversed
order.
'''

n = int(input('Enter your Number: '))

for i in range(0,11):
    print(f'{n} * {10-i} = {n*(10-i)}')