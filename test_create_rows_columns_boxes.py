import unittest
import auxiliary_functions
import create_rows_columns_boxes as cr


class TestCreateRowsColumnsBoxes(unittest.TestCase):
    
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
        
        cls.fields = auxiliary_functions.load_sudoku(cls.sudoku)
        cls.fields_s = auxiliary_functions.load_sudoku(cls.sudoku_s)
    

    def test_create_rows(self):
        rows = cr.create_rows(self.fields)
        rows_s = cr.create_rows(self.fields_s)
        
        self.assertEqual(rows[0][0].id, 0)
        self.assertEqual(rows[3][8].number, 2)
        self.assertEqual(len(rows[6]), 9)
        self.assertEqual(len(rows), 9)

        self.assertEqual(rows_s[2][4].number, 4)


    def test_create_columns(self):
        columns = cr.create_columns(self.fields)
        columns_s = cr.create_columns(self.fields_s)
        
        self.assertEqual(columns[3][0].id, 3)
        self.assertEqual(columns[3][6].number, 7)
        self.assertEqual(len(columns[6]), 9)
        self.assertEqual(len(columns), 9)

        self.assertEqual(columns_s[2][4].number, 5)


    def test_create_boxes(self):
        boxes = cr.create_boxes(self.fields)
        boxes_s = cr.create_boxes(self.fields_s)
        
        self.assertEqual(boxes[1][0].id, 3)
        self.assertEqual(boxes[2][2].id, 8)
        self.assertEqual(boxes[3][7].number, 6)
        self.assertEqual(len(boxes[6]), 9)
        self.assertEqual(len(boxes), 9)

        self.assertEqual(boxes_s[5][1].number, 9)
