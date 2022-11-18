'''
two functional parameters: *args and **kwargs
And they stand for arguments and keyword arguments.
Eventually, if you work with Python functions long enough, you're going to want a way to accept an arbitrary number of arguments and keyword arguments without having to pre define a bunch of parameters in your function calls.
'''


def myfunc(a, b, c=0, d=0, e=0):
    # returns 5% of the sum of a and b
    # it takes the sum of everything in that tuple, and then we multiply by 0.05.
    return sum((a, b, c, d, e)) * 0.05


print(myfunc(40, 60, 100, 100, 600))

'''
right now that A and B, these are examples of what are called positional arguments.
That is to say that right now 40 is assigned to A because it was in the first position or the first argument and that 60 is assigned to B because it was in the second position or second argument.

I notice that when we want to work with multiple positional arguments in the sum function, we had to pass them in as a tuple.

the thing that we did above was assigned a lot of parameters i.e c,d,e and set their default value to 0 so that even if there value was not defined during function call it won't effect the result.
(won't affect the sum, but they can always override it)

I'll eventually hit a limit up to e, because if I keep adding in more numbers

print(myfunc(40,60,100,100,600,86))
i'll get:
TypeError: myfunc() takes from 2 to 5 positional arguments but 6 were given

and this is where we can use that *args
It allows us to set this to take an arbitrary number of arguments.
'''


def myfunc(*args):
    return sum(args) * 0.05


print(myfunc(40, 60, 100, 100, 600, 86))

'''
this allows me to do is treat this as a tuple of parameters that are coming in
And now I can pass in as many arguments as I want. And by default, what Python is going to do is it's going to take all the parameters that are passed in and set them to be inside a tuple.
and I can keep adding in as many numbers as I want here with no problems.
And that's basically the whole point of *args
'''


def myfunc(*args):
    print(args)


print(myfunc(45, 23, 23, 43, 12, 6))

'''
if I just print out what ARGs actually looks like to this function, it just looks like a tuple here.
So all this does when it starts with this star term, it says "okay, whatever this parameter is, the user can pass in as many as they want and it's going to be treated as a tuple inside of this function"

And that's really useful for a lot of things.
You can loop through it or iterate through it or sum it together or do any sort of aggregation function on whatever this tuple that is being passed in.
'''


def myfunc(*jelly):  # has the exact same effect as *args
    print(jelly)


print(myfunc(45, 23, 23, 43, 12, 6))

'''
by convention we use args, but this technically indicated by the fact that there's that star term there.
args can be any other keyword you want. same with **kwargs
'''


def myfunc(*args):
    for item in args:
        print(item)


print(myfunc(45, 23, 23, 43, 12, 6))


'''
Similarly, Python offers a way to handle an arbitrary number of key worded arguments.
So instead of creating a tuple of values, what happens is we use **kwargs, which is keyword arguments, and that builds a dictionary of key-value pairs.

'''


def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("eww")


myfunc(fruit='apple')
# python is no longer complaining. and that's the power of these arbitrary keyword arguments.
myfunc(fruit='apple', veggie='cauliflower')


def myfunc(**kwargs):
    print(kwargs)  # It's just the dictionary.
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("eww")


myfunc(fruit='apple', veggie='cauliflower')

'''
So just like args appear return back a tuple, keyword arguments returned back a dictionary that you can then play around with inside your function.
'''

def myfunc(*args, **kwargs):
    print("i would like: {} {}".format(args[0], kwargs['food']))

myfunc(10,20,30, food = 'apple', animal = 'dog', color = 'pink')

'''
The only final point I'd like to make here is that because we set args first and keyword arguments, it has to go in that order.
We have to have that list or tuple of arguments and then after that we have to have the keyword arguments.

myfunc(10,20,30, food = 'apple', animal = 'dog', color = 'pink', 100)
we can't do this, it gives:
SyntaxError: positional argument follows keyword argument

it has to be in the same order you prescribed, which was all the arguments first, then all the keyword arguments.
'''
