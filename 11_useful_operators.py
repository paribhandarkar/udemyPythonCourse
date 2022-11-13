# basically a generator is just a special type of function that will generate information instead of saving it all to memory. So this is a more efficient way of generating these numbers instead of having a giant list sorted memory.
# range
for num in range(5):
    print(num)

for num in range(2, 7):
    print(num)

for num in range(2, 10, 2):
    print(num)

print(type(range(0, 11, 2)))

print(list(range(0, 11, 2)))
# if I actually want the actual list of numbers, what I can do is cast it to a list and then I get back the list of numbers.

# enumerate function

index_count = 0

for letter in 'abcde':
    print(f'the index {index_count} is for letter {letter}')
    index_count += 1

# this is such a common operation that what we're going to do is use the 'enumerate' function to replicate this. And the reason this is very common is because a lot of times you will want to have some sort of counter for how many times have you gone through this for loop or what index position you are at in this particular string?

word = 'abcde'

for letter in enumerate(word):
    print(letter)

# And now when I run this I get back tuples. So this is basically doing that index count for us automatically in the form of tuples and as we know we have tuple unpacking from the for loop lecture.

word = 'akjdk'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# zip function

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
print(zip(mylist1, mylist2))
# Now, if I just run this, I don't get back anything. It just says, hey, you have this zip generator waiting for you at this 0x0000024A7B480040 location in your memory

# now if we actually iterate through it we get tuples
for item in zip(mylist1, mylist2):
    print(item)

#  we can do this with more that 2 lists

mylist3 = ['sa', 're', 'ga', 'ma', 'pa']
for item in zip(mylist1, mylist2, mylist3):
    print(item)

# But if you actually just want to get the list itself, you can just cast it using list.
print(list(zip(mylist1, mylist2, mylist3)))

# we can also use tuple unpacking
for a, b, c in zip(mylist1, mylist2, mylist3):
    print(b)
    print(a)
    print(c)
    print('\n')


# membership operator

check = 'x' in [1, 2, 3]
print(check)

check = 3 in [1, 2, 3]
print(check)
# So this is a really nice way to quickly check if something is in a list.

# This also works in dictionaries as well for their keys.
check = 'mykey' in {'mykey': 123}
print(check)

d = {'mykey': 123}
check1 = 345 in d.keys()
print(check1)


# min and max function

# keep in mind because often it's going to be very tempting to use min and max as keywords, but they're already built in functions in Python, so you should not use those. And that's denoted by the fact that they show you syntax highlighting.
mylist4 = [1, 3, 5, 23, 75, 122, 8]
print(min(mylist4))
print(max(mylist4))

# random library

from random import shuffle
# So what this is saying is, hey, from that random library that's built into Python, import the shuffle function
#random is built in

mylist5 = [3, 5, 23, 75, 122]
random_list = shuffle(mylist5)
print(mylist5) #its now shuffled

# should also note that it's actually not returning anything.
print(type(random_list))
# So this is an in place function, meaning it operates in place on that list.

# There's also a really nice function for grabbing a random integer.
from random import randint
print(randint(0, 200))
# it returns back some random integer.

# to accept user input
# input function

# So we use the special keyword input function and then we have the text that wants to show up when we actually ask the user for input.

result = input('enter a no. ')
print(f'the entered no. is {result}')

# The thing you've got to watch out for is that input always accepts anything that's passed into it as a string.

