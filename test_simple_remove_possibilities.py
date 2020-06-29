import unittest
import auxiliary_functions
import create_rows_columns_boxes as cr

import simple_remove_possibilities as sr

class TestSimpleRemovePossibilities(unittest.TestCase):
    
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

        
        cls.fields = auxiliary_functions.load_sudoku(cls.sudoku)

        # Create rows, column and boxes for the testing
        cls.rows = cr.create_rows(cls.fields)
        cls.columns = cr.create_columns(cls.fields)
        cls.boxes = cr.create_boxes(cls.fields)
    
    
    def test_simple_remove_row(self):
        self.assertEqual(sr.simple_remove_possibilities_row(self.fields[0], self.rows[0]), {2})
        self.assertEqual(sr.simple_remove_possibilities_row(self.fields[9], self.rows[1]), {1,2,4,7,9})
        self.assertEqual(sr.simple_remove_possibilities_row(self.fields[78], self.rows[8]), {1,3,4,5,6,8})
    

    def test_simple_remove_column(self):
        self.assertEqual(sr.simple_remove_possibilities_column(self.columns[1][3], self.columns[1]), {7})
        self.assertEqual(sr.simple_remove_possibilities_column(self.fields[6], self.columns[6]), {1,2,4,5,6,7,8})
        self.assertEqual(sr.simple_remove_possibilities_column(self.fields[76], self.columns[4]), {1,2,3,5,6,8})
    
    
    def test_simple_remove_box(self):
        self.assertEqual(sr.simple_remove_possibilities_boxes(self.boxes[3][0], self.boxes[3]), {4})
        self.assertEqual(sr.simple_remove_possibilities_boxes(self.fields[1], self.boxes[0]), {1,4,7,8,9})
        self.assertEqual(sr.simple_remove_possibilities_boxes(self.fields[79], self.boxes[8]), {1,2,4,5,6,8})