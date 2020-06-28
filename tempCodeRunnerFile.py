for field in fields:
    field.possible = remove_possibilities_rows(field, row[field.y])
