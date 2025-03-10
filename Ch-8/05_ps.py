
'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

# Using for loop

def star(n):
    for i in range(0,n):
        no_stars = n-i
        print('*'*no_stars)

star(7)


# Using Recurssion

def pattern(k):
    if (k == 0):
        return 
    print('*' * k)
    pattern(k-1)

pattern(7)