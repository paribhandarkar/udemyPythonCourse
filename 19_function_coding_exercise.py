'''
Functions #9: pick evens
Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.
'''

def myfunc(*args):
    lst = []
    for item in args:
        if item % 2 == 0:
            lst.append(item)
        else:
            pass
    return lst

print(myfunc(5,6,7,8))

'''
Functions #10: skyline
Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.

Remember, don't run the function, simply provide the definition.
'''

# my code

def myfunc(a):
    lst = []
    for letter in a:
        if a.index(letter) % 2 == 0:
            lst.append(letter.lower())
        else:
            lst.append(letter.upper())
    return ''.join(lst)

print(myfunc('Anthropomorphism'))

# the 'correct' code

def myfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

print(myfunc('Anthropomorphism'))