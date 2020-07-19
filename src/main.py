#! /usr/sbin/python
import itertools
import random
import copy
import datetime
import numpy
import termcolor
import os
import sys
import solver

if "--help" in sys.argv:
    print("""
--rule
    How to play Sudoku. Print out rules

--colorblind
    Change color of error messages. Change to blue with white background. Default: red, no background. 
    """)
    exit()

if "--rule" in sys.argv:
    print("""
The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9.    
    """)
    exit()

error_color = "red"
error_back = None

if "--colorblind" in sys.argv:
    error_color = "blue"
    error_back = "on_white"


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
        a b c   d e f   g h i
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
"""


# Messages
welcome_message = """
**********************************************
| Welcome to my Sudoku App!                  |
**********************************************
"""

navigation_message = """
**********************************************
|                                            |
| Navigation: Type in the word or number     |
|                                            |
| 1. Solver (Get a solution to your Sudoku)  |
| 2. Play   (Generate a Sudoku to play)      |
|                                            |
| 0. Exit                                    |
**********************************************
"""

row_message = """
Input your Sudoku one row at a time, top to bottom. Example: 009028007
Enter empty cells as 0 and number cells as the number 1-9
Type 'back' to remove last row, 'exit' to return to navigation
"""

difficulty_message = """
Choose a difficulty. Type: easy, medium, hard
Type 'exit' to return to navigation
"""

play_instructions = """
To enter a number, type the coordinates(horizontal then vertical) followed by your answer
Example: To enter 9 in the top left corner, type a19
If you wish to quit, type 'exit'.
"""

exit_app = "\nThanks for playing! Have an awesome day!"


difficulty = { "easy": 5, "medium": 20, "hard": 64 }
positions = { "a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8 }

# Clear the terminal
def clear():
    # for windows
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Prints the sudoku to terminal
def displayBoard(sudoku):
    print(better_looking_board.format(*list(itertools.chain(*sudoku))).replace("0", "."))


# Takes user input
def userInputRow():
    user_Sudoku = []
    error_message = ""
    while len(user_Sudoku) < 9:
        print(row_message)
        if error_message:
            termcolor.cprint(error_message, error_color, error_back)
            error_message = ""
        userRow = input("Input: ").replace(" ","").replace(",","").replace(".","")
        
        # Check input
        if userRow == "":
            clear()
            error_message = "No Input, Try again"
            print(numpy.matrix(user_Sudoku))
        elif userRow == "back":
            clear()
            try:
                user_Sudoku.pop()
                print(numpy.matrix(user_Sudoku))
                continue
            except IndexError:
                error_message = "Nothing to remove, try again"
                continue
        
        elif userRow == "exit":
            clear()
            return []
        
        elif len(userRow) != 9:
            clear()
            error_message = "Invalid length, try again"
            print(numpy.matrix(user_Sudoku))
        else:
            try:
                int(userRow)
                user_Sudoku.append(list(map(int,userRow))) # Convert str to list of int for use when creating 9x9 grid
                clear()
                print(numpy.matrix(user_Sudoku))
                
            except ValueError:
                clear()
                error_message = "Invalid input, please use integers from 0-9"
                print(numpy.matrix(user_Sudoku))

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
        else:
            termcolor.cprint("Please choose 'yes' or 'no'", error_color, error_back)

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
    user_move = ""
    error_message = ""
    while play_counter > 0:
        clear()
        displayBoard(sudoku)
        # Play instructions
        print(play_instructions)
        print(f"missing numbers left: {play_counter}")
        print(f"Previous Input: {user_move}")
        # move is valid unless flag 
        move_valid = True

        if error_message:
            termcolor.cprint(error_message, error_color, error_back)
            error_message = ""

        user_move = input("Input: ").lower().replace(" ", "").replace(",", "")

        # Exit play
        if user_move == "exit":
            break
        # Invalid move if string is bigger than 3
        elif len(user_move) != 3:
            error_message = "Invalid move length. Expected: 3 characters"
            move_valid = False
        # First char between a-i
        elif user_move[0] not in horizontal or user_move[1] not in vertical[:9] or user_move[2] not in vertical:
            error_message = "Invalid move. Expected: Horizontal first (a-i), Vertical second (1-9), answer last (1-9)"
            move_valid = False
        # Is move in an initially empty cell
        elif (int(user_move[1])-1, positions[user_move[0]]) not in empty_cells:
            error_message = "Cannot overwrite this cell. Empty cells are marked with '.'"
            move_valid = False
        # If move is "."
        elif user_move[2] == ".":
            sudoku[int(user_move[1])-1][positions[user_move[0]]] = 0
            play_counter -= 1
            continue
        # Find duplicate
        elif not solver.isValidMove(sudoku,int(user_move[1])-1, positions[user_move[0]], int(user_move[2])):
            error_message = "Answer not correct. Duplicate found in row/column/square"
            move_valid = False

        # If move is valid
        if move_valid == False:
            continue
        
        sudoku[int(user_move[1])-1][positions[user_move[0]]] = int(user_move[2])
        play_counter -= 1
    
    # Play ends when no spaces left to fill
    clear()
    displayBoard(sudoku)
    # Print timer if used
    if user_time:
        timer(user_time)
    
    if play_counter == 0:
        termcolor.cprint("You Finished!", "blue")
        input("Press 'enter' to return to navigation...")
        clear()
    else:
        while True:
            want_solution = input("Would you like the solution to this Sudoku(yes/no)? ").lower().replace(" ", "")
            if want_solution == "yes":
                solver.solve(generatedSudoku)
                displayBoard(generatedSudoku)
                input("Here is the solution. Press 'enter' to continue...")
                clear()
                break
            elif want_solution == "no":
                clear()
                break
            else:
                termcolor.cprint("Please choose 'yes' or 'no'", error_color, error_back)

# Application start
print(welcome_message)
userDecision = ""
error_message = ""

# Main loop / Navigation
while True:
    print(navigation_message)
    if error_message:
        termcolor.cprint(error_message, error_color, error_back)
        error_message = ""
    userDecision = input("Input: ").lower().replace(" ", "")

    # 1. Solve
    if userDecision in ["1", "solver"]:
        clear()
        user_Sudoku = userInputRow()
        if user_Sudoku == []: # If user exits solver
            continue
        elif solver.isValidSudoku(user_Sudoku): # Checks if user's sudoku is solvable
            print("\nSolution:")
            solver.solve(user_Sudoku)
            displayBoard(user_Sudoku)
        else:
            termcolor.cprint("Sudoku not valid", error_color, error_back)
            input("Press 'enter' to go back to navigation...")
            clear()

    # 2. Play
    elif userDecision in ["2", "play"]:
        while True:
            clear()
            print(difficulty_message)
            if error_message:
                termcolor.cprint(error_message, error_color, error_back)
                error_message = ""
            user_difficulty = input("Input: ").lower().replace(" ", "")

            if user_difficulty in difficulty:
                print("Generating Sudoku. Please wait...")
                generatedSudoku = generateSudoku(user_difficulty)
                play(generatedSudoku)
                
                # Finish generation and solution
                break
            
            elif user_difficulty == "exit":
                break
            else:
                error_message = "Please type 'easy', 'medium', or 'hard'"

    # 0. Exit
    elif userDecision in ["0", "exit"]:
        print(exit_app)
        break
    
    else:
        clear()
        error_message = "Input not valid. Please type '1' for Solver, '2' for Play, or '0' to exit"


