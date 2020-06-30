
def find_single_possibilities(field, list):
    """ Check if a possibility in the field only appears ones in a list of fields. Sets the fields possibility to that value if so """
    
    if len(list) != 9:
        raise ValueError("The list input to find_single_possibilities must be == 9")
    
    # Only check the unset numbers
    if field.number == 0:
        for num in field.possible:
            # The num_found_times is the amount of times the possibility has been found in other fields
            num_found_times = 0
            for other_field in list:
                if other_field.id != field.id:
                    if num in other_field.possible:
                        num_found_times += 1
            # If the possibility only is found in the working field then that is our number!
            if num_found_times == 0:
                return {num}
    return field.possible
