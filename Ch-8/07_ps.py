'''
Write a python function to remove a given word from a list ad strip it at the same
time.
'''

l = ['Minato','Naruto','Boruto']

def rem(list,word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n       


print(rem(l,'to')) 
    