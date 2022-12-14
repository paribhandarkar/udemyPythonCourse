# WARMUP SECTION:

'''
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
'''

def lesser_of_two_evens(a,b):
    if (a%2==0) and (b%2==0):
        if a>b:
            return b
        else:
            return a
    elif (a%2==1) or (b%2==1):
        if a>b:
            return a
        else:
            return b

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

'''
# another method

def lesser_of_two_evens(a,b):
    if (a%2==0) and (b%2==0):
        result = min(a,b)
    elif (a%2==1) or (b%2==1):
         result = max(a,b)
    return result

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
'''

'''
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
'''

def animal_crackers(text):
    two_words = text.lower().split()
    word_count = len(two_words)
    if word_count == 2:
        if two_words[0][0] == two_words[1][0]:
            return True
        else:
            return False
    else:
        return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print(animal_crackers('Crazy cat'))

'''
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
'''

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or (n1 + n2 == 20):
        return True
    else:
        return False

'''
def makes_twenty(n1,n2):
    return (n1 == 20 or n2 == 20 or (n1 + n2 == 20))
'''


print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))