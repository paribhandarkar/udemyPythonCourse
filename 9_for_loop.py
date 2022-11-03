# Syntax for for loop
my_iterable = [1,2,3] #We start off with this statement and this is just an assignment. We're saying, my_iterable. We're choosing that as a variable name. This could be my_list, my items, my dogs, whatever you want is equal to. And in this case, we're choosing a list.
for item_name in my_iterable: #So item_name is a variable name that you can choose. That's going to be a bit of a placeholder for every single item in your iterable object.So in this case, the item_name actually represents the numbers in that list.
    print(item_name)

# example 1

myList = [7, 17, 27, 37]
for listContent in myList:
    print(listContent)

# example 2

# We can still execute some block of code for every single item in this list, even if the code itself is unrelated to the item. So I can print. Hello. For every item in that list.

myList = [7, 17, 27, 37]
for listContent in myList:
    print('hello')

# example 3

myList1 = [1,2,3,4,5,6,7,8,9,10]
for listContent1 in myList1:
    if listContent1 % 2 == 0:
        print(f'Even number: {listContent1}')    
    else:
        print(f'Odd number: {listContent1}')   

# example 4

sum_list = 0
for listContent in myList:
    sum_list += listContent
print(sum_list)

# example 5

# strings are a sequence, so that means we can iterate through them and we'll be accessing

mystring = 'hiiii'
for stringLetter in mystring:
    print(stringLetter)

# we can also do

for stringLetter in 'hiiii':
    print(stringLetter)

# So a lot of times what people do as they get more advanced in Python, for some reason they want to iterate something a certain amount of times. So imagine I wanted to print. Cool for as many times as there are characters here.
# What they do is instead of assigning this variable name, they just use an underscore. And that's really common syntax for when you don't intend to actually use that variable name as you iterate through.

for _ in 'hiiii':
    print('cool')


# tuple unpacking
# tuples have a little bit of a special quality when it comes to for loops. So if you're iterating through a sequence that contains itself tuples, the item can be used with tuple unpacking.

myList2 = [(1,2), (3,4), (5,6), (7,8)] # This sort of data structure is extremely common in Python. And later on we're going to see that a lot of built in Python functions actually take advantage of this built in structure and return back tuples inside of a list. And the reason for that is something called tuple unpacking.
for tup in myList2:
    print(tup)

#or 

for (a,b) in myList2:
# for a,b in myList2:
    print(a,b)
    print(a)
    print(b)

# iterating through dictionary

d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
for item in d:
    print(item)
# Notice that by default when you iterate through a dictionary, you only iterate through the keys.

d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
for item in d.items():
    print(item)
# When you run this, you get back tuple pairs. which means we can use the same tuple unpacking technique we just discussed.

d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
for key, value in d.items():
    print(value)

# So by default when you iterate through a dictionary, it's going to be the keys. If you want to iterate through the items you can use tuple unpacking to grab both keys and values.

# If you only want the values themselves.

d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
for value in d.values():
    print(value)

#dictionaries are technically unordered. This is a very small dictionary, so it looks like everything's going in order. But if you have a very large dictionary, there's no guarantee that things are going to be sorted or in any sort of order.


