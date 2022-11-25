# special (magic/dunder) methods

'''
Special methods allow us to use some built in operations in Python, such as the length function or the print function with our own user created objects.
'''

# What if I wanted to check the length of one of my own objects?

class Sample():
    pass

mysample =  Sample()

print(len(mysample)) # I get a type error "object of type 'Sample' has no len()"
print(mysample) # I just get back the report of where my sample object is located at my memory

'''
So the question arises how am I able to actually use built in python functions such as length or print with my own user defined objects?

And this is where those special methods come into play.
So special methods, some people also call them magic methods or dunder methods because they use double underscores 
'''

class Book():

    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages

    def __str__(self):
        return f'{self.author} wrote {self.title}'
    '''
    And what this does, if there's ever any function that asks for the string representation of your book class, then it's going to return whatever this method returns, which is why it's a special method. And make sure you use return here, not print. And I'm going to return whatever I want to be printed out.
    '''

    def __len__(self):
        return self.pages

    '''
    when I print these books out and ask for their length, I get back to 300
    '''

    def __del__(self):
        print("a book object has been deleted")

    '''
    Sometimes you may want to print out a report upon the deleting the variable, or you may want other things to occur when you delete the variable in order to basically specify extra things that may occur when you call delete.
    '''

    

b = Book('rowling','harry potter', 300)

print(b) # If I try to print my book, it just says, Hey, you have this book object in memory. What happens is when you call the print function, what the print function does is it asks what is the string representation of B?

# instead, what we can do is actually use the special method related to that string call __str__
# So what happens is when I'm going to call the print function, the print function asks the book object, hey, do you have a string representation of yourself? To which the book object then says Yes, I do, because I have this special str method and I return this string

print(len(b)) # we can do the same thing for length because right now if I try to check the length of my book b, it says, Hey, object, the type book has no length.

del b # this will actually delete that book from the memory on your computer. So if you ask for B again, it's going to say name error B is not the defined. So this is a way to delete variables from your computer's memory.

'''
u can check the documentation for many more under or special or magic methods, but really these are the main ones you're going to be using, especially str and len.

So again, str, it returns back the actual string representation so you can print out user defined objects.

len returns back the length so you can return back the length of user defined objects.
'''