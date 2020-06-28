
def create_rows(fields):
    """ Store all fields in lists of rows """
    rows = []
    row = []
    for field in fields:
        row.append(field)
        # Save row list and create new list when the row is finnished
        if field.x == 8:
            rows.append(row)
            row = []
            
    return rows


def create_columns(fields):
    """ Store all fields in lists of columns """
    columns = []
    column = []
    column_num = list(range(9))

    for num in column_num:    
        for field in fields:
            if field.x == num:
                column.append(field)
                # Save column list and create new list when the column is finnished
                if field.y == 8:
                    columns.append(column)
                    column = []
                    
    return columns


def create_boxes(fields):
    """ Store all fields in lists of columns """
    boxes = []
    box = []
    box_num = list(range(9))

    for num in box_num:    
        for field in fields:
            if field.box == num:
                box.append(field)
                # Save box list and create new list when the box is full
                if len(box) == 9:
                    boxes.append(box)
                    box = []
                    
    return boxes
