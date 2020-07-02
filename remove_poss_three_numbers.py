
def remove_poss_just_three(list_input):
    list_work = list_input  # create a copy of the list (not sure this does anythin)
    
    # Create a test set of every two numbers
    for num1 in list(range(1,10)):
        for num2 in list(range(num1,10)):
            if num2 != num1:
                # this is every test set
                test_set = {num1, num2}

                ts_found_counter = 0
                ts_id = []
                # Run throu all fields and check if their possibilities are the same as the test set
                for field in list_work:
                    if test_set == field.possible:
                        ts_found_counter += 1           # Count how many times they appear
                        ts_id.append(field.id)          # and store the field id
                
                # If the test set appears two times in the fields remove the test set from every other field
                if ts_found_counter == 2:
                    for field in list_work:
                        if not field.id in ts_id:
                            field.possible.discard(list(test_set)[0])
                            field.possible.discard(list(test_set)[1])
    
    return list_work


def remove_extra_poss3_field(field, list):
    """ Remove extra possibilities in a field if two of the possibilities just appear in one other field once """
    
    if len(field.possible) <= 2:
        # No need to remove anything if there is just one or two possibilities
        return field.possible
    
    if len(list) != 9:
        raise ValueError("The list length need to be nine")
    
    possible = field.possible

    for poss1 in field.possible:
        for poss2 in field.possible:
            # This creates sets of two of the possibilities (two many but ok for now)
            if poss1 != poss2:

                both_found_counter = 0
                poss1_found_counter = 0
                poss2_found_counter = 0

                for other_field in list:
                    # loop all ther field in the list
                    if other_field.id != field.id:
                        # Count the times both appear in the other field
                        if poss1 in other_field.possible and poss2 in other_field.possible:
                            both_found_counter += 1
                        
                        # Count the time each one appears in the other field
                        if poss1 in other_field.possible:
                            poss1_found_counter += 1

                        if poss2 in other_field.possible:
                            poss2_found_counter += 1

                # If the two possibilities just appears in one other field and in no other field then remove!
                if both_found_counter == 1 and poss1_found_counter == 1 and poss2_found_counter == 1:
                    possible = {poss1, poss2}

    return possible

