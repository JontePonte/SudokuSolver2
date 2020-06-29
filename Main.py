""" Main file for SudokuSolver2"""

from Sudokus import sudoku          # The sudoku is chosen in the Sudokus file
from FieldClass import Field
from axiliary_functions import load_sudoku, check_field_possible_number, is_solved, print_sudoku, print_two_sudokus
from create_rows_columns_boxes import create_rows, create_columns, create_boxes

# Solving functions
from simple_remove_possibilities import simple_remove_possibilities_row, simple_remove_possibilities_column, simple_remove_possibilities_boxe
from find_single_possibilities import find_single_possibilities_row, find_single_possibilities_column, find_single_possibilities_box


# Create field objects for the sudoku
fields = load_sudoku(sudoku)
fields_old = load_sudoku(sudoku)

# Create lists for all rows, column and boxes
rows = create_rows(fields)
columns = create_columns(fields)
boxes = create_boxes(fields)


# Loop all the fields max 20 times and run all solving functions. 
counter = 0
while not is_solved(fields) and counter < 19:
    for field in fields:
        field.possible = simple_remove_possibilities_row(field, rows[field.y])
        field.possible = simple_remove_possibilities_column(field, columns[field.x])
        field.possible = simple_remove_possibilities_boxe(field, boxes[field.box])

        field.possible = find_single_possibilities_row(field, rows[field.y])
        field.possible = find_single_possibilities_column(field, columns[field.x])
        field.possible = find_single_possibilities_box(field, boxes[field.box])

        # Set the finds number if there is only one possibility
        field.number = check_field_possible_number(field)
    counter += 1

print(" ")
if is_solved(fields):
    print("The sudoku was solved after", str(counter+1), "iterations")
else:
    print("The sudoku was not solved after", str(counter+1), "iterations")

# The original and the hopfully solved sudoku are printed side by side
print_two_sudokus(fields_old, fields)
