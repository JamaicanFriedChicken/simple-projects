# Utility script for Game


def count_open(move):
    return sum(map(lambda x: 1 if 'O' in x else 0, move))
