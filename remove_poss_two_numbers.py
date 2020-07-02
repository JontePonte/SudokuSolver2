

def remove_poss_just_two(list_input):
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


def remove_extra_poss_field(field, list):
    """ Remove extra possibilities in a field if two of the possibilities just appear in one other field once """
    return field.possible


def remove_extra_poss_if_two(list_input):
    list_work = list_input  # create a copy of the list (not sure this does anythin)

    if len(list_work) != 9:
        raise ValueError("The list length need to be nine")
    
    # Create a test set of every two numbers
    for num1 in list(range(1,10)):
        for num2 in list(range(num1,10)):
            if num2 != num1:
                # this is every test set
                test_set = {num1, num2}

                num1_counter = 0
                num2_counter = 0
                ts_found_counter = 0
                ts_id = []
                # Run throu all fields and check if the test set appears in them
                # also check if the numbers appears by them selves
                for field in list_work:
                    if num1 in field.possible and num2 in field.possible:
                        ts_found_counter += 1
                        ts_id.append(field.id)

                    if num1 in field.possible:
                        num1_counter += 1

                    if num2 in field.possible:
                        num2_counter += 1

                # If the test set appears two times in the fields and in no other field
                # then remove all other possibilities in the fields
                if ts_found_counter == 2 and num1_counter == 2 and num2_counter == 2:
                    for field in list_work:
                        # Look up the fields based on id
                        if field.id in ts_id:
                            field.possible = test_set
    
    return list_work