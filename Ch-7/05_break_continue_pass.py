# Break exits loop force fully
for i in range(0,100):
    if (i == 35):
        break
    print(i)
    
for i in range(0,50):
    if (i == 35):
        continue # Dosen't execute code below it goes back to loop again when condition(i==35) is satisfied
    print(i)

# Pass is used for removing indentation error, It is a null statement
for i in range(0,50):
    pass