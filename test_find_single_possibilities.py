import unittest
import auxiliary_functions
import create_rows_columns_boxes as cr

import find_single_possibilities as fs

class TestFindSinglePossibilities(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.sudoku =   [[2, 0, 0, 0, 9, 0, 0, 5, 1],
                        [0, 0, 6, 8, 0, 5, 3, 0, 0],
                        [5, 0, 3, 0, 4, 0, 0, 0, 0],
                        [4, 7, 0, 0, 0, 8, 0, 0, 2],
                        [0, 0, 0, 9, 0, 0, 0, 3, 0],
                        [0, 6, 0, 0, 7, 0, 0, 4, 0],
                        [0, 9, 4, 7, 0, 6, 0, 0, 0],
                        [0, 5, 0, 0, 0, 0, 9, 0, 3],
                        [0, 0, 0, 2, 0, 9, 0, 0, 7]]

        # s id for solved
        cls.sudoku_s = [[2, 4, 7, 6, 9, 3, 8, 5, 1],
                        [9, 1, 6, 8, 2, 5, 3, 7, 4],
                        [5, 8, 3, 1, 4, 7, 6, 2, 9],
                        [4, 7, 1, 3, 6, 8, 5, 9, 2],
                        [8, 2, 5, 9, 1, 4, 7, 3, 6],
                        [3, 6, 9, 5, 7, 2, 1, 4, 8],
                        [1, 9, 4, 7, 3, 6, 2, 8, 5],
                        [7, 5, 2, 4, 8, 1, 9, 6, 3],
                        [6, 3, 8, 2, 5, 9, 4, 1, 7]]
        
    def setUp(self):
        """ Create rows, columns and boxes for each test """
        self.fields = auxiliary_functions.load_sudoku(self.sudoku)
        self.fields_s = auxiliary_functions.load_sudoku(self.sudoku_s)

        self.rows = cr.create_rows(self.fields)
        self.columns = cr.create_columns(self.fields)
        self.boxes = cr.create_boxes(self.fields)


    def test_find_singe_poss_rows(self):
        row_1 = self.rows[1]    # The second row has a "0" in the first field
        row_1[0].possible = {1,2,3,4,5,6,7,8,9} # "1" is only found once in the possibilities
        row_1[1].possible = {2,3,4,5,6,7,8,9}
        row_1[2].possible = {2,3,4,5,6,7,8,9}
        row_1[3].possible = {2,3,4,5,6,7,8,9}
        row_1[4].possible = {2,3,4,5,6,7,8,9}
        row_1[5].possible = {2,3,4,5,6,7,8,9}
        row_1[6].possible = {2,3,4,5,6,7,8,9}
        row_1[7].possible = {2,3,4,5,6,7,8,9}
        row_1[8].possible = {2,3,4,5,6,7,8,9}

        self.assertEqual(fs.find_single_possibilities(row_1[0], row_1), {1})
    

    def test_find_singe_poss_columns(self):
        column_1 = self.columns[3]    # The forth column has a "0" in the first field
        column_1[0].possible = {1,2,3,4,5,6,7,8,9}  # "1" is only found once in the possibilities
        column_1[1].possible = {2,3,4,5,6,7,8,9}
        column_1[2].possible = {2,3,4,5,6,7,8,9}
        column_1[3].possible = {2,3,4,5,6,7,8,9}
        column_1[4].possible = {2,3,4,5,6,7,8,9}
        column_1[5].possible = {2,3,4,5,6,7,8,9}
        column_1[6].possible = {2,3,4,5,6,7,8,9}
        column_1[7].possible = {2,3,4,5,6,7,8,9}
        column_1[8].possible = {2,3,4,5,6,7,8,9}

        self.assertEqual(fs.find_single_possibilities(column_1[0], column_1), {1})


    def test_find_singe_poss_boxes(self):
        box_1 = self.boxes[4]    # The fifth box has a "0" in the fifth field
        box_1[0].possible = {2,3,4,5,6,7,8,9}
        box_1[1].possible = {2,3,4,5,6,7,8,9}
        box_1[2].possible = {2,3,4,5,6,7,8,9}
        box_1[3].possible = {2,3,4,5,6,7,8,9}
        box_1[4].possible = {1,2,3,4,5,6,7,8,9}     # "1" is only found once in the possibilities
        box_1[5].possible = {2,3,4,5,6,7,8,9}
        box_1[6].possible = {2,3,4,5,6,7,8,9}
        box_1[7].possible = {2,3,4,5,6,7,8,9}
        box_1[8].possible = {2,3,4,5,6,7,8,9}

        self.assertEqual(fs.find_single_possibilities(box_1[4], box_1), {1})