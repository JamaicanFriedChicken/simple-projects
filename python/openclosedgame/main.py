import random
import sys

from utils import count_open


def check_input(move):
    if move.length > 3:
        print()


def play_again():
    print('Do you want to play again? yes or no?')
    return input().lower().startswith('y')


def decide_winner(player_move, computer_move, guess):
    o_count = count_open(player_move) + count_open(computer_move)
    print(guess)
    print(o_count)
    if guess == o_count:
        return True


if __name__ == '__main__':
    # computer's move list
    computer_moveset = ['CC', 'OO', 'CO', 'OC']
    player_move = False
    gameIsPlaying = True
    turn = 'player'

    while gameIsPlaying:
        if turn == 'player':
            computer_move = random.choice(computer_moveset)
            print('Welcome to the game!\n')
            print('You are the PREDICTOR, What is your input?')
            player_move = input().upper()
            print('AI: ' + computer_move)

            player_guess = int(player_move[2:3])
            if decide_winner(player_move, computer_move, player_guess):
                print('You win!')
                gameIsPlaying = False
            else:
                print('No Winner')
                turn = 'computer'
        else:
            print('Computer is the PREDICTOR, what is your input?')
            player_move = input().upper()
            computer_predict = (random.choice(computer_moveset) + str(random.randrange(5)))
            print('Computer: ' + computer_predict)

            computer_guess = int(computer_predict[2:3])
            if decide_winner(player_move, computer_predict, computer_guess):
                print('Computer Wins!')
                gameIsPlaying = False
            else:
                print('No Winner')
                turn = 'player'

    # Terminates program if player decides not to play again.
    if not play_again():
        print('Nice playing with ya! Bye :)')
        sys.exit()
