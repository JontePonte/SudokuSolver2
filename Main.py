""" Main file for SudokuSolver2"""

from Sudokus import sudoku          # The sudoku is chosen in the Sudokus file
from FieldClass import Field
from auxiliary_functions import (load_sudoku, 
                                 check_field_possible_number, 
                                 is_solved, 
                                 count_zeros, 
                                 print_sudoku,
                                 print_two_sudokus)
from create_rows_columns_boxes import (create_rows, 
                                      create_columns, 
                                      create_boxes)

# Solving functions
from simple_remove_possibilities import (simple_remove_possibilities_row, 
                                         simple_remove_possibilities_column, 
                                         simple_remove_possibilities_box)
from find_single_possibilities import find_single_possibilities
from remove_poss_two_numbers import (remove_poss_just_two, 
                                     remove_extra_poss_field)
from remove_poss_three_numbers import (remove_poss_just_three,
                                       remove_extra_poss3_field)
from recursive_solution import RecursivSolv


# Create field objects for the sudoku
fields = load_sudoku(sudoku)
fields_old = load_sudoku(sudoku)

# Create lists for all rows, column and boxes
rows = create_rows(fields)
columns = create_columns(fields)
boxes = create_boxes(fields)


# Loop all the fields max 20 times and run all solving functions. 
counter = 1
while not is_solved(fields) and counter < 20:
    for field in fields:
        # Remove possibilities if field if they appears in the same row, colomn or box
        field.possible = simple_remove_possibilities_row(field, rows[field.y])
        field.possible = simple_remove_possibilities_column(field, columns[field.x])
        field.possible = simple_remove_possibilities_box(field, boxes[field.box])

        # Remove all other possibilities if a possibility only appears ones in a row, column or box
        field.possible = find_single_possibilities(field, rows[field.y])
        field.possible = find_single_possibilities(field, columns[field.x])
        field.possible = find_single_possibilities(field, boxes[field.box])
        
        # If a pair of two possibilities just appears in two fields in a row, column or box then remove them from all other
        # them from all other fields in that row, column or box
        for row in rows:
            row = remove_poss_just_two(row)
        for column in columns:
            column = remove_poss_just_two(column)
        for box in boxes:
            box = remove_poss_just_two(box)
        
        # Remove extra possibilities in a field if two of the possibilities just appear in one other
        # field in the row, column or box
        field.possible = remove_extra_poss_field(field, rows[field.y])
        field.possible = remove_extra_poss_field(field, columns[field.x])
        field.possible = remove_extra_poss_field(field, boxes[field.box])
        
        """ The functions testing three solutions are commented out to increase prefomance
            All sudokus can be solved using the recursive solution instead
        
        # If a pair of three possibilities just appears in three fields in a row, column or box then remove them from all other
        # them from all other fields in that row, column or box
        for row in rows:
            row = remove_poss_just_three(row)
        for column in columns:
            column = remove_poss_just_three(column)
        for box in boxes:
            box = remove_poss_just_three(box)
        
        # Remove extra possibilities in a field if three of the possibilities just appear in two other
        # field in the row, column or box
        field.possible = remove_extra_poss3_field(field, rows[field.y])
        field.possible = remove_extra_poss3_field(field, columns[field.x])
        field.possible = remove_extra_poss3_field(field, boxes[field.box])
        """
        
        # Set the finds number if there is only one possibility
        field.number = check_field_possible_number(field)
    counter += 1        


# If the solution method cant solve the sudoku in 20 iterations the recursive solution kiks in
if not is_solved(fields):
    used_recursive = True
    sudo = RecursivSolv(fields)             # Call recursive solution method
    fields = load_sudoku(sudo.sudoku_num)   # Update fields from RecursiveSolve output
else:
    used_recursive = False                  # Just for print output


print(" ")
if is_solved(fields):
    if not used_recursive:
        print("The sudoku was solved after", str(counter), "iterations")
    else:
        print("The sudoku was solved after", str(counter), "iterations and used recursive solution")
else:
    print("The sudoku was not solved after", str(counter), "iterations")
    print(count_zeros(fields), "unsolved fields")

# The original and the hopfully solved sudoku are printed side by side
print_two_sudokus(fields_old, fields)
