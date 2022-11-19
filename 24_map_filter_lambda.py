'''
i want to apply the square function to every single number in my nums list. Well, one way I could do that is use a for loop, but that may take a while and it's a lot of code.

Instead, what I want to do is take advantage of that map function.

So the map function, what you end up doing is you pass in yhe function that you want to map to every single element or item in this list.
'''

def square(nums):
    return nums**2

my_nums = [1,2,3,4,5,6]

print(map(square, my_nums))

'''
when I just run it like this. I get back this kind of cryptic statement which says, Hey, you have a map at this location <0x00000288687BB550> on your computer.

So this is a memory location. This by itself isn't super useful.

What we need to do is actually iterate through this.
'''

for item in map(square, my_nums):
    print(item)

# And what this does is it generates applying this square function to every single item in this list.

# another way
print(list(map(square, my_nums)))

#another example

def splicer(name):
    if len(name)%2 == 0:
        return 'even'
    else:
        return name[0]

names = ['pari', 'asmi', 'aarti', 'mansi', 'hitika']

print(list(map(splicer, names)))

'''
When you're using the map function, notice how I'm passing in square and how I'm passing in splicer.
I'm actually not calling them to execute inside of this map because map by itself is later on going to execute them.

So that means when you pass in the function here, it's a map.
You do not add in the open and close parentheses.

Instead you just pass in the function itself as an argument.

And that's a really important detail to note here.

Otherwise, you'll end up getting some sort of type error.

we just want to pass in the function itself.

We don't want to execute the function.

We'll let map do that for us.

That's the map function.
'''

# filter function

'''
The filter function returns an iterator yielding those items of the iterable for which when you pass in the item into the function, it's true.

And that just means that you need to filter by a function that returns either true or false.
'''

def check_even(nums):
    return nums%2 == 0

print(list(filter(check_even, my_nums)))

'''
Lambda expressions are a way to quickly create what are known as anonymous functions, basically just one time use functions that you don't even really name. You just use them one time and then never reference them again.

the map function is built into Python as well as the filter function is built into Python.
'''

def square(nums):
    return nums**2

# for turning this into a lambda expression

lambda num: num ** 2 # this is now a lambda exp
# i can aslo assign it
square = lambda num: num ** 2
square(5) # lambdas are anonymous functions and you typically don't name them. So a lot of times you're not really going to be doing the squares equal to some lambda expression. Instead, you're going to be using it in conjunction with other functions such as map and filter.

print(list(map(lambda num: num ** 2, my_nums)))
print(list(filter(lambda num: num%2 == 0, my_nums)))
print(list(map(lambda name: name[0], names)))


