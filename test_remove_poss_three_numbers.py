import unittest
import auxiliary_functions
import create_rows_columns_boxes as cr

import remove_poss_three_numbers as rem_poss

class TestRemovePossSetThree(unittest.TestCase):
    
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


    def tearDown(self):
        self.fields = []
        self.fields_s = []

        self.rows = []
        self.columns = []
        self.boxes = []


    def test_remove_poss_just_three_row(self):
        row_1 = self.rows[4]    # The fifth row has a "0" in the first field and only two set numbers
        # fifth row: [0, 0, 0, 9, 0, 0, 0, 3, 0]
        
        # All possible needs to be set manualy for this test
        row_1[0].possible = {1,2,4,5,6,7,8}
        row_1[1].possible = {4,5,6}
        row_1[2].possible = {1,2,4,5,6,7,8}
        row_1[3].possible = {9}
        row_1[4].possible = {1,2,4,5,6,7,8}
        row_1[5].possible = {4,5,6}
        row_1[6].possible = {1,2,4,5,6,7,8}
        row_1[7].possible = {3}
        row_1[8].possible = {4,5,6}

        row_1_result = rem_poss.remove_poss_just_three(row_1)

        # 4, 5, 6 should be removed from every field exept 1, 5 and 8 becasue 4,5,6 have to be in 1,5,8
        # all other possibilities should stay the same
        self.assertEqual(row_1_result[0].possible, {1,2,7,8})
        self.assertEqual(row_1_result[1].possible, {4,5,6})        
        self.assertEqual(row_1_result[2].possible, {1,2,7,8})  
        self.assertEqual(row_1_result[3].possible, {9})  
        self.assertEqual(row_1_result[4].possible, {1,2,7,8})    
        self.assertEqual(row_1_result[5].possible, {4,5,6})  
        self.assertEqual(row_1_result[6].possible, {1,2,7,8})  
        self.assertEqual(row_1_result[7].possible, {3})  
        self.assertEqual(row_1_result[8].possible, {4,5,6})


    def test_remove_poss_just_three_row_NOCHANGE(self):
        row_1 = self.rows[4]    # The fifth row has a "0" in the first field and only two set numbers
        # fifth row: [0, 0, 0, 9, 0, 0, 0, 3, 0]
        
        # All possible needs to be set manualy for this test
        row_1[0].possible = {1,2,4,5,6,7,8}
        row_1[1].possible = {4,5,6}
        row_1[2].possible = {1,2,4,5,6,7,8}
        row_1[3].possible = {9}
        row_1[4].possible = {1,2,4,5,6,7,8}
        row_1[5].possible = {4,5,6,7}
        row_1[6].possible = {1,2,4,5,6,7,8}
        row_1[7].possible = {3}
        row_1[8].possible = {4,5,6}

        row_1_result = rem_poss.remove_poss_just_three(row_1)

        # No changes should be done because no set of tree numbers appears by them selves in three fields
        self.assertEqual(row_1_result[0].possible, {1,2,4,5,6,7,8})
        self.assertEqual(row_1_result[1].possible, {4,5,6})        
        self.assertEqual(row_1_result[2].possible, {1,2,4,5,6,7,8})  
        self.assertEqual(row_1_result[3].possible, {9})  
        self.assertEqual(row_1_result[4].possible, {1,2,4,5,6,7,8})    
        self.assertEqual(row_1_result[5].possible, {4,5,6,7})  
        self.assertEqual(row_1_result[6].possible, {1,2,4,5,6,7,8})  
        self.assertEqual(row_1_result[7].possible, {3})  
        self.assertEqual(row_1_result[8].possible, {4,5,6})


    def test_remove_extra_poss3_field_REMOVE(self):
        row_1 = self.rows[1]    # The second row has a "0" in the first field
        # second row: [0, 0, 6, 8, 0, 5, 3, 0, 0]
        
        # All possible needs to be set manualy for this test
        row_1[0].possible = {1,2,4,7,9}
        row_1[1].possible = {1,5,7,9}
        row_1[2].possible = {6}
        row_1[3].possible = {8}
        row_1[4].possible = {1,7}
        row_1[5].possible = {5}
        row_1[6].possible = {3}
        row_1[7].possible = {2,4}
        row_1[8].possible = {5,7,9}

        row_1[0].possible = rem_poss.remove_extra_poss3_field(row_1[0], row_1)

        # All possibilities exept 2 and 4 should be removed becase they only appears in the field[0] and field[7]
        self.assertEqual(row_1[0].possible, {2,4})


    def test_remove_extra_poss3_field_DONT(self):
        row_1 = self.rows[1]    # The second row has a "0" in the first field
        # second row: [0, 0, 6, 8, 0, 5, 3, 0, 0]
        
        # All possible needs to be set manualy for this test
        row_1[0].possible = {1,2,4,7,9}
        row_1[1].possible = {1,5,7,9}
        row_1[2].possible = {6}
        row_1[3].possible = {8}
        row_1[4].possible = {1,2,7}     # 2 i a possibility in the fifth row
        row_1[5].possible = {5}
        row_1[6].possible = {3}
        row_1[7].possible = {2,4}
        row_1[8].possible = {5,7,9}

        row_1[0].possible = rem_poss.remove_extra_poss3_field(row_1[0], row_1)

        # No possibilities should be removed for this one because 2 appears in three fields
        self.assertEqual(row_1[0].possible, {1,2,4,7,9})
