'''
Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!
'''

meaning  = input('Enter the hindi word for that which you want meaning:')

word = {
    'kursi':'chair',
    'karab':'bad',
    'kadva':'sour'
}

print(word[meaning])