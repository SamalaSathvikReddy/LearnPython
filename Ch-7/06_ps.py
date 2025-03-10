'''
Write a program to calculate the factorial of a given number using for loop
'''

n = int(input('Enter your number: '))

fac = 1

for i in range(1,n+1):
    fac = fac * i


print(f'The factorial of {n} is {fac}')

# Using While loop

n = int(input("Enter the number: "))

i = 1
fac = 1

while (n>=i):
    fac = fac * i
    i = i + 1

print(f'The factorial of {n} is {fac}')