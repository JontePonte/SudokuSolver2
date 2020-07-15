import tkinter as tk
import tkinter.ttk as ttk

from Main_solver import solve_sudoku
from Sudokus import sudoku

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
        box_ent.pack(padx=5, pady=10)


# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

# Run the event loop
window.mainloop()