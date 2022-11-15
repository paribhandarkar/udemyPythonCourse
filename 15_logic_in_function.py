def even_check(num):
    return num % 2 == 0


print(even_check(34))

# long form of this


def even_check(num):
    result = num % 2 == 0
    return result


print(even_check(43))

# return true if any number is even inside a list


def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass


'''
what it's doing is just looping through these numbers until it finds an even one and then it just
breaks out of the function and returns true.
And in fact, you can think of this return statement as essentially going to break off the entire function and end the function call. Once you call return.
That's it.
The function is over.
It's not being run anymore.
'''

print(check_even_list([1, 3, 5]))

# If there is no even number in the list, let's say we actually want it to return. False. How can we fix this?
'''
def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            return False

A super common mistake that a beginner would make is they would simply change else here to return. False. However, this is wrong.
Often beginners make the mistake that all the return statements should have the same level of indentation. But that's actually not true

the very first time that a number is not even, we'll say, okay, in other words, just return false, essentially saying that this if else statement is only going to be able to check one number because both conditions will immediately return something.

So the return false should actually be an indentation with the for loop. So what this says is go ahead and complete the entire for loop.
If this has completed and we never broke out of the function with true return statement, then go ahead and then return false.

the correct way:

def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False
    
'''

# return all the even numbers in the list.

def even_number_return(num_list):
    even_list = [] # placeholder variables
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            pass
    return even_list

print(even_number_return([2, 3, 4, 6, 23, 54]))

