import random
from main import valid, print_board
# from gui2 import pos
print("WELCOME TO SUDOKU!")


def first_print_level_choose():
    print("Please choose your level of difficulty: ")
    print("       1. Beginner")
    print("       2. Intermediate")
    print("       3. Advanced")

    level = int(input("\n"))

    if level == 1:
        return 20
    elif level == 2:
        return 15
    elif level == 3:
        return 8
    else:
        first_print_level_choose()


zer = first_print_level_choose()

grid = [[0 for i in range(9)] for j in range(9)]


def random_grid(zer):
    for i in range(zer):
        rows = random.randrange(9)
        column = random.randrange(9)
        pos = (rows, column)
        nums = random.randrange(1, 10)

        while not valid(grid, nums, pos) or grid[rows][column] != 0:
            rows = random.randrange(9)
            column = random.randrange(9)
            pos = (rows, column)
            nums = random.randrange(1, 10)
        grid[rows][column] = nums


random_grid(zer)
print("---------UNSOLVED GRID--------")
print()
print_board(grid)

# solve(grid)
#
# print()
#
# print("--------SOLVED BOARD---------")
#
# print()
#
# print_board(grid)
