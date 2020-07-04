
def guess_and_try(fields):
    field_2poss = []

    for field in fields:
        if len(field.possible) == 2:
            field_2poss.append(field)
