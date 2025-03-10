'''  Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.
l = ["Harry", "Soham", "Sachin", "Rahul"] '''

l = ["Harry", "Soham", "Sachin", "Rahul",'saketh','Sathvik']

for k in l:
    if k[0] == 'S' or k[0].lower() == 's':
        print(f'Hello {k}')
    else:
        pass