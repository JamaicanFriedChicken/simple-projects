import random


if __name__ == '__main__':

    # set player's move to a value of False
    player_move = False

    computer_moveset = ['scissors', 'paper', 'rock']

    print('Entertain me well!\n')
    # while player's move is equal to false, continues to loop
    while player_move == False:
        print('Welcome to the game of rock, paper and scissors!')
        print('Make your move challenger! What will you pick? (Enter q to quit)')
        player_move = input().lower()

        # if q is entered by user, program will quit
        if player_move == 'q':
            break

        computer_move = computer_moveset[random.randint(0, 2)]

        # rest of the code is self explanatory, it goes as shown:
        # if player's move is this, there will be an if statement that will defeat player's move 'else'
        # computer automatically loses as the assumption is the computer picks the losing move.
        if len(player_move) == len(computer_move):
            print('It is a draw!')
        elif player_move == 'scissors':
            if computer_move == 'rock':
                print('You lose sucker!', computer_move, 'smashes', player_move)
            else:
                print('You win!', player_move, 'cuts', computer_move)
        elif player_move == 'rock':
            if computer_move == 'paper':
                print('You lose sucker!', computer_move, 'covers', player_move)
            else:
                print('You win!', player_move, 'smashes'. computer_move)
        elif player_move == 'paper':
            if computer_move == 'scissors':
                print('You lose sucker!', computer_move, 'cuts', player_move)
            else:
                print('You win!', player_move, 'covers', computer_move)
        else:
            print('You have misspelt a word or have inputted an invalid option')

        player_move = False
        computer_move = computer_moveset[random.randint(0, 2)]
