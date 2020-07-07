""" Input for the sudoku """

# 0 equals an empty square

""" Easy sudoku """
sudoku_e = [[0, 9, 8, 4, 5, 1, 0, 0, 2],
            [7, 2, 0, 0, 0, 0, 8, 0, 0],
            [0, 0, 3, 7, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 4, 2, 0, 0, 0],
            [0, 0, 0, 9, 0, 0, 0, 0, 4],
            [0, 0, 5, 0, 1, 7, 0, 0, 9],
            [2, 8, 0, 1, 0, 9, 4, 0, 0],
            [0, 0, 0, 3, 0, 0, 0, 0, 0],
            [0, 4, 0, 0, 8, 5, 0, 9, 7]]

""" Medium sudoku """
sudoku_m = [[2, 0, 0, 0, 9, 0, 0, 5, 1],
            [0, 0, 6, 8, 0, 5, 3, 0, 0],
            [5, 0, 3, 0, 4, 0, 0, 0, 0],
            [4, 7, 0, 0, 0, 8, 0, 0, 2],
            [0, 0, 0, 9, 0, 0, 0, 3, 0],
            [0, 6, 0, 0, 7, 0, 0, 4, 0],
            [0, 9, 4, 7, 0, 6, 0, 0, 0],
            [0, 5, 0, 0, 0, 0, 9, 0, 3],
            [0, 0, 0, 2, 0, 9, 0, 0, 7]]

""" Hard sudoku """
sudoku_h0 =[[0, 0, 0, 0, 0, 9, 3, 8, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 2],
            [6, 8, 0, 7, 0, 3, 0, 0, 0],
            [0, 0, 7, 0, 0, 0, 0, 2, 6],
            [8, 0, 1, 9, 0, 0, 0, 0, 0],
            [0, 9, 0, 0, 7, 0, 1, 0, 0],
            [0, 2, 0, 0, 3, 0, 8, 0, 1],
            [4, 7, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 3, 0]]
        
sudoku_h1 =[[9, 0, 0, 0, 0, 0, 0, 0, 8],
            [3, 0, 0, 0, 0, 4, 7, 2, 6],
            [0, 7, 0, 0, 0, 6, 0, 5, 3],
            [1, 0, 0, 0, 0, 0, 0, 3, 0],
            [0, 0, 0, 1, 0, 5, 0, 0, 4],
            [0, 9, 0, 0, 3, 0, 0, 0, 0],
            [0, 3, 0, 0, 0, 2, 0, 8, 0],
            [6, 0, 0, 4, 5, 0, 0, 0, 7],
            [5, 0, 0, 0, 0, 0, 0, 0, 0]]

""" Very hard sudokus """
sudoku_v0 =[[0, 0, 0, 0, 9, 0, 4, 0, 0],
            [0, 0, 0, 7, 3, 0, 0, 0, 0],
            [4, 0, 3, 0, 0, 0, 0, 2, 0],
            [0, 4, 0, 6, 0, 0, 8, 0, 0],
            [0, 7, 0, 8, 0, 0, 0, 9, 0],
            [5, 0, 0, 0, 4, 0, 6, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 0],
            [0, 1, 0, 0, 5, 7, 0, 0, 0],
            [0, 0, 2, 4, 0, 1, 0, 0, 6]]

sudoku_v1 =[[0, 0, 3, 0, 1, 0, 0, 0, 0],
            [0, 2, 0, 9, 0, 0, 6, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 6, 0, 0, 2, 0, 0, 9, 0],
            [8, 5, 0, 6, 0, 4, 0, 0, 0],
            [0, 0, 8, 0, 5, 0, 0, 0, 9],
            [0, 4, 2, 1, 0, 0, 0, 5, 0],
            [6, 0, 0, 0, 0, 7, 0, 0, 3]]

sudoku_v2 =[[0, 0, 0, 7, 0, 0, 3, 0, 9],
            [0, 0, 0, 0, 0, 0, 0, 8, 2],
            [0, 5, 7, 0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 0, 6],
            [3, 0, 0, 1, 0, 8, 0, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 0, 0, 0, 8],
            [8, 0, 9, 4, 1, 0, 6, 0, 5],
            [0, 7, 0, 0, 6, 0, 1, 0, 0]]

sudoku_v3 =[[0, 0, 0, 2, 0, 0, 4, 0, 3],
            [0, 0, 0, 0, 5, 3, 0, 0, 0],
            [7, 0, 0, 8, 0, 0, 0, 6, 0],
            [8, 1, 2, 0, 3, 0, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 7, 0, 0, 0, 0, 0],
            [0, 4, 3, 0, 0, 6, 0, 0, 0],
            [0, 6, 0, 0, 0, 5, 1, 4, 0]]


""" Empty sudoku """
sudoku_x = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]


""" Decide which one to use """
sudoku = sudoku_h1