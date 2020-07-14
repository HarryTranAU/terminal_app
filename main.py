import numpy
import solver

# sample sudoku
sudoku = [[4,3,5,2,6,9,7,8,1],
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

# prints the sudoku to terminal
def display_board(sudoku):
    print(numpy.matrix(sudoku))



# tests

# display
# display_board(sudoku) # terminal display
# display_board(unsolved) # terminal display

# isValidMove function
print(solver.isValidMove(unsolved,4,4,5)) # True
print(solver.isValidMove(unsolved,0,2,5)) # False
