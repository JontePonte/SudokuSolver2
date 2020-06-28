""" Main file for SudokuSolver2"""

from Sudokus import sudoku          # The sudoku is chosen in the Sudokus file
from FieldClass import Field
from axiliary_functions import load_sudoku, create_rows, print_sudoku


fields = load_sudoku(sudoku)
rows = create_rows(fields)

print_sudoku(fields)
print(fields[10].box)