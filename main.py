import itertools
import random
import copy
import datetime
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

blank_board = [[0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0]]

better_looking_board = """
      +-------+-------+-------+
    1 | {} {} {} | {} {} {} | {} {} {} |
    2 | {} {} {} | {} {} {} | {} {} {} |
    3 | {} {} {} | {} {} {} | {} {} {} |
      +-------+-------+-------+
    4 | {} {} {} | {} {} {} | {} {} {} |
    5 | {} {} {} | {} {} {} | {} {} {} |
    6 | {} {} {} | {} {} {} | {} {} {} |
      +-------+-------+-------+
    7 | {} {} {} | {} {} {} | {} {} {} |
    8 | {} {} {} | {} {} {} | {} {} {} |
    9 | {} {} {} | {} {} {} | {} {} {} |
      +-------+-------+-------+
        a b c   d e f   g h i
"""


# Messages
navigation_message = """
**********************************************
| Welcome to my Sudoku App!                  |
|                                            |
| Navigation: Type in the word or number     |
|                                            |
| 1. Solver (Get a solution to your Sudoku)  |
| 2. Play   (Generate a Sudoku to play)      |
|                                            |
| 0. Exit                                    |
**********************************************
Input: """

row_message = """
Input your Sudoku one row at a time, top to bottom. Example: 009028007
Enter empty cells as 0 and number cells as the number 1-9
Type 'back' to remove last row, 'exit' to return to navigation
Input: """

difficulty_message = """
Choose a difficulty. Type: easy, medium, hard
Type 'exit' to return to navigation
Input: """

play_instructions = """
To enter a number, type the coordinates(horizontal then vertical) followed by your answer
Example: To enter 9 in the top left corner, type a19
If you wish to quit, type 'exit'.
"""

exit_app = "\nBye!"


difficulty = { "easy": 5, "medium": 20, "hard": 64 }
positions = { "a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8 }

# Prints the sudoku to terminal
def displayBoard(sudoku):
    print(better_looking_board.format(*list(itertools.chain(*sudoku))).replace("0", "."))


# Takes user input
def userInputRow():
    user_Sudoku = []
    while len(user_Sudoku) < 9:
        userRow = input(row_message).replace(" ","").replace(",","").replace(".","")
        
        # Check input
        if userRow == "":
            print("No Input, Try again\n")
        if userRow == "back":
            try:
                user_Sudoku.pop()
                print(numpy.matrix(user_Sudoku))
                continue
            except IndexError:
                print("Nothing to remove, try again\n")
                continue
        
        if userRow == "exit":
            return []
        
        if len(userRow) != 9:
            print("Invalid length, try again\n")
            print(numpy.matrix(user_Sudoku))
        else:
            try:
                int(userRow)
                user_Sudoku.append(list(map(int,userRow))) # Convert str to list of int for use when creating 9x9 grid
                print(numpy.matrix(user_Sudoku))
                
            except ValueError:
                print("Invalid input, please use integers from 0-9\n")

    return user_Sudoku

# Generate sudoku
def generateSudoku(diff):
    new_Sudoku = copy.deepcopy(blank_board)

    # Create a random valid filled Sudoku
    random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(random_list)
    for i in range(9):
        new_Sudoku[i][random.randrange(9)] = random_list[i]
    solver.solve(new_Sudoku)
    
    # Replace cells with 0 according to difficulty
    counter = 0
    while counter < difficulty[diff]:
        a = random.randrange(9)
        b = random.randrange(9)
        if new_Sudoku[a][b] != 0:
            new_Sudoku[a][b] = 0
            counter += 1
    
    return new_Sudoku

# Timer Function
def timer(time=None):
    # User hits enter to start timer
    if time == None:
        input("Press 'enter' to start timer...")
        time = datetime.datetime.now()
    else:
        stop_time = datetime.datetime.now()
        time_delta = stop_time - time
        print(f"Your time: {time_delta.seconds//60} mins {time_delta.seconds%60} secs ")

    return time
    

# Play Sudoku function
def play(sudoku):

    user_time = False
    while True:
        time_question = input("Would you like a timer(yes/no)? ").lower().replace(" ","")
        if time_question == "yes":
            user_time = timer()
            break
        elif time_question == "no":
            break

    # Make list of empty cells to differentiate between sudoku puzzle and user moves
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                empty_cells.append((i,j))

    # While loop until sudoku has no moves left
    play_counter = len(empty_cells)
    horizontal = "abcdefghi"
    vertical = "1234567890."
    while play_counter > 0:
        displayBoard(sudoku)
        # Play instructions
        print(play_instructions)
        print(f"missing numbers left: {play_counter}")
        # move is valid unless flag 
        move_valid = True
        user_move = input("Input: ").lower().replace(" ", "").replace(",", "")

        # Exit play
        if user_move == "exit":
            break
        
        # Invalid move if string is bigger than 3
        if len(user_move) != 3:
            print("Invalid move length. Expected: 3 characters")
            move_valid = False
        # First char between a-i
        elif user_move[0] not in horizontal or user_move[1] not in vertical[:9] or user_move[2] not in vertical:
            print("Invalid move. Expected: Horizontal first (a-i), Vertical second (1-9), answer last (1-9)")
            move_valid = False
        # Is move in an initially empty cell
        elif (int(user_move[1])-1, positions[user_move[0]]) not in empty_cells:
            print("Cannot overwrite this cell")
            move_valid = False
        # If move is "."
        elif user_move[2] == ".":
            sudoku[int(user_move[1])-1][positions[user_move[0]]] = 0
            play_counter -= 1
            continue
        # Find duplicate
        elif not solver.isValidMove(sudoku,int(user_move[1])-1, positions[user_move[0]], int(user_move[2])):
            print("Duplicate Found")
            move_valid = False

        # If move is valid
        if move_valid == False:
            continue
        
        sudoku[int(user_move[1])-1][positions[user_move[0]]] = int(user_move[2])
        play_counter -= 1
    
    # Play ends when no spaces left to fill
    displayBoard(sudoku)
    # Print timer if used
    if user_time:
        timer(user_time)
    
    if play_counter == 0:
        print("You Finished!")
    else:
        while True:
            want_solution = input("Would you like the solution to this Sudoku(yes/no)? ").lower().replace(" ", "")
            if want_solution == "yes":
                solver.solve(generatedSudoku)
                displayBoard(generatedSudoku)
                break
            elif want_solution == "no":
                break

    return




# Main loop / Navigation
while True:
    userDecision = input(navigation_message).lower().replace(" ", "")

    # 1. Solve
    if userDecision in ["1", "solver"]:
        user_Sudoku = userInputRow()
        if user_Sudoku == []: # If user exits solver
            continue
        elif solver.isValidSudoku(user_Sudoku): # Checks if user's sudoku is solvable
            print("\nSolution:")
            solver.solve(user_Sudoku)
            displayBoard(user_Sudoku)
        else:
            print("Sudoku not valid")

    # 2. Generate
    if userDecision in ["2", "play"]:
        while True:
            user_difficulty = input(difficulty_message).lower().replace(" ", "")

            if user_difficulty in difficulty:
                generatedSudoku = generateSudoku(user_difficulty)
                play(generatedSudoku)
                # displayBoard(generatedSudoku)
                
                # while True:
                #     want_to_play = input("Would you like to play this Sudoku(yes/no)? ").lower().replace(" ", "")
                #     if want_to_play == "yes":
                #         play(generatedSudoku)
                #         break
                #     elif want_to_play == "no":
                #         break


                
                # Finish generation and solution
                break
            
            elif user_difficulty == "exit":
                break
            else:
                print("Please choose a difficulty from the list")

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
