age = int(input("Enter your age:"))

# If statement 1(if can be independent)
if(age%2 == 0):
    print('age is even')
# End of if statement 1


# If statement 2 linked with else
if(age>=18):
    print('you are above the age of consent')
elif(age<0):
    print('You are enterning a invalid age')
else:
    print('you are below the age of consent')


# End of if statement 2
# Elif and Else can't be independent


print('End of program')

