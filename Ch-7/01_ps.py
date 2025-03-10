# Write a program to print multiplication table of a given number using for loop.

k = int(input("Enter the multiplication: "))

for i in range(1,11):
    print(f'{k} * {i} = {k*i}')
