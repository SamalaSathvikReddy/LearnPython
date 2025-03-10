# Write a program to find whether a given number is prime or not.

# key idea: prime no is divisible by itself and 1

n = int(input('Enter your number: '))

for i in range(2,n):
    if (n%i == 0):
        print('Number is not prime number ')
        break
else:
    print('Number is prime')
