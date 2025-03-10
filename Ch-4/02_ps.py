# Write a program to accept marks of 6 students and display them in a sorted manner
marks = []

i1 = int(input('Enter your marks'))
marks.append(i1)
i2 = int(input('Enter your marks'))
marks.append(i2)
i3 = int(input('Enter your marks'))
marks.append(i3)
i4 = int(input('Enter your marks'))
marks.append(i4)
i5 = int(input('Enter your marks'))
marks.append(i5)
i6 = int(input('Enter your marks'))
marks.append(i6)

marks.sort()
print(marks)