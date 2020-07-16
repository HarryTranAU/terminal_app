import numpy
import solver

# Sample sudokus
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

# Messages
navigation_message = """\nWelcome to my Sudoku App!
Navigation: Type in the word or number
1. Solve
0. Exit\n"""

row_message = """\nInput your Sudoku one row at a time, top to bottom
Enter empty cells as 0 and number cells as the number 1-9
Type 'back' to remove last row, 'exit' to return to navigation\n"""

exit_app = "\nBye!"

# Prints the sudoku to terminal
def displayBoard(sudoku):
    print(numpy.matrix(sudoku))


# Takes user input
def userInputRow():
    userSudoku = []
    while len(userSudoku) < 9:
        userRow = input(row_message)
        # Sanitize input
        userRow = userRow.replace(" ","")
        
        # Check input
        if userRow == "back":
            try:
                userSudoku.pop()
                displayBoard(userSudoku)
                continue
            except IndexError:
                print("Nothing to remove, try again\n")
                continue
        
        if userRow == "exit":
            return []
        
        if len(userRow) != 9:
            print("Invalid length, try again\n")
            displayBoard(userSudoku)
        else:
            try:
                int(userRow)
                # Convert string to list of int
                userSudoku.append(list(map(int,userRow)))
                displayBoard(userSudoku)
                
            except ValueError:
                print("Invalid input, please use integers from 0-9\n")

    return userSudoku


# Main loop / Navigation
while True:
    userDecision = input(navigation_message)

    # Sanitise input
    userDecision = userDecision.lower().replace(" ", "")

    # 1. Solve
    if userDecision in ["1", "solve"]:
        userSudoku = userInputRow()
        if userSudoku == []:
            continue
        elif solver.isValidSudoku(userSudoku):
            print("\nSolution:")
            solver.solve(userSudoku)
            displayBoard(userSudoku)
        else:
            print("Sudoku not valid")

    # 0. Exit
    if userDecision in ["0", "exit"]:
        print(exit_app)
        break


# Tests

# display
# displayBoard(solved) # terminal display
# displayBoard(unsolved) # terminal display

# isValidMove function
# print(solver.isValidMove(unsolved,4,4,5)) # True
# print(solver.isValidMove(unsolved,0,2,5)) # False
# print(solver.isValidMove(solved,0,0,4)) # True

# isValidSudoku function
# print(solver.isValidSudoku(solved)) # True
# print(solver.isValidSudoku(unsolved)) # True
# print(solver.isValidSudoku(invalid_unsolved)) # False

# solve function
# displayBoard(unsolved)
# solver.solve(unsolved)
# print("solution:")
# displayBoard(unsolved)

# displayBoard(test_1)
# solver.solve(test_1)
# print(f"solution {solver.isValidSudoku(test_1)}")
# displayBoard(test_1)

# User Input
# userInputRow()
