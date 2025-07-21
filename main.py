import tkinter as tk 
from tkinter import messagebox 
 
# Initial setup 
root = tk.Tk() 
root.title("Tic Tac Toe - Multiplayer") 
root.geometry("400x450") 
 
current_player = "X" 
buttons = [] 
 
# Function to check for win or draw 
def check_winner(): 
    combos = [ 
        [0,1,2], [3,4,5], [6,7,8],  # Rows 
        [0,3,6], [1,4,7], [2,5,8],  # Columns 
        [0,4,8], [2,4,6]            # Diagonals 
    ] 
    for combo in combos: 
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == 
buttons[combo[2]]["text"] != "": 
            winner = buttons[combo[0]]["text"] 
            messagebox.showinfo("Game Over", f"Player {winner} wins!") 
            reset() 
            return 
    if all(button["text"] != "" for button in buttons): 
        messagebox.showinfo("Game Over", "It's a draw!") 
        reset() 
 
# Function to handle player move 
def on_click(i): 
    global current_player 
    if buttons[i]["text"] == "": 
        buttons[i]["text"] = current_player 
        check_winner() 
        current_player = "O" if current_player == "X" else "X" 
        status_label.config(text=f"Player {current_player}'s Turn") 
 
# Function to reset the board 
def reset(): 
    global current_player 
    for button in buttons: 
        button["text"] = "" 
    current_player = "X" 
    status_label.config(text="Player X's Turn") 
 
# UI layout 
frame = tk.Frame(root) 
frame.pack() 
 
for i in range(9): 
    button = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2, 
command=lambda i=i: on_click(i)) 
    button.grid(row=i//3, column=i%3) 
    buttons.append(button) 
 
status_label = tk.Label(root, text="Player X's Turn", font=("Arial", 16)) 
status_label.pack(pady=10) 
 
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), 
command=reset) 
reset_button.pack() 
# Run the game 
root.mainloop()
