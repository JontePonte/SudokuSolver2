# SudokuSolver2
Input a sudoku square and let the program solve it for you a second time.

This is the verion 2 of the sudoku solver. The goal with v2 is (other than solver harder sudokus) to improve code structure and implement unit tests.

Code structure design goals.
- Short Main.py that mainy just load and run sudokus and functions
- The main code body divided into smaller functions to improve readability
- Two levels of functions:
    - Single function functions. Ex."return numbers in row" or "find possibilities for numbers in column"
    - Solving functions. Ex "Find unset numbers in rows based on possibility eliminiation"
    - The solving functions will start in Main.py but problably move to seperate file
- Unit tests in every function will help to keep everything in check

The project is launched to improve my programming skills and give me a reason to properly learn unit tests and debugging.

# Roadmap
Same as version 1 for now
- [ ] Load a sudoku in a usable list
- [ ] Print a good looking sudoku
- [ ] Add ID-number for each square
- [ ] Create simple solution loop
    - [ ] Loop trough the square-list and remove possible numbers
    - [ ] Check if numbers in a row, column or box just have one possibility
    - [ ] Create a win condition
    - [ ] Create a failure condition
- [ ] Create a more advance solution method
    - [ ] Add more advanced sudoku to test on
    - [ ] Remove possible numbers based on combinations of numbers elsewere
- [ ] Create a very advanced solution method
    - [ ] Add even more advanced sudoku to test on
    - [ ] Test numbers if the other methods fail
- [ ] Better input for the sudoku