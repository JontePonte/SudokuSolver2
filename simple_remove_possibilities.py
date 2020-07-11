

def simple_remove_possibilities(field, field_list):
    """ Remove a fields possibilities if the numbers appear in the other fields in the row, column or box """
    possible = field.possible
    for other_field in field_list:
        if other_field.id != field.id:
            # Remove possibilities from the field by discarding the from the set
            possible.discard(other_field.number)
    return possible