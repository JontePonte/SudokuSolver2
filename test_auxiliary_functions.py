import unittest
import auxiliary_functions

class TestAuxiliary_functions(unittest.TestCase):

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
    

if __name__ == '__main__':
    unittest.main()
