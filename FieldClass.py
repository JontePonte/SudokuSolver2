class Field():
    def __init__(self):
        # x- and y coordinates and box number. All coordinates and box are numbered 0-8
        self.x = 0
        self.y = 0
        self.box = 0

        self.number = 0     # The number in the field. 0 is undetermined
        self.id = 0         # All field has an id from 0 to 80

        # A set of every number that might be placed in the field
        self.possible = {1,2,3,4,5,6,7,8,9} 