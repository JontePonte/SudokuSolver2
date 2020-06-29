import unittest
import auxiliary_functions

class TestAuxiliaryFunctions(unittest.TestCase):

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


    def test_set_box_number(self):
        self.assertEqual(auxiliary_functions.set_box_number(0,0), 0)
        self.assertEqual(auxiliary_functions.set_box_number(8,0), 2)
        self.assertEqual(auxiliary_functions.set_box_number(0,8), 6)
        self.assertEqual(auxiliary_functions.set_box_number(4,7), 7)
        self.assertEqual(auxiliary_functions.set_box_number(7,7), 8)
        self.assertEqual(auxiliary_functions.set_box_number(6,6), 8)

        with self.assertRaises(ValueError):
            auxiliary_functions.set_box_number("a", "b")
        with self.assertRaises(ValueError):
            auxiliary_functions.set_box_number(3.5, 4)
    

    def test_load_sudoku(self):
        fields_t = auxiliary_functions.load_sudoku(self.sudoku)

        self.assertEqual(fields_t[0].x, 0)
        self.assertEqual(fields_t[7].x, 7)
        self.assertEqual(fields_t[80].x, 8)

        self.assertEqual(fields_t[0].y, 0)
        self.assertEqual(fields_t[8].y, 0)
        self.assertEqual(fields_t[79].y, 8)

        self.assertEqual(fields_t[77].number, 9)
        self.assertEqual(fields_t[14].number, 5)
        self.assertEqual(fields_t[28].number, 7)


    def test_check_field_possible_number(self):
        self.assertEqual(auxiliary_functions.check_field_possible_number(self.fields[0]), 2)
        self.assertEqual(auxiliary_functions.check_field_possible_number(self.fields[1]), 0)


    def test_is_solved(self):
        self.assertEqual(auxiliary_functions.is_solved(self.fields), False)
        self.assertEqual(auxiliary_functions.is_solved(self.fields_s), True)


if __name__ == '__main__':
    unittest.main()
