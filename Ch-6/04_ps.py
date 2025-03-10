'''
Write a program to find whether a given username contains less than 10
characters or not.
'''

user_name = input("Enter your username:")

if (len(user_name) < 10):
    print("It has less than 10 character.")
else:
    print('All is Well')
