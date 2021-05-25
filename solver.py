# Arquivo responsável com as funções que vão resolver o sudoku.
import numpy as np
from entry_values import grid

def verify_column(grid, y, n):

    for i in range(0,9):
        if grid[i][y] == n:
            return False

def verify_line(grid, x, n):

    for i in range(0,9):
        if grid[x][i] == n:
            return False

def verify_square(grid, x, y, n):

    x1 = (x // 3) * 3
    y1 = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[x1+i][y1+j] == n:
                return False

def is_zero(grid, x, y):

    if grid[x][y] == 0:
        return True
    else:
        return False

def is_possible(grid, n, x, y):

    # verify_column(grid, y, n)
    # verify_line(grid, x, n)
    # verify_square(grid, x, y, n)

    for i in range(0,9):
        if grid[i][y] == n:
            return False

    for i in range(0, 9):
        if grid[x][i] == n:
            return False

    x1 = (x//3)*3
    y1 = (y//3)*3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x1+i][y1+j] == n:
                return False
    return True


def verify_all_numbers(grid, x, y):

    for n in range(1, 10):
        if is_possible(grid, n, x, y):
            grid[x][y] = n
            solve(grid)
            grid[x][y] = 0
    return



def solve(grid):

    for x in range(9):
        for y in range(9):
            if is_zero(grid, x, y):
                # verify_all_numbers(grid, x, y)
                for n in range(1, 10):
                    if is_possible(grid, n, x, y):
                        grid[x][y] = n
                        solve(grid)
                        grid[x][y] = 0
                return

    # for x in range(9):
        # for y in range(9):
            # if grid[x][y] == 0:
                # for n in range(1,10):
                    # if is_possible(grid, n, x, y):
                        # grid[x][y] = n
                        # solve(grid)
                        # grid[x][y] = 0
                # return
    print("Solution:\n")
    print(np.matrix(grid), "\n")
