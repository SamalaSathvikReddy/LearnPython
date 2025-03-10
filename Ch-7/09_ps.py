'''
Write a program to print the following star pattern.
* * *
*   *       for n = 3
* * *

* * * *
*     *     for n = 4
*     *   
* * * *

'''

n = int(input("Enter your Number: "))

for i in range(0,n+1):
  if (i==0) or (n==i):
    no_stars = n
    no_spaces = 0
    print(' '*no_spaces+'*'*no_stars)

  else:
    no_stars = 1
    no_spaces = n-2
    print('*'*no_stars+' '*no_spaces+'*'*no_stars)