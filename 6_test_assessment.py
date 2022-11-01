a = 4 * (6 + 5)
print(f"What is the value of the expression {a}")

b = 4 * 6 + 5
print(f"What is the value of the expression {b}")

c = 4 + 6 * 5
print(f"What is the value of the expression {c}")

print(type(3 + 1.5 + 4))

print(2 ** 2) # for square of no.
print(9 ** 0.5) # for square root of no.

s = 'hello'
print(s[1])
print(s[::-1])
print(s[-1])
print(s[4])

l=[0,0,0]
l.append(0)
print(l)

l1 = [0] *3
print(l1)

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

list10 = [5,3,4,6,10]
sorted(list10)
print(list10)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['helloooooo']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# Use a set to find the unique values of the list below:

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

print(3.0 == 3)
print(4**0.5 != 2)


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
print(l_one[2][0] >= l_two[2]['k1'])