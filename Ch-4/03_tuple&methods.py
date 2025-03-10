# Tuples are similar to list , but they are immutable.
a = () # Empty tuple

b = (1)
print(type(b)) # it is integer

# for single element tuple
c = (1,)
print(type(c))

# Methods

tup = (1,2,4,6,6,0)
print(tup.index(0))
print(tup.count(6))
print(2 in tup)
print(5 in tup)
