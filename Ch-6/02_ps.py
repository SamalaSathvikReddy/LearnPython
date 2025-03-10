'''
Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user. Let maximum marks in each subject be 100
'''
marks_1 = int(input("Enter your marks"))
marks_2 = int(input("Enter your marks"))
marks_3 = int(input("Enter your marks"))

total_marks = marks_1 + marks_2 + marks_3
total_percentage = total_marks * 100/300 

if total_percentage >= 40 and marks_1 and marks_2 and marks_3 >= 33:
    print("Congratulations, Yoou're Pass")
else:
    print("You have failed")