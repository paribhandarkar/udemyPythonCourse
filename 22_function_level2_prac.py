# LEVEL 2 PROBLEMS
'''
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''

# # failed code
# def has_33(nums):
#     for item in nums:
#         if item == 3:
#             index_of_first_3 = nums.index(item)
#             index_of_second_3 = index_of_first_3 + 1
#             if nums[index_of_second_3] == 3:
#                 return True
#             else:
#                 return False
    

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# another spectactular method
# def has_33(nums):
#     for i in range(0, len(nums)-1):
#         if nums[i:i+2] == [3,3]:
#             return True
#     return False


print(has_33([1, 3, 4, 2, 3, 3]))
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''

def paper_doll(text):
    lst = []
    for letter in text:
        new_letter = letter*3
        lst.append(new_letter)
    return ''.join(lst)

print(paper_doll('hello'))
print(paper_doll('Mississippi'))

'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''

def blackjack(a,b,c):
    if a+b+c <= 21:
        return a+b+c
    elif a+b+c > 21 and (a==11 or b==11 or c==11):
        return (a+b+c) - 10
    else:
        return 'BUST'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

'''
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
'''

def summer_69(arr):
    for item in arr:
        if item == 6:
            six_index = arr.index(item)
            # print(six_index)
            nine_index = arr.index(9)
            # print(nine_index)
            sliced_list = arr[six_index : nine_index + 1]
            # print(sliced_list)
            newlst = [i for i in arr if i not in sliced_list]
            # newlst = [i for i in arr if not i in sliced_list or sliced_list.remove(i)]
            return sum(newlst)
    return sum(arr)

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))