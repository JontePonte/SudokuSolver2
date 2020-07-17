import tkinter as tk
import tkinter.ttk as ttk

from Main_solver import solve_sudoku
from Sudokus import sudoku
from auxiliary_functions import print_two_sudokus, load_sudoku

sudoku_old = sudoku
first_iteration = True

# Create an event handler
def correctGrid(num):
    if num == '':
        sudoku[i][j]
    else:
        sudoku[i][j] = int(num)    


# Create a window object
window = tk.Tk()
window.geometry('500x500')

for i in range(0,9):
    # Make the window scalable
    window.columnconfigure(i, weight=1, minsize=50)
    window.rowconfigure(i, weight=1, minsize=50)
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
            master=window,
            bg=color,
            padx=5,
            pady=5
        )
        frame.grid(
            row=i,
            column=j
        )

        # Combobox create a dropdown menu
        box_ent = ttk.Combobox(master=frame)
        box_ent["values"] = ("",1,2,3,4,5,6,7,8,9)

        if first_iteration:
            box_ent.current(sudoku[i][j])
            num = box_ent.get()
            box_ent.bind(correctGrid)

        num = box_ent.get()
        box_ent.bind('<Motion>', correctGrid)

        box_ent.pack(padx=5, pady=10)

first_iteration = False

# Run the event loop
window.mainloop()

fields = load_sudoku(sudoku)
fields_old = load_sudoku(sudoku_old)

print_two_sudokus(fields_old, fields)