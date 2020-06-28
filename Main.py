""" Main file for SudokuSolver2"""

from Sudokus import sudoku          # The sudoku is chosen in the Sudokus file
from FieldClass import Field
from axiliary_functions import load_sudoku, print_sudoku, check_field_possible_number
from create_rows_columns_boxes import create_rows, create_columns, create_boxes

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


for i in range(10):
    for field in fields:
        field.possible = simple_remove_possibilities_rows(field, rows[field.y])
        field.possible = simple_remove_possibilities_columns(field, columns[field.x])
        field.possible = simple_remove_possibilities_boxes(field, boxes[field.box])
        field.number = check_field_possible_number(field)

print_sudoku(fields)
