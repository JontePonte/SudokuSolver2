# The field class is needed for the creation of readable sudoku
from FieldClass import Field


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
            field.box = 0
            field.id = id_num
            

            field.number = number

            # If the field has a number, that is the only possibility
            if field.number != 0:
                field.possible = [field.number]

            fields.append(field)

            # Step up all index
            x += 1
            id_num += 1
        y += 1
    return(fields)
