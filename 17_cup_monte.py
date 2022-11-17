from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def user_guess_function():
    user_guess = ''
    while user_guess not in ['0', '1', '2']:
        user_guess = input(print('either select 0 or 1 or 2: '))
    return int(user_guess)

def play_game_now(my_list, user_guess):
    if my_list[user_guess] == 'o':
        print("you win")
    else:
        print("wrong guess")
        print(lst)

lst = [' ','o',' ']
shfl_list = shuffle_list(lst)
final_guess = user_guess_function()
play_game_now(shfl_list, final_guess)



# the course code 

'''

def shuffle_list(mylist):
    # Take in list, and returned shuffle versioned
    shuffle(mylist)
    return mylist

def player_guess(): 
    guess = ''
    
    while guess not in ['0','1','2']:
        
        # Recall input() returns a string
        guess = input("Pick a number: 0, 1, or 2:  ")
    
    return int(guess)    

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)


# Initial List
mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()

# Check User's Guess
#------------------------
# Notice how this function takes in the input 
# based on the output of other functions!
check_guess(mixedup_list,guess)

'''
