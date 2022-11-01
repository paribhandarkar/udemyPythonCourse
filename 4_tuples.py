t = ('one',2,3, 'a', 'a', 'a', 'a', 'a', 'a', 'b')
print(type(t))
print(t[1])
print(t.count('a'))
print(t.index('a')) # this returns back the very first time a appears in your tuple.

l = ['hello', 'hi', 'hey']
print(type(l))
l[1] = 'bye'
print(l) # therfore list is mutable

print(t)
# t[2] = 'new value'
# print(t)
# will give type error as tuples are immutable