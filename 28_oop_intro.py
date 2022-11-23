class NameOfClass():
    def __init__(self, param1, param2): #this thing that looks a lot like a function, but it's actually called a method when it's inside of an object or inside of a class call.
        self.param1 = param1
        self.param2 = param2

def some_method(self):
    print(self.param1)

'''
the name of the class now is following what's called camel racing, where every individual word has that first letter capitalized, which is why we were telling you before to have variable names and function names in lowercase, because classes, those are the reserved uppercase words and uppercase naming schemes.
'''

'''
init allows you to create an instance of the actual object.

You'll notice here we have then a self keyword as well as some parameters to be passed. So param1 and param2 are going to be parameters that Python expects you to pass when you actually create an instance of this object.

And then what it does is when you pass in a parameter, for instance, param2, you go ahead and assign it to an attribute of the function.

That way Python knows that when you're referring to self.param2, you're referring to the attribute param2 that's connected to this actual instance of the class instead of a global variable called param2.

all we're doing here is we're going to pass in a parameter and then connect that parameter with the use of that self dot argument or self.parame to link it to the actual object itself.
'''

'''
After that, then we can have various other method calls and these look a lot like functions. We say def the name of whatever you want your method to be, and then you pass in that self keyword again to let Python know that this isn't just some function, it's a method that's connected to this class.

And that's why we use a self word to connect these methods to the class so that when you call something like    self.param1, it knows that you're referring to the attribute param1 that's connected to the class itself.
'''