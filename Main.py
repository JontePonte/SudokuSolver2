""" Main file for SudokuSolver2"""

from Sudokus import sudoku          # The sudoku is chosen in the Sudokus file
from FieldClass import Field
from axiliary_functions import load_sudoku, check_field_possible_number, print_sudoku, print_two_sudokus
from create_rows_columns_boxes import create_rows, create_columns, create_boxes

# Solving functions
from simple_remove_possibilities import simple_remove_possibilities_row, simple_remove_possibilities_column, simple_remove_possibilities_boxe


# Create field objects for the sudoku
fields = load_sudoku(sudoku)
fields_old = load_sudoku(sudoku)

# Create lists for all rows, column and boxes
rows = create_rows(fields)
columns = create_columns(fields)
boxes = create_boxes(fields)

def find_single_possibilities_row(row):
    pass

for i in range(10):
    for field in fields:
        field.possible = simple_remove_possibilities_row(field, rows[field.y])
        field.possible = simple_remove_possibilities_column(field, columns[field.x])
        field.possible = simple_remove_possibilities_boxe(field, boxes[field.box])
        field.number = check_field_possible_number(field)

print_two_sudokus(fields_old, fields)
