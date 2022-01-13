####
# titc_tac_toe project
# Matthew Goodsell
####

import random


def main():

    # creating the board spots
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test
    # board_spots[0] == 4
    #print(board)

    # Game 
    welcome_message()

    player_1, player_2 = get_players()

    print(f'\n{player_1} is X \n{player_2} is O.')

    # pick the player to go first 
    first_player = pick_first_player()

    # putting the players in a dictionary to be associated with 1 and 2.
    players = {1:player_1, 2:player_2}

    print(f'\n{players[first_player]} you go first.\n')


    draw_board(board)


    # loop through the game 
    game_result = False
    while game_result == False: 
        choice = players_turn()
        # if statment to specify the argument choice should go to. 
        if first_player == 1:
            choice = players_turn()
            new_board = board_spots(board, player_1 = choice)  
            draw_board(new_board)
        else: 
            choice = players_turn()
            new_board = board_spots(board, player_2 = choice)
        draw_board(new_board)
        print(new_board)

        # check if there is a winner
        if check_results(new_board, x = players[1], o = players[2]) == True: 
            game_result == True
            print('\n Congratulations You won the game!!')
        else: 
            game_result == False
            
        
        

    # to replace numbers on the chart, take the list and replace the value with what the user choose 
    # could use a function for this.
    


def welcome_message():
    print('Welcome to tic-tac-toe!')
    print()

def get_players():
    '''
    Gets the players names. 
    '''

    player_1 = input('player 1 enter your name: ')
    player_2 = input('player 2 enter your name: ')

    return player_1, player_2

def pick_first_player():
    '''
    Randomly chooses a player
    '''
    
    first_player = random.randint(1,2)
    return first_player

def draw_board(board_list):
    ''' 
    Draws a 3x3 board for tic-tac-toe
    '''
    # loop
    #board_spots = [1,2,3,4,5,6,7,8,9]

    #needs work
    # for i in range(0,9):
    #     print(f'{board_spots[i]}|{board_spots[i]}|{board_spots[i]}')
    #     print('_+_+_')
    #print(board_list)
        
    print(f'{board_list[0]}|{board_list[1]}|{board_list[2]}')
    print('_+_+_')
    print(f'{board_list[3]}|{board_list[4]}|{board_list[5]}')
    print('_+_+_')
    print(f'{board_list[6]}|{board_list[7]}|{board_list[8]}')

def board_spots(board_list, player_1=None, player_2=None):
    '''
    Is the list that populates the board. 
    Changes based on the input of the player. 
    '''
    
    # where the number matches the list replace with 
    # when player 1 replace spot with an X 
    # when player 2 replace spot with an O

    if player_1 != None:
        board_list[player_1-1] = 'X'
    else:
        board_list[player_2-1] = 'O'

    return board_list
    

def players_turn():
    '''
    Gets the choice of the player
    '''
    choice = int(input("\nWhat spot would you like? [1-9] "))

    return choice 
    

def check_results(board, x, o):
    '''
    Check the result of the game. 
    '''
    # if these indexes are the same type then end game
    result = False
    if board[0, 1, 2] == 'X' or 'O':
        result = True 
    elif board[3, 4, 5]== 'X' or 'O':
        result = True
    elif board[6, 7, 8] == 'X' or 'O':
        result = True
    elif board[0, 3, 6] == 'X' or 'O':
        result = True 
    elif board[1, 4, 7] == 'X' or 'O':
        result = True
    elif board[2, 5, 8] == 'X' or 'O':
        result = True
    elif board[0, 4, 8] == 'X' or 'O':
        result = True
    elif board[2, 4, 6] == 'X' or 'O':
        result = True
    else:
        result = False

    # test = []
    # for i in board[0,1,2]:
    #     test += i
    #     for j in test:
    #         test[j] == 'X' 
    #         result == True

    return result 

main()
