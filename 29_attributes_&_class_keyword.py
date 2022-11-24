# What we're going to do is see if we can create our own user defined objects, and everything in Python is an object. So let's explore how we can use the class keyword to create a user defined object. lists, sets dicts etc. they all are built in objects.

'''
For a user defined object, the class is basically a blueprint that defines the nature of a future object.

And from classes we can then construct an instance of the object and an instance is a specific object created from a particular class.
'''

class Sample():
    pass

my_sample = Sample()

# if I check the type of my_sample, you should see something that lets you know that it's a sample type
print(type(my_sample))
# the '__main__.Sample' means it's just letting you know that this particular instance of sample is connected to your main script here.

'''
a special method called the init method, which is going to be called upon whenever you actually create an instance of the class.

And we always start off with the self keyword, which basically connects this method to the instance of the class.

And it allows us to refer to itself, and then we pass in any attributes that we want the user to define. an attribute is a characteristic of an object.
'''

class Dog():
    def __init__(self, breed):
        self.breed = breed
 
'''
and let's create a variable. I will say my_dog is equal to an instance of the dog class.

my_dog = Dog()

Now, if I don't pass anything, I will actually get an error.
So you'll notice that we actually get an error when we run this with no positional arguments because we are expecting the breed parameter.

So what this python is trying to say to us is, hey, when you create a dog, it's expecting you to pass any parameter for breed.
'''

my_dog = Dog(breed='lab') # And now when we run this, we don't get an error.
print(type(my_dog)) # And I can check the type of this my_dog variable and it says, Hey, you now have an instance of the Dog class.

print(my_dog.breed)

'''
__init__ : it can basically be thought of as the constructor for a class, and it's going to be called automatically when you create an instance of the class

self keyword : It represents the instance of the object itself. And actually most object oriented languages pass this as a hidden parameter to the methods defined on an object.

But Python, it doesn't do this. You have to declare it explicitly and by convention.
We use the word self here.
Technically, you could write in any variable name you wanted, but you should definitely stick with self that way.

Other programmers when they look at your code, it makes sense to them.

breed: u c breed above 3 times

class Dog():
    def __init__(self, mybreed):
        self.my_attribute = mybreed

my_dog = Dog(mybreed = 'husky')
print(my_dog.my_attribute)

So all we're doing here is you pass in the parameter or argument and then it gets assigned to the attribute that you can later call on your object.

it's just cleaner to have all three of these be the same term.
That way you know what's being passed in and where it's being assigned.
There's no real reason that they should all have those separate names.
'''

class Cat():

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

# not every attribute you pass in is going to be a string, but it can be an integer. A floating point, a list. It can be a lot of stuff.

my_cat = Cat(breed='scottish folds', name='olivia', spots=False)
print(my_cat.breed)
print(my_cat.name)