'''
fac(0) = 1
fac(1) = 1
fac(n) = n * n-1 * n-2 ........3 * 2 * 1
fac(n) = n * fac(n-1)
fac(n) = n * fac(n-2)

'''



'''

Be extremely careful while working with recursion to ensure
that the function doesn't infinitely keep calling itself.


'''


n = int(input('Enter your Number: '))

def fac(n):
    if (n==0) or (n==1):
        return 1
    return n * fac(n-1)

print(f'The factorial of {n} is {fac(n)}')