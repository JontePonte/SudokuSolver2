# The field class is needed for the creation of readable sudoku
from FieldClass import Field


def set_box_number(x, y):
    """ Get the number of the box the hard way... """
    
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("x and y in set_box_number needs to be integer")

    if y <= 2:
        if x <= 2:
            box_number = 0
        elif 3 <= x <= 5:
            box_number = 1
        elif 6 <= x <= 8:
            box_number = 2
    elif 3 <= y <= 5:
        if x <= 2:
            box_number = 3
        elif 3 <= x <= 5:
            box_number = 4
        elif 6 <= x <= 8:
            box_number = 5
    elif 6 <= y <= 8:
        if x <= 2:
            box_number = 6
        elif 3 <= x <= 5:
            box_number = 7
        elif 6 <= x <= 8:
            box_number = 8

    return box_number


def unpack_sudoku(fields):
    """ Create sudoku matrix from fields """
    output = []
    output_row = []
    # Create list in lists with all field numbers
    for field in fields:
        output_row.append(field.number)
        if field.x == 8:
            output.append(output_row)
            output_row = []
    return output


def load_sudoku(sudoku):
    """ Create a list of fields with all relevant information based on a sudoku. The sudoku needs to be in the form found in Sudokus.py """
    y = 0
    id_num = 0
    fields = []
    
    for row in sudoku:
        x = 0
        for number in row:
            # Create a field
            field = Field()

            # Set coordinates, 3x3 box and and id
            field.x = x
            field.y = y
            field.box = set_box_number(x, y)
            field.id = id_num
            

            field.number = number

            # If the field has a number, that is the only possibility
            if field.number != 0:
                field.possible = {field.number}

            fields.append(field)

            # Step up all index
            x += 1
            id_num += 1
        y += 1
        
    return fields


def check_field_possible_number(field):
    """ Check if the possible list in the field only contains one value. If so, set the number to the one possibility"""
    if len(field.possible) == 1:
        number = list(field.possible)[0]
    else:
        number = 0
    return number


def is_solved(fields):
    """ Returns true if solved and false if not """
    for field in fields:
        if field.number == 0:
            return False
    return True


def count_zeros(fields):
    """ Returns the number of zeros in the sudoku """
    num_zero = 0
    for field in fields:
        if field.number == 0:
            num_zero += 1
    return num_zero


def copy_fields(fields):
    """ Create a copy of the fields in the list called "fields" """
    fields_c = []
    for field in fields:
        # copy all values in the fields and append them to copy list
        f = Field()
        f.x = field.x
        f.y = field.y
        f.box = field.box
        f.id = field.id

        f.number = field.number
        f.possible = field.possible

        fields_c.append(f)
    
    return fields_c


def print_sudoku(fields):
    """ Print the list of fields in a nice sudoku-like way"""
    output = []
    output_row = []
    # Create list in lists with all field numbers
    for field in fields:
        output_row.append(field.number)
        if field.x == 8:
            output.append(output_row)
            output_row = []

    # Print the numbers in output-list
    print(" ")
    for row in output:
        print(row)
    print(" ")


def print_two_sudokus(fields_old, fields):
    """ Print two sudokus named (fields_old and fields) side by side"""
    output_old = []
    output_old_row = []
    # Create list in lists with all field numbers
    for field in fields_old:
        output_old_row.append(field.number)
        if field.x == 8:
            output_old.append(output_old_row)
            output_old_row = []

    output = []
    output_row = []
    # Create list in lists with all field numbers
    for field in fields:
        output_row.append(field.number)
        if field.x == 8:
            output.append(output_row)
            output_row = []

    # Print the numbers in output_old and output lists
    print(" ")
    for row_old, row in zip(output_old, output):
        print(row_old, "   ", row)
    print(" ")

