16/7/20
Solver feature complete
Successes:
- solver takes in only numbers (invalid inputs do not crash app)


Roadblocks:
- isValidSudoku function checks to see if sudoku has any duplicates. Issue: all sudokus including valid examples returned False(invalid). Logic bug identified: sudoku cell was compared to every number in the row/column/square (including itself)


17/7/20
Generate sudoku feature complete
Generate feature was easier to implement due to having the solve feature completed first. The idea behind the generate feature was to use the inbuild randomizer to generate a randomized list of numbers from 1 to 9. Then randomly add it to a blank sudoku. Use the solver to fill in the rest. Then take out numbers one by one according the difficulty chosen by the user.

Successes:
- updated display sudoku to show squares and co-ordinates

Roadblocks:
- 
