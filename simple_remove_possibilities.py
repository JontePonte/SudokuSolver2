

def simple_remove_possibilities_row(field, row):
    """ Remove a fields possibilities if the numbers appear in the fields row """
    possible = field.possible
    for other_field in row:
        if other_field.id != field.id:
            # Remove possibilities from the field by discarding the from the set
            possible.discard(other_field.number)
    return possible


def simple_remove_possibilities_column(field, column):
    """ Remove a fields possibilities if the numbers appear in the fields column """
    possible = field.possible
    for other_field in column:
        if other_field.id != field.id:
            # Remove possibilities from the field by discarding the from the set
            possible.discard(other_field.number)
    return possible


def simple_remove_possibilities_box(field, box):
    """ Remove a fields possibilities if the numbers appear in the fields box """
    possible = field.possible
    for other_field in box:
        if other_field.id != field.id:
            # Remove possibilities from the field by discarding the from the set
            possible.discard(other_field.number)
    return possible