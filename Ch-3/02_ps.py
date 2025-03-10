# Write a program to fill in a letter template given below with name and date.
'''
letter = 
Dear <|Name|>,
You are selected!
<|Date|>
'''

Name = input('Enter your Name:')
Date = input("Enter today's date")

print(f'''
letter 
Dear {Name},
You are selected!
{Date}

''')