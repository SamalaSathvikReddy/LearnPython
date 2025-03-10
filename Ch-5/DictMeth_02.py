score = {
    'Shewag':100,
    'Sachin':150,
    'Dravid':200,
    'laxman':[70,60]
    }

# .items() turns into tuples
print(score.items())

# .keys()
print(score.keys())

# .values()
print(score.values())

# .update()
score.update({'Dravid':180,'Ganguly':120})
print(score)

'''.get()
print(score.get('laxman2'))--> returns None
print(score['laxman2']) -->error occurs'''

# .pop()
score.pop('Shewag')
print(score)

# .popitem()
score.popitem() #removes last item
print(score)