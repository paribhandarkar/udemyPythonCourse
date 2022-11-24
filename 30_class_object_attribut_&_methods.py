
class Cat():

    # class object attribute
    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    # operations/actions ----> methods
    def meow(self):
        print(f'meow! my name is {self.name}') # What we need to do is reference the particular instance of the dog's name, meaning we need to reference, not name but self.name, because when you pass the name at the beginning, it gets connected to the object through the use of this self keyword.

    def tag(self, number):
        print(f'my tag number is {number}') # Methods can take outside arguments so we can pass it. Some other argument here. So we could say pass in some number.
        # I'm no longer saying self.number because number is already being provided for us when we actually call tag. So that means we need to actually pass in a number call.
'''
class object attributes: these are attributes that are going to be the same for any instance of the class.

there may be attributes that are going to be the same for any instance of the Cat class, for example. We know that it doesn't matter whether a cat has a certain breed, a certain name, whether or not has spots, it's always going to be a mammal.

So something we may want to do is have an attribute be defined at a class object level instead of having the particular instance

Instead we'll define an attribute above our init method here. So above this special method.
At the very start we can define what's known as a class object attribute, and these are the same for any instance of a class.

we don't use the self keyword because we know that the self keyword is a reference to this particular instance of a class.
But since the class object attribute is the same for any instance of a class, we can just say something like the species = 'mammal'

'''

my_cat = Cat(breed='scottish folds', name='olivia', spots=False)
my_cat1 = Cat('siamese', 'meredith', False) # can also do it this way
print(my_cat.breed)
print(my_cat.name)
print(my_cat.species)
my_cat.meow() 
my_cat1.meow()
my_cat.tag(3) # now this method is expecting some sort of added argument number

'''
Methods are essentially functions defined inside the body of the class, and they're used to perform operations that sometimes utilize the actual attributes of the object we created.

So you can basically think of methods as functions, acting on an object that take the object itself into account through the use of the self argument or self keyword.

what's the difference between a function and a method? Basically a method is a function that is inside of a class that will actually work with the object in some way. It's basically just an action that the actual object can take.

the attributes never had open and close parentheses, and that's because attributes aren't really something that you execute.
Instead, it's just something that's a characteristic of the object that you call back.
So it's just information there about the actual cat.
methods will need to be executed. so that means we need to have the open and close parentheses when we do a method call
'''

class Circle():

    # class object attribute 
    pi = 3.14

    def __init__(self, radius = 1): # i provided a default parameter here
        self.radius =  radius
        self.circum = 2* self.pi * radius
        self.circum = 2* Circle.pi * radius # can also do this

    def get_area(self):
        return self.pi * (self.radius**2)

my_circle = Circle(7)
print(my_circle.get_area())
print(my_circle.circum)