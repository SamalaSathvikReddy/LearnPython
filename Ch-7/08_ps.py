'''
Write a program to print the following star pattern:
*
**
*** for n = 3
'''

n = int(input('Enter the number: '))

for i in range(0,n):
    no_stars = i + 1
    print('X' * no_stars)