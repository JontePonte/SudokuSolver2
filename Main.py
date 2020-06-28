""" Main file for SudokuSolver2"""

from Sudokus import sudoku          # The sudoku is chosen in the Sudokus file
from FieldClass import Field
from axiliary_functions import load_sudoku, create_rows, create_columns, create_boxes, print_sudoku

# Solving functions
from simple_remove_possibilities import simple_remove_possibilities_rows, simple_remove_possibilities_columns, simple_remove_possibilities_boxes


# Create field objects for the sudoku
fields = load_sudoku(sudoku)

# Create lists for all rows, column and boxes
rows = create_rows(fields)
columns = create_columns(fields)
boxes = create_boxes(fields)

# Create a print of the first initial sudoku
print_sudoku(fields)


print(fields[1].possible)

for field in fields:
    field.possible = simple_remove_possibilities_rows(field, rows[field.y])
    field.possible = simple_remove_possibilities_columns(field, columns[field.x])
    field.possible = simple_remove_possibilities_boxes(field, boxes[field.box])

print(fields[1].possible)
