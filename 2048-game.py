import random

def initialize_game():
    grid = [[0] * 4 for _ in range(4)]
    print("Commands are as follows:")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    add_random_two(grid)
    return grid

def add_random_two(grid):
    row, col = random.randint(0, 3), random.randint(0, 3)
    while grid[row][col] != 0:
        row, col = random.randint(0, 3), random.randint(0, 3)
    grid[row][col] = 2

def check_game_state(grid):
    for row in grid:
        if 2048 in row:
            return 'WON'
    for row in grid:
        if 0 in row:
            return 'GAME NOT OVER'
    for i in range(3):
        for j in range(3):
            if grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1]:
                return 'GAME NOT OVER'
    for j in range(3):
        if grid[3][j] == grid[3][j+1]:
            return 'GAME NOT OVER'
    for i in range(3):
        if grid[i][3] == grid[i+1][3]:
            return 'GAME NOT OVER'
    return 'LOST'

def compress_grid(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    changed = False
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_grid, changed

def merge_grid(grid):
    changed = False
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j+1] = 0
                changed = True
    return grid, changed

def reverse_grid(grid):
    return [row[::-1] for row in grid]

def transpose_grid(grid):
    return [list(row) for row in zip(*grid)]

def move_left(grid):
    new_grid, changed1 = compress_grid(grid)
    new_grid, changed2 = merge_grid(new_grid)
    new_grid, _ = compress_grid(new_grid)
    return new_grid, changed1 or changed2

def move_right(grid):
    new_grid = reverse_grid(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse_grid(new_grid)
    return new_grid, changed

def move_up(grid):
    new_grid = transpose_grid(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose_grid(new_grid)
    return new_grid, changed

def move_down(grid):
    new_grid = transpose_grid(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose_grid(new_grid)
    return new_grid, changed
