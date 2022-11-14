# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Sam print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)
    # else:
    #     print('is not an s letter word')

# Use range() to print all the even numbers from 0 to 10.

for num in range(1, 11):
    if num % 2 == 0:
        print(num)

print(list(range(0,11,2))) #or

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

lst = [num for num in range(1, 51) if num % 3 == 0]
print(lst)

# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) % 2 == 0:
        print(word)

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1, 101):
    if num % 15 == 0:
        print("fizzbuzz")
    else:
        if num % 5 == 0:
            print("buzz")
        else:
            if num % 3 == 0:
                print("fizz")
            else:
                print(num)

#or

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)


# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
mylist = [letter[0] for letter in st.split()]
print(mylist)