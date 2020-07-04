
from auxiliary_functions import (check_field_possible_number, is_solved, copy_fields)
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


def try_guess(fields):
    """ Try the guess made in guess and try """
    rows = create_rows(fields)
    columns = create_columns(fields)
    boxes = create_boxes(fields)

    # Loop all the fields max 10 times and run all solving functions. 
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
            
            # If a pair of tree possibilities just appears in three fields in a row, column or box then remove them from all other
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
            
            # Set the finds number if there is only one possibility
            field.number = check_field_possible_number(field)
        counter += 1

        return fields


def guess_and_try(fields):
    """ Create copy of the fields, guess one possibility and try if it works """
    fields_c = copy_fields(fields)
    
    fields_2poss = []

    for field in fields_c:
        # Store all fields with two possibilities
        if len(field.possible) == 2:
            fields_2poss.append(field)

    if len(fields_2poss) == 0:
        # Break if there is no fields with two possibilities
        print("Guess and Try: No fields had two possibilities")
        return fields
    
    field_2poss = fields_2poss[0]

    print(list(field_2poss.possible))
    field_2poss.possible = {list(field_2poss.possible)[0]}
    field_2poss.number = list(field_2poss.possible)[0]

    try_guess(fields_c)

    return fields_c