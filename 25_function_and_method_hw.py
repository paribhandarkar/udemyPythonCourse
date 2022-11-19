# Functions and Methods Homework

'''
Complete the following questions: ____ Write a function that computes the volume of a sphere given its radius.
'''

import math

def vol(rad):
    volume = (4/3) * (math.pi) * (rad**3)
    return volume

# Check
print(vol(2))

'''
Write a function that checks whether a number is in a given range (inclusive of high and low)
'''

def ran_check(num,low,high):
    lst = []
    for item in range(low, high+1):
        lst.append(item)
    
    if num not in lst:
        print(f'{num} is not in the range between {low} and {high}')
    else:
        print(f'{num} is in the range between {low} and {high}')

# Check
ran_check(5,2,7)

'''
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: .isupper() and .islower()
'''

def up_low(s):
    lst = list(s)
    upp_lst = []
    low_lst = []
    for item in lst:
        if item.isupper() == True:
            upp_lst.append(item)
        elif item.islower() == True:
            low_lst.append(item)
        else:
            pass
    
    print(f'No. of Upper case characters : {len(upp_lst)}')
    print(f'No. of Lower case characters : {len(low_lst)}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''

def unique_list(lst):
    print(set(lst))

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

'''
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
'''


def multiply(numbers): 
    mul = 1 
    for num in numbers:
        mul = mul * num

    return mul

print(multiply([1,2,3,-4]))
print(multiply([3, 2, 4]))

'''
Write a Python function that checks whether a word or phrase is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
'''

def palindrome(s):
    str = s.lower().replace(" ", "")
    straight_list = list(str)
    reversed_list = straight_list[::-1]
    if straight_list == reversed_list:
        return True
    else:
        return False


print(palindrome('hE ll eh'))
print(palindrome('racecar'))
print(palindrome('nurses run'))


'''
Hard:
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Hint: You may want to use .replace() method to get rid of spaces.

Hint: Look at the string module

Hint: In case you want to use set comparisons
'''

import string
 
def ispangram(str1, alphabet=string.ascii_lowercase):
    str = str1.replace(" ", "").lower()
    if set(str) == set(alphabet):
        return True
    else:
        return False

print(ispangram("The quick brown fox jumps over the lazy dog"))

    