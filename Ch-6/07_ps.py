'''
Write a program to find out whether a given post is talking about “Harry” or not
'''

text = input("Enter your text:")

if ('Harry' or 'harry' in text.lower()):
    print('It is talking about Harry')
else:
    print('It is not talking about harry')