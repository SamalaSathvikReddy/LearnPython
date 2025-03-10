'''
A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.
'''
s1 = "Make a lot of money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

text = input("Enter your comment")

if (s1 or s2 or s3 or s4 in text):
    print("This is spam comment")
else:
    print("your comment is accepted")