
""" 
This functions are basically all the same and could be grouped into one.
They are kept seperate for row, column and box for readability.
"""

def find_single_possibilities_row(field, row):
    """ Check if a possibility in the field only appears ones in a row. Sets the possibility to that value if so """
    # Only check the unset numbers
    if field.number == 0:
        for num in field.possible:
            # The num_found_times is the amount of times the possibility has been found in other fields
            num_found_times = 0
            for other_field in row:
                if other_field.id != field.id:
                    if num in other_field.possible:
                        num_found_times += 1
            # If the possibility only is found in the working field then that is our number!
            if num_found_times == 0:
                return {num}
    return field.possible


def find_single_possibilities_column(field, column):
    """ Check if a possibility in the field only appears ones in a column. Sets the possibility to that value if so """
    # Only check the unset numbers
    if field.number == 0:
        for num in field.possible:
            # The num_found_times is the amount of times the possibility has been found in other fields
            num_found_times = 0
            for other_field in column:
                if other_field.id != field.id:
                    if num in other_field.possible:
                        num_found_times += 1
            # If the possibility only is found in the working field then that is our number!
            if num_found_times == 0:
                return {num}
    return field.possible


def find_single_possibilities_box(field, box):
    """ Check if a possibility in the field only appears ones in a box. Sets the possibility to that value if so """
    # Only check the unset numbers
    if field.number == 0:
        for num in field.possible:
            # The num_found_times is the amount of times the possibility has been found in other fields
            num_found_times = 0
            for other_field in box:
                if other_field.id != field.id:
                    if num in other_field.possible:
                        num_found_times += 1
            # If the possibility only is found in the working field then that is our number!
            if num_found_times == 0:
                return {num}
    return field.possible