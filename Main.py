import tkinter as tk
import tkinter.ttk as ttk

from Main_solver import solve_sudoku
from Sudokus import sudoku
from auxiliary_functions import print_two_sudokus, load_sudoku

class Launch:
    def __init__(self, master):

        self.window = master
        master.title("Sudoku Solver v2")
        self.window.geometry('500x500')

        self.sudoku = sudoku

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
                
                # The entry box are framed by a frame
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

                self._table[i][j].bind('<Motion>', self.correctGrid)

                self._table[i][j].pack(padx=5, pady=10)
       
        # Front-End Menu
        menu = tk.Menu(master)
        master.config(menu = menu)

        file = tk.Menu(menu)
        menu.add_cascade(label = 'Sudoku', menu = file)
        file.add_command(label = 'Exit', command = master.quit)
        file.add_command(label = 'Solve', command = self.solveInput)
        file.add_command(label = 'Clear', command = self.clearAll)

    
    def clearAll(self):
        pass
    

    def solveInput(self):
        solve_sudoku(self.sudoku)
        for i in range(9):
            for j in range(9):
                self._table[i][j].current(self.sudoku[i][j])

    

    # Correct the Grid if inputs are incorrect
    def correctGrid(self, event):
        for i in range(9):
            for j in range(9):
                if self._table[i][j].get() == '':
                    self.sudoku[i][j] = 0
                else:
                    self.sudoku[i][j] = int(self._table[i][j].get())

root = tk.Tk()
root.geometry('275x283')

app = Launch(root)
root.mainloop()