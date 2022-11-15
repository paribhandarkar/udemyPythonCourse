def name_of_function(name):
    '''
    docstring explains a function
    '''
    print("hello" + name)

name_of_function("pari")


name_of_function
# If you call it without parentheses, then it's actually not going to execute the function. Python will just report back that say name_of_functio is a function. Keep that in mind that when we're calling functions in order to execute them, we have to add on open and close parentheses. So if you see something like this, it means you're not actually calling the function you need to add on the parentheses.

name_of_function()
'''
let's imagine I forgot to pass in an actual value. So I just said name_of_function Well, in this case, Python is going to complain. and the way to read this error is it will say
TypeError: name_of_function() missing 1 required positional argument: 'name'
which is essentially trying to tell you, "hey, we need to know what name is as an argument in order to actually execute this block of code"

So how can you fix this?

Well, one way is just to provide the value, as mentioned.

Another way is to provide what's known as a default value.

name_of_function(name = "user")
So what this means is if name is not provided, then we'll go ahead and use this default.

'''

# main difference between print & return is that return, instead of just printing out the results, is actually going to allow you to save them as a variable. just having prints is not going to allow you to actually grab the result.

# python is dynamically typed, which means I don't need to specify beforehand what data type I expect name to be That allows you to program a lot faster, but it also leaves you open to possible bugs.
