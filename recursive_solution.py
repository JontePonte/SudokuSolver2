
class RecursivSolv:
    """ Recursiv solving method """
    
    def __init__(self, fields):
        self.counter = 0

        # Create list in lists with all field numbers
        self.sudoku_num = []
        row = []
        for field in fields:
            row.append(field.number)
            if field.x == 8:
                self.sudoku_num.append(row)
                row = []
        
        # Run solution algoritm
        self.startSolution()
        

    def startSolution(self, i=0, j=0):
        i,j = self.findNextCellToFill(i, j)

        # If i == -1 the position is Ok or the Sudoku is Solved
        if i == -1:
            return True
        for e in range(1,10):
            if self.isValid(i,j,e):
                self.sudoku_num[i][j] = e
                if self.startSolution(i, j):
                    return True
                # Undo the current cell for backtracking
                self.sudoku_num[i][j] = 0
        return False
    

    # Search the Nearest Cell to fill
    def findNextCellToFill(self, i, j):

        self.counter += 1
        for x in range(i,9):
            for y in range(j,9):
                if self.sudoku_num[x][y] == 0:
                    return x,y

        for x in range(0,9):
            for y in range(0,9):
                if self.sudoku_num[x][y] == 0:
                    return x,y

        return -1,-1


    # Check the Validity of savedNumbers[i][j]
    def isValid(self, i, j, e):
        
        for x in range(9):
            if self.sudoku_num[i][x] == e:
                return False

        for x in range(9):
            if self.sudoku_num[x][j] == e:
                return False

        # Finding the Top x,y Co-ordinates of the section containing the i,j cell    
        secTopX, secTopY = 3 *int((i/3)), 3 *int((j/3))
        for x in range(secTopX, secTopX+3):
            for y in range(secTopY, secTopY+3):
                if self.sudoku_num[x][y] == e:
                    return False
        
        return True