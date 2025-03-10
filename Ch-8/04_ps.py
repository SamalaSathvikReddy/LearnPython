'''
How do you prevent a python print() function to print a new line at the end.
'''



def sum_n(n):   # In Recurssion make a base condition such that it stop.(go infinately)
    if (n==1):  # If this statement was not there then the sum would get into negative numbers also.
        return 1  
    return sum_n(n-1) + n

print(sum_n(10))

