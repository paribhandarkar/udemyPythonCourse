# List comprehension are a unique way of quickly creating a list with Python. So if you're ever in a situation where you find yourself using a for loop along with an append statement that goes over and over again through for loop to create a list, list comprehensions are a good alternative to this method.

mystring = 'hello'
mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)

# this is something that's really common for beginners to do. They create an empty list and then they iterate through some other iterable, and then they append whatever object that is or whatever element that is to their list.

# There's actually a more efficient way to do this in Python, and by efficient, I really mean taking up less space and code.

mystring = 'hello'
mylist = [letter for letter in mystring]
print(mylist)

# The logic is essentially a flattened out for loop because we're going to assume that the only action being taken in this for loop is just appending whatever elements you want to your same list.

mylist = [x for x in 'word']
print(mylist)

# if I wanted to grab the square of every number in that range

mylist = [num**2 for num in range(0, 6)]
print(mylist)

# you can also add in if statements into this.
# et's say we only wanted to grab the even numbers from this.

mylist = [num for num in range(0, 11) if num % 2 == 0]
print(mylist)

mylist = [num**2 for num in range(0, 11) if num % 2 == 0]
print(mylist)  # now I only have the square of the even numbers.

# with list comprehension
cel = [0, 10, 20, 34.5]
fah = [(((9/5)*t) + 32) for t in cel]
print(fah)

# without list comprehension
cel = [0, 10, 20, 34.5]
for t in cel:
    print((((9/5)*t) + 32))
    print('\n')

# if else in list comprehension

result = [x if x%2==0 else 'odd' for x in range(0,11)]
print(result)

# you can also do nested loops in a list comprehension.

# without list comprehension
mylist = []
for x in [1,0, 100]:
    for y in [1, 0, 100]:
        mylist.append(x*y)

print(mylist)

# with list comprehension

mylist = [x*y for x in [1,0, 100] for y in [1, 0, 100]]
print(mylist)
