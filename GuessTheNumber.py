import random


def random_generator():
    random_number = random.randint(0, 20)
    return random_number


if __name__ == '__main__':

    while True:
        random_number = random_generator()
        print('Please guess a number between 0 and 20:\n')
        number_guessed = int(input())
        if number_guessed > random_number:
            print('The number you guessed is too high')
        elif number_guessed < random_number:
            print('The number you guessed is too low')
        if number_guessed == random_number:
            print('You guessed it! you got it correct! Congratulations~')
            break