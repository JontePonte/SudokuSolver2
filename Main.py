""" Main file for SudokuSolver2"""

from Sudokus import sudoku          # The sudoku is chosen in the Sudokus file
from FieldClass import Field
from axiliary_functions import load_sudoku
from axiliary_functions import print_sudoku


fields = load_sudoku(sudoku)
print_sudoku(fields)