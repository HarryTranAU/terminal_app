def isValidMove(sudoku, x, y, num):
    # check row
    for a in range(9):
        if sudoku[x][a] == num:
            return False

    # check column
    for a in range(9):
        if sudoku[a][y] == num:
            return False

    # check 3x3 square
    fx = (x//3) * 3
    fy = (y//3) * 3

    for a in range(3):
        for b in range(3):
            if sudoku[fx+a][fy+b] == num:
                return False
    
    # does not find duplicate
    return True
