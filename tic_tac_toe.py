import random

def main():

    welcome_message()

    player_1, player_2 = get_players()

    print(f'\n{player_1} is X \n{player_2} is O.')

    # pick the player to go first 
    first_player = pick_first_player()
    print(f'\nPlayer {first_player} you go first.\n')

    draw_board()


    # loop through the game 
    # game_result = False
    # while game_result == False: 
        # 
    


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
    first_player = random.randint(1,2)
    return first_player

def draw_board():
    ''' 
    Draws a 3x3 board for tic-tac-toe
    '''
    # loop
    board_spots = [1,2,3,4,5,6,7,8,9]

    #needs work
    for i in range(0,9):
        print(f'{board_spots[i]}|{board_spots[i]}|{board_spots[i]}')
        print('_+_+_')
        
    print('1|2|3')
    print('_+_+_')
    print('4|5|6')
    print('_+_+_')
    print('7|8|9')
    

def check_results():
    '''
    Check the result of the game. 
    '''
    pass

main()
