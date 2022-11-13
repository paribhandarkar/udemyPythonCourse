num1_list = [2, 3, 5, 6]
num1_list[1] = 4
print(num1_list) #unlike strings, we can change it here like this

num_list = [2,6,4,8]
num_list.sort()
my_sorted_list = num_list.sort()
print(type(my_sorted_list))

#do this instead
num2_list = [2, 5, 7, 3, 1, 6]
num2_list.sort()
my_sorted_list2 = num2_list
print(num2_list)
print(my_sorted_list2)

# If you are familiar with another programming language, you might start to draw parallels between arrays in another language and lists in Python. Lists in Python however, tend to be more flexible than arrays in other languages for a two good reasons: they have no fixed size (meaning we don't have to specify how big a list will be), and they have no fixed type constraint