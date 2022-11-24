# inheritance

'''
inheritance is basically a way to form new classes using classes that have already been defined.
And really important benefits of inheritance are the ability to reuse code that you've already worked on and to reduce the complexity of a program.
'''

# base class. this is going to serve as our base class. So newly formed classes can use the animal class in order to inherit some of its methods that you may want to use again.

class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print("i am an animal")

    def eats(self):
        print("i am eating")

my_animal = Animal()

# if I pass an animal, I'm going to inherit or derive from this base class. So this is now known as a derived class because I'm deriving some of my features from this base class of animal.
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self) # So I'm going to actually create an instance of the animal class when I create an instance of my dog class. And I'm able to do that because I'm inheriting from the animal class.
        print("DOG CREATED")
    
    def who_am_i(self):
        print('i am a dog') # if I want to overwrite one of the older methods

    def bark(self):
        print("woof!") # we can also add new methods

my_dog = Dog() # And I run this and now I see that an animal is created because when I run this line of dog, this init method gets called, which in turn runs the init method off animal which in turn prints out animal created. And then after that's created, I print out dog created.

my_dog.who_am_i()

'''
All those old methods that were available for the animal who_am_i and eats are now available for my dog. So even though inside this dog class I don't have eats or who_am_i defined, I'm still able to use them because I was able to derive them from my base class of animal.

And that's the main idea behind inheritance.

I can now reuse methods that should be common between classes by just inheriting, so I don't need to rewrite all these methods for my new class.
'''

# polymorphism

'''
In Python, polymorphism refers to the way in which different object classes can share the same method name, and then those methods can be called from the same place, even though a variety of different objects might be passed in 

polymorphism basic idea is you have these two separate classes that happen to share the same method name allowing you to then call those same method names without needing to worry about the specific class that's being passed in.
'''

class Dogs():

    def __init__(self, name):
        self.name = name

    def speaks(self):
        return self.name + " says woof!"

class Cats():

    def __init__(self, name):
        self.name = name

    def speaks(self):
        return self.name + " says meow!"

niko = Dogs('niko')
felix = Cats('felix')

print(niko.speaks())
print(felix.speaks())

'''
So here we have a Dogs class and a Cats class. Each of them has the speak method.
When called each object's speak method returns a result that's unique to the object.

That is to say, it's unique for the dog to say Woof, and it's unique to the cat to say meow, as well as their names are going to be unique to that particular instance of the class.
'''

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speaks())

'''
I run this and this is an example of polymorphism.
So both Nico and Felix shared the same method name called Speak.
However, they are different types here. 
'''

def pet_speak(pet):
    print(pet.speaks())

pet_speak(niko)
pet_speak(felix)

'''
So pet_speak itself doesn't actually know whether you're going to pass in a dog or a cat.
'''

# abstract classes

'''
an abstract class is, is one that never expects to be instantiated, you never actually expect to create an instance of this class. Instead, it's just designed to basically only serve as a base class.
'''
# this animal class is never actually expected to be instantiated. I don't expect to ever make an instance of the animal class. Instead, this is basically to be only used as a base class.

class Animals():

    def __init__(self, name):
        self.name = name 

    def speaks(self):
        raise NotImplementedError ("subclass must implement this abstract method")

myanimal = Animals('phil')
# myanimal.speaks() 
# if I say animal speak, I get back hey not implemented error and this is actually telling me hey, you're supposed to use a subclass to implement this abstract method. So the reason this is an abstract method is because in the base class itself, it doesn't actually do anything. It's expecting you to inherit the animal class and then overwrite the speak method so I could delete this line because as we just said, we never actually expect to use animal in that fashion.

class Bird(Animals):

    def speaks(self):
        return self.name + " says twitter"

tweety = Bird('tweety')
print(tweety.speaks()) # this works now