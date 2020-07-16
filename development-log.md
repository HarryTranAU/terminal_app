16/7/20
Solver feature is finished.
Successes:
- solver takes in only numbers (invalid inputs do not crash app)


Roadblocks:
- isValidSudoku function checks to see if sudoku has any duplicates. Issue: all sudokus including valid examples returned False(invalid). Logic bug identified: sudoku cell was compared to every number in the row/column/square (including itself)
