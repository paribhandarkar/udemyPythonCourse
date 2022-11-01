# s = set(2, 3, 4 ,1 ,2)
# print(s)
# if you run this you get TypeError: set expected at most 1 argument, got 5

s =set()
s.add(2)
print(s)
s.add(2)
print(s)

#when you're working with sets, it may not be super useful to add them in this manner.Instead, what it's really useful for is maybe casting a list to a set that we only get the unique values.

l = [1,2, 4, 5, 2, 4, 6, 2 ,13, 3, 10]
# s.add(l)
# print(s) # will give error TypeError: unhashable type: 'list'
s = set(l)
print(s)

b = None
print(type(b))