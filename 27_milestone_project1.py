# def game_on():
#     msg = 'some'
#     while msg not in ['y', 'n']:
#         msg = input("do u want to play game? y or n? ")

#     if msg not in ['y', 'n']:
#         print('please only select from y or n')

#     if msg == 'y':
#         return True
#     else:
#         return False


# print(game_on())


def display_board(test_board):
    print(test_board[0]+'|'+test_board[1]+'|'+test_board[2])
    print(test_board[3]+'|'+test_board[4]+'|'+test_board[5])
    print(test_board[6]+'|'+test_board[7]+'|'+test_board[8])


# board = [' ']*9
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

display_board(board)


def goti_select():
    p1 = 'hello'
    p2 = 'hi'
    while p1 not in ['x', 'o']:
        p1 = input("select player1 either x or o: ")

    if p1 not in ['x', 'o']:
        print("select only from x or o")

    if p1 == 'x' or p1 == 'o':
        print(f"player 1 you are {p1}")
        return p1


goti = ['x', 'o']
p1_title = goti_select()

if p1_title == goti[0]:
    p2_title = goti[1]
else:
    p2_title = goti[0]

print(p1_title)
print(p2_title)


def select_pos1(selection):
    pos = 'some'
    while pos not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        pos = int(input("select position from (0-9): "))

    # board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    board[pos] = selection

    display_board(board)

# def check_it(pos1, pos2):
#     while win_or_not == False:
#         pl1 = 'some'
#         pl2 = 'thing'
#         while pl1 not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
#             pl1 = int(input("select position from (0-9): "))
    
#         board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#         board[pl1] = pos1
#         display_board(board)

#         win_check()

#         while pl2 not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
#             pl2 = int(input("select position from (0-9): "))

#         board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#         board[pl2] = pos2
#         display_board(board)
        
    



def select_pos2(selection):
    pos = 'some'
    while pos not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        pos = int(input("select position from (0-9): "))

    # board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    board[pos] = selection

    display_board(board)

def win_check(item):
    # for item in goti:
    if item == board[0] and item == board[1] and item == board[2]:
        print(f'{item} wins')
        return True
    elif item == board[3] and item == board[4] and item == board[5]:
        print(f'{item} wins')
        return True
    elif item == board[6] and item == board[7] and item == board[8]:
        print(f'{item} wins')
        return True
    elif item == board[0] and item == board[3] and item == board[6]:
        print(f'{item} wins')
        return True
    elif item == board[1] and item == board[4] and item == board[7]:
        print(f'{item} wins')
        return True
    elif item == board[2] and item == board[5] and item == board[8]:
        print(f'{item} wins')
        return True
    elif item == board[0] and item == board[4] and item == board[8]:
        print(f'{item} wins')
        return True
    elif item == board[2] and item == board[4] and item == board[6]:
        print(f'{item} wins')
        return True
    else:
        return False

# win_or_not = win_check()

def game_map():

    while win_check(p1_title) == False and win_check(p2_title) == False:


        print(select_pos1(p1_title))

    # print(check_it(p1_title, p2_title))

        win_check(p1_title)

    # def select_pos1(selection):
    #     pos = 'some'
    #     while pos not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
    #         pos = int(input("select position from (0-9): "))

    #     board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    #     board[pos] = selection

    #     display_board(board)

    #     print(select_pos1(p1_title))

    # def select_pos2(selection):
    #     pos = 'some'
    #     while pos not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
    #         pos = int(input("select position from (0-9): "))

    #     board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    #     board[pos] = selection

    #     display_board(board)

    #     print(select_pos1(p2_title))

        # while win_check(p1_title) == False:

        print(select_pos2(p2_title))

        win_check(p2_title)



print(game_map())
