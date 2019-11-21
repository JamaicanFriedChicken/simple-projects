from random import shuffle, randrange


def make_maze(w, h):
    visualize_grid = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    vertical = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    horizontal = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x ,y):
        visualize_grid[y][x] = 1

        d = [(x - 1, y), (x, y +1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if visualize_grid[yy][xx]: continue
            if xx == x: horizontal[max(y, yy)][x] = "x  "
            if yy == y: vertical[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a,b) in zip(horizontal, vertical):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s


if __name__ == '__main__':
    print(make_maze(16, 8))