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
- [x] Load a sudoku in a usable list
- [x] Print a good looking sudoku
- [x] Add ID-number for each square
- [x] Create simple solution loop
    - [x] Loop trough the square-list and remove possible numbers
    - [x] Check if numbers in a row, column or box just have one possibility
    - [x] Create a win condition
    - [x] Create a failure
- [x] Add unit tests
    - [x] Create a folder and file structure for unit tests
    - [x] Test a unit test on one of the functions
    - [x] Implement relevant unit tests on all functions
- [x] Create a more advance solution method
    - [x] Add more advanced sudoku to test on
    - [x] Remove possible numbers based on combinations of two numbers in rows, columns and boxes
- [x] Create a very advanced solution method
    - [x] Add even more advanced sudokus to test on
    - [x] Remove possible numbers based on combination of tree numbers in rows, columns and boxes
    - [x] Guess numbers with brute force solution if the other methods fail
- [x] Better UI
    - [x] Improve input of new sudokus
    - [x] Make the output nicer
- [ ] Database of sudokus
    - [ ] Create database of sudokus
    - [ ] Enable "load sudoku called sudoku_v2" from database
    - [ ] Enable "save sudoku called sudoku_john" in database
- [ ] Make the solver web based