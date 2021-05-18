# Arquivo responsável com as funções que vão resolver o sudoku.
import numpy

def verify_column(y, n):
    global grid

    for i in range(10):
        if grid[i][y] == n:
            return False

def verify_line(x, n):
    global grid

    for i in range(10):
        if grid[x][i] == n:
            return False

def verify_square(x, y, n):
    global grid

    x1 = (x // 3) * 3
    y1 = (y // 3) * 3

    for i in range(4):
        for j in range(4):
            if grid[x1+i][y1+j] == n:
                return False

def is_zero(x, y):
    global grid

    if grid[x][y] == 0:
        return True
    else:
        return False

def is_possible(n, x, y):
    global grid

    verify_column(y, n)
    verify_line(x, n)
    verify_square(x, y, n)

    return True


def verify_all_numbers(x, y):
    global grid

    for n in range(1, 10):
        if is_possible(n, x, y):
            grid[x][y] = n
            solve()
            grid[x][y] = 0
    return



def solve():
    global grid

    for x in range(9):
        for y in range(9):
            if is_zero(x, y):
                verify_all_numbers(x, y)

    print("Solução:\n")
    print(np.matrix(grid), "\n")
