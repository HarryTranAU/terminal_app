import numpy
import solver

# sample sudoku
solved = [[4,3,5,2,6,9,7,8,1],
          [6,8,2,5,7,1,4,9,3],
          [1,9,7,8,3,4,5,6,2],
          [8,2,6,1,9,5,3,4,7],
          [3,7,4,6,8,2,9,1,5],
          [9,5,1,7,4,3,6,2,8],
          [5,1,9,3,2,6,8,7,4],
          [2,4,8,9,5,7,1,3,6],
          [7,6,3,4,1,8,2,5,9]]

unsolved = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]

invalid_unsolved = [[5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,7]]

test_1 = [[0,0,0,0,0,0,0,2,0],
          [0,0,1,3,0,8,0,0,0],
          [9,8,0,0,0,7,3,4,0],
          [0,6,0,0,0,5,0,0,0],
          [8,9,0,0,0,0,0,3,7],
          [0,0,0,7,0,0,0,8,0],
          [0,2,3,6,0,0,0,1,5],
          [0,0,0,5,0,1,2,0,0],
          [0,1,0,0,0,0,0,0,0]]

# prints the sudoku to terminal
def display_board(sudoku):
    print(numpy.matrix(sudoku))

# takes user input
def userInputRow():
    userSudoku = []
    while len(userSudoku) < 9:
        userRow = input("""Input your Sudoku one row at a time, top to bottom
Enter empty cells as 0 and number cells as the number 1-9
Type 'back' to remove last row\n""")
        # Sanitize input

        # Check input
        if userRow == "back":
            try:
                userSudoku.pop()
                continue
            except IndexError:
                print("Nothing to remove, try again\n")
                continue
        
        if len(userRow) != 9:
            print("Invalid length, try again\n")
        else:
            try:
                int(userRow)
                # convert string to list of int
                userSudoku.append(list(map(int,userRow)))
                display_board(userSudoku)
                
            except ValueError:
                print("Invalid input, please use integers from 0-9\n")

    return userSudoku

# tests

# display
# display_board(solved) # terminal display
# display_board(unsolved) # terminal display

# isValidMove function
# print(solver.isValidMove(unsolved,4,4,5)) # True
# print(solver.isValidMove(unsolved,0,2,5)) # False
# print(solver.isValidMove(solved,0,0,4)) # True

# isValidSudoku function
# print(solver.isValidSudoku(solved)) # True
# print(solver.isValidSudoku(unsolved)) # True
# print(solver.isValidSudoku(invalid_unsolved)) # False

# solve function
# display_board(unsolved)
# solver.solve(unsolved)
# print("solution:")
# display_board(unsolved)

# display_board(test_1)
# solver.solve(test_1)
# print(f"solution {solver.isValidSudoku(test_1)}")
# display_board(test_1)

# User Input
userInputRow()
