""" Main file for SudokuSolver2"""

from Sudokus import sudoku          # The sudoku is chosen in the Sudokus file
from FieldClass import Field
from axiliary_functions import load_sudoku, create_rows, create_columns, create_boxes, print_sudoku


# Create field objects for the sudoku
fields = load_sudoku(sudoku)

# Create lists for all rows, column and boxes
rows = create_rows(fields)
columns = create_columns(fields)
boxes = create_boxes(fields)

print_sudoku(fields)
