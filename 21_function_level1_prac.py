# LEVEL 1 PROBLEMS

'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald

Note: 'macdonald'.capitalize() returns 'Macdonald'
'''

def old_macdonald(name):
    first_letter_capital = name.capitalize()
    first_letter_capital_list = list(first_letter_capital)
    first_letter_capital_list[3] = first_letter_capital_list[3].upper()
    return ''.join(first_letter_capital_list)

print(old_macdonald('macdonald'))

# another method
'''
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
'''

'''
MASTER YODA: Given a sentence, return a sentence with the words reversed

master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

>>> "--".join(['a','b','c'])
>>> 'a--b--c'

This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

>>> " ".join(['Hello','world'])
>>> "Hello world"
'''

def master_yoda(text):
    text_to_list = text.split()
    reversed_list = text_to_list[::-1]
    return ' '.join(reversed_list)


print(master_yoda('I am home'))
print(master_yoda('We are ready'))

'''
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True

NOTE: abs(num) returns the absolute value of a number
'''

def almost_there(n):
    if (abs(100 - n) <= abs(10)) or (abs(200 - n) <= abs(10)):
        return True
    else:
        return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
