import itertools


def remove_poss_just_three(list_input):
    """ If a set of three possibilities only exists in tree fields then remove them from every other field """
    list_work = list_input  # create a copy of the list (not sure this does anythin)
    
    # Create a test set of every two numbers
    for num1 in list(range(1,10)):
        for num2 in list(range(num1,10)):
            if num2 != num1:
                for num3 in list(range(1,10)):
                    if num3 != num1 and num3 != num2:
                        # this is every test set plus some unnessasary
                        test_set = {num1, num2, num3}

                        ts_found_counter = 0
                        ts_id = []
                        # Run throu all fields and check if their possibilities are the same as the test set
                        for field in list_work:
                            if test_set == field.possible:
                                ts_found_counter += 1           # Count how many times they appear
                                ts_id.append(field.id)          # and store the field id
                        
                        # If the test set appears two times in the fields remove the test set from every other field
                        if ts_found_counter == 3:
                            for field in list_work:
                                if not field.id in ts_id:
                                    field.possible.discard(list(test_set)[0])
                                    field.possible.discard(list(test_set)[1])
                                    field.possible.discard(list(test_set)[2])
    
    return list_work


def remove_extra_poss3_field(field, list):
    """ Remove extra possibilities in a field if three of the possibilities just appear in two other fields and nowhare else """
    
    if len(field.possible) <= 3:
        # No need to remove anything if there is just one, two or three possibilities
        return field.possible
    
    if len(list) != 9:
        raise ValueError("The list length need to be nine")
    
    possible = field.possible

    # Create a list of all subset of length 3 in possible
    combos_of_three = [set(i) for i in itertools.combinations(possible, 3)]

    for poss_set in combos_of_three:

        all_found_counter = 0
        no_found_counter = 0

        for other_field in list:
            # loop all ther field in the list
            if other_field.id != field.id:
                # Count the times the whole set appears and not appears at all in the other fields
                if other_field.possible.issuperset(poss_set):
                    all_found_counter += 1
                if other_field.possible.isdisjoint(poss_set):
                    no_found_counter += 1

        # If the three possibilities just appears in two other field and in no other field then remove!
        if all_found_counter == 2 and no_found_counter == 6:
            possible = poss_set
            return possible

    return possible

