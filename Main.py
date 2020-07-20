import tkinter as tk
import tkinter.ttk as ttk

from Main_solver import solve_sudoku
from Sudokus import sudoku
from auxiliary_functions import print_two_sudokus, load_sudoku, unpack_sudoku

class Launch:
    def __init__(self, master):

        # Create main window
        self.window = master
        master.title("Sudoku Solver v2")
        self.window.geometry('500x500')

        self.sudoku = sudoku

        # Create frontend table
        self._table = []
        for i in range(1,10):
            self._table += [[0,0,0,0,0,0,0,0,0]]

        for i in range(0,9):
            # Make the window scalable
            self.window.columnconfigure(i, weight=1, minsize=50)
            self.window.rowconfigure(i, weight=1, minsize=50)
            for j in range(0,9):
                
                # Create a 3x3 color grid
                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'gray80'
                elif i in [3,4,5] and j in [3,4,5]:
                    color = 'gray80'
                else:
                    color = 'white'
                
                # The combobox are framed by a frame
                frame = tk.Frame(
                    master=self.window,
                    bg=color,
                    padx=5,
                    pady=5
                )
                frame.grid(
                    row=i,
                    column=j
                )

                # Combobox create a dropdown menu
                self._table[i][j] = ttk.Combobox(master=frame)
                self._table[i][j]["values"] = ("",1,2,3,4,5,6,7,8,9)
                self._table[i][j].current(self.sudoku[i][j])

                # Update values all the time
                self._table[i][j].bind('<Motion>', self.setGrid)
                self._table[i][j].bind('<FocusIn>', self.setGrid)
                self._table[i][j].bind('<Button-1>', self.setGrid)

                self._table[i][j].pack(padx=5, pady=10)
       
        # Frontend Menu
        menu = tk.Menu(master)
        master.config(menu = menu)

        file = tk.Menu(menu)
        menu.add_cascade(label = 'Sudoku', menu = file)
        file.add_command(label = 'Exit', command = master.quit)
        file.add_command(label = 'Solve', command = self.solveInput)
        file.add_command(label = 'Clear', command = self.clearAll)

    
    # Set all tabe values (and sudoku values) to 0
    def clearAll(self):
        for i in range(9):
            for j in range(9):
                self._table[i][j].set('')


    # Call main solver and update 
    def solveInput(self):
        # The solver outputs a matrix of field-objects and they needs to be unpacked
        solved_fields = solve_sudoku(self.sudoku)
        solved_sudoku = unpack_sudoku(solved_fields)

        # Update all values
        for i in range(9):
            for j in range(9):
                self._table[i][j].set(solved_sudoku[i][j])
    

    # Store grid input in sudoku matrix
    def setGrid(self, event):
        for i in range(9):
            for j in range(9):
                if self._table[i][j].get() == '':
                    self.sudoku[i][j] = 0
                else:
                    self.sudoku[i][j] = int(self._table[i][j].get())


# Create tk object
root = tk.Tk()
root.geometry('275x283')

# Create main object and runt tkinter-loop
app = Launch(root)
root.mainloop()