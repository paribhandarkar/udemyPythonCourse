game_list = [0,1,2]


def display_list(game_list):
    print("this is our current game list")
    print(game_list)
    return game_list


def position_selection():

    choice = 'wrong'

    while choice not in ['0', '1', '2']:

        choice = input("pick a position from 0, 1 or 2: ")

        if choice not in ['0', '1', '2']:
            print(" sorry please select the right number")

    return int(choice)


def replacement_function(game_list, position):

    replace_word = input("enter the word that u want to replace the selected position with: ")
    game_list[position] = replace_word

    return game_list


def gameon_choice():
    ask_choice = 'some'

    while ask_choice not in ['y', 'n']:
        ask_choice = input("do u want to continue with the game: y or n? ")

        if ask_choice not in ['y', 'n']:
            print('please only select from y or n')
    
    if ask_choice == 'y':
        return True
    else:
        return False
        

continue_game = True


while continue_game == True:

    display_list(game_list)

    position = position_selection()
    print(position)

    updated_game_list = replacement_function(game_list, position)

    display_list(updated_game_list)

    continue_game = gameon_choice()

