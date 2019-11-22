from random import shuffle, randrange


def make_maze(w, h):
    """
    Generates a random maze using Depth first search algorithm.
    w : width of the maze
    h : height of the maze

    Set the parameters as you would like for the size of the generated maze.
    """
    visualize_grid = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    vertical = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    horizontal = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x ,y):
        """
            Walk function generates the maze's interior design through random generations and spacing between
        each partitions. The maze will be different each time due to the randrange and shuffle function
        imported from random library.
        """
        visualize_grid[y][x] = 1

        d = [(x - 1, y), (x, y +1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if visualize_grid[yy][xx]: continue
            if xx == x: horizontal[max(y, yy)][x] = "x  "
            if yy == y: vertical[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    # assembles the grid together, whereby a consists of '+--' and 'x ', however b
    # consists of partitions followed by empty spaces in between the partitions.
    s = ""
    for (a,b) in zip(horizontal, vertical):
        s += ''.join( a+ ['\n'] + b + ['\n'])
    return s


if __name__ == '__main__':
    print(make_maze(16, 8))