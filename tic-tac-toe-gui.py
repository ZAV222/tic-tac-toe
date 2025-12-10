# Importing essential libraries
import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")       
window.geometry("300x300")         

# Track the current player
current_player = "X"

# Function to handle button click
def button_click(btn):
    global current_player
    if btn["text"] == "_":  
        btn["text"] = current_player
        if not check_winner():   # Check for winner; returns True if someone wins
            if all(b["text"] != "_" for b in buttons):  # Check for draw
                messagebox.showinfo("Game Over", "It's a Draw!")
                window.quit()
            else:
                # Switch player
                current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showinfo("Invalid Move", "This cell is already taken")

# Create 9 buttons for the grid
b1 = tk.Button(window, text="_", width=6, height=3, command=lambda: button_click(b1))
b2 = tk.Button(window, text="_", width=6, height=3, command=lambda: button_click(b2))
b3 = tk.Button(window, text="_", width=6, height=3, command=lambda: button_click(b3))
b4 = tk.Button(window, text="_", width=6, height=3, command=lambda: button_click(b4))
b5 = tk.Button(window, text="_", width=6, height=3, command=lambda: button_click(b5))
b6 = tk.Button(window, text="_", width=6, height=3, command=lambda: button_click(b6))
b7 = tk.Button(window, text="_", width=6, height=3, command=lambda: button_click(b7))
b8 = tk.Button(window, text="_", width=6, height=3, command=lambda: button_click(b8))
b9 = tk.Button(window, text="_", width=6, height=3, command=lambda: button_click(b9))

buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]  # List of all buttons

# Place buttons in a 3x3 grid and make them expandable
b1.grid(row=0, column=0, sticky="nsew")
b2.grid(row=0, column=1, sticky="nsew")
b3.grid(row=0, column=2, sticky="nsew")
b4.grid(row=1, column=0, sticky="nsew")
b5.grid(row=1, column=1, sticky="nsew")
b6.grid(row=1, column=2, sticky="nsew")
b7.grid(row=2, column=0, sticky="nsew")
b8.grid(row=2, column=1, sticky="nsew")
b9.grid(row=2, column=2, sticky="nsew")

for i in range(3):
    window.rowconfigure(i, weight=1)
    window.columnconfigure(i, weight=1)

# Function to check if any player has won
def check_winner():
    wins = [
        [b1, b2, b3], [b4, b5, b6], [b7, b8, b9],  # rows
        [b1, b4, b7], [b2, b5, b8], [b3, b6, b9],  # columns
        [b1, b5, b9], [b3, b5, b7]                 # diagonals
    ]
    
    for combo in wins:
        if combo[0]["text"] == combo[1]["text"] == combo[2]["text"] != "_":
            messagebox.showinfo("Game Over", f"{combo[0]['text']} wins!")
            window.quit()
            return True
    return False  # No winner yet

window.mainloop()
