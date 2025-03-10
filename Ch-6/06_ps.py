'''
Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F
'''

marks = int(input('Enter your marks:'))

if (100 >= marks > 90):
    print('Your grade is Ex')
elif (90 >= marks > 80):
    print('Your grade is A')
elif (80 >= marks > 70):
    print('Your grade is B')
elif (70 >= marks > 60):
    print('Your grade is C')
elif (60 >= marks > 50):
    print('Your grade is D')
elif (marks<50):
    print('Your grade is F')