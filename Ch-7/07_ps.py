'''
Write a program to print the following star pattern.
  *       --> 1
 ***      --> 3
*****    --> 5           for n = 3
'''

# Hint:Check for the spaces n-1 space in 1st row and n-2 spaces in 2nd row

n = int(input("Enter the number: "))

for i in range(0, n):
    spaces = (n - i - 1)
    stars = (2 * i + 1) 
    print(" "*spaces + "X"*stars)