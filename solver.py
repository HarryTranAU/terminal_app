

# checks if there is a duplicate in row, column, 3x3 square
def isValidMove(sudoku, y, x, num):
    # check row
    for a in range(9):
        if sudoku[y][a] == num:
            return False

    # check column
    for a in range(9):
        if sudoku[a][x] == num:
            return False

    # check 3x3 square
    fx = (x//3) * 3
    fy = (y//3) * 3

    for a in range(3):
        for b in range(3):
            if sudoku[fy+a][fx+b] == num:
                return False
    
    # does not find duplicate
    return True


# checks if sudoku is valid
def isValidSudoku(sudoku):
    for a in range(9):
        for b in range(9):
            # if cell is not empty and finds a duplicate
            check_number = sudoku[a][b]
            if check_number == 0:
                continue

            sudoku[a][b] = 0
            if not isValidMove(sudoku, a, b, check_number):
                sudoku[a][b] = check_number
                return False
            sudoku[a][b] = check_number

    # is valid
    return True

# def solve(sudoku):
#     for y in range(9):
#         for x in range(9):
#             if sudoku[y][x] == 0:
#                 for num in range(1,10):
#                     if isValidMove(sudoku, y, x, num):
#                         sudoku[y][x] = num
#                         solve(sudoku)
#                         sudoku[y][x] = 0
#                     return
#     return
