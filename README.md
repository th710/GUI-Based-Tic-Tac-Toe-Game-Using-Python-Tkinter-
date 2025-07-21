# GUI-Based-Tic-Tac-Toe-Game-Using-Python-Tkinter-
SRM INSTITUTE OF SCIENCE AND TECHNOLOGY
Ramapuram, Chennai – 600089
FACULTY OF ENGINEERING AND TECHNOLOGY
Department of Electronics and Communication Engineering
Academic Year: 2025 – 2026

MINI PROJECT REPORT
Course Title: Python Programming
Course Code: 21CSO352T

TITLE: GUI-Based Tic Tac Toe Game Using Python Tkinter
Submitted by:
THARNISH R.N
RA2211004020088

Under the Guidance of:
Dr. R. ARTHI
Associate Professor (SIG)

Abstract
This project implements a two-player Tic Tac Toe game using Python’s tkinter library. The game features a graphical user interface (GUI) that allows two players to take turns marking spaces in a 3×3 grid. The system detects win conditions, handles draws, and includes a reset function. The goal is to demonstrate event-driven programming and Python GUI development through a simple multiplayer game.

1. Introduction
Tic Tac Toe is a classic game widely used in programming education to teach logic structures and conditional programming. By bringing this into a GUI-based environment with Python’s tkinter, the project enhances interactivity and reinforces:

GUI layout design

Event handling

Button control logic

Conditional and state-based programming

2. Problem Statement
Traditional implementations of Tic Tac Toe are text-based, limiting user interaction. This project aims to provide a visually engaging, user-friendly interface that enhances gameplay while also demonstrating GUI programming principles.

3. Proposed Solution
To solve the problem, the project implements a GUI-based Tic Tac Toe game with:

A 3×3 grid layout using Button widgets

Turn-based management for Player X and Player O

Win and draw detection after each move

A reset button to restart the game

A status label showing the current player’s turn

4. Block Diagram
(You may draw and insert the following logic as a diagram)

plaintext
Copy
Edit
Start Game → Player X Clicks Button → Check Win/Draw → Switch Turn  
     ↓                 ↓                              ↓  
  Reset Game ← Player O Clicks Button ← Check Win/Draw ← ...
5. Components Used
➤ Python 3.x
Main programming language used

Supports GUI, automation, and event-driven logic

Provides access to tkinter natively

➤ tkinter Library
Built-in Python GUI framework

Used for:

Window creation (Tk)

Buttons (Button)

Status display (Label)

Layouts (Frame)

Allows event-driven GUI development

➤ messagebox from tkinter
Displays pop-up messages such as:

"Player X wins!"

"It's a draw!"

Enhances feedback for the user

6. Explanation of Working
6.1 Game Interface Setup
A 3×3 grid using Button widgets

A Label for showing whose turn it is

A Reset Game button below the grid

6.2 Player Move Logic
On clicking a button:

Button updates with current player's symbol (X/O)

Switches to the next player

Status label updates

6.3 Win or Draw Check
After each move:

check_winner() function checks all 8 possible win lines:

Rows: [0,1,2], [3,4,5], [6,7,8]

Columns: [0,3,6], [1,4,7], [2,5,8]

Diagonals: [0,4,8], [2,4,6]

Displays a message if a player wins or if it’s a draw

Resets the board

6.4 Reset Functionality
Clears all cells

Resets current_player to "X"

Updates the status label

7. Event Handling Summary
Event	Action
Button Click	Marks cell, checks for win/draw
Win/Draw Detected	Shows popup, resets game
Reset Button Clicked	Clears the board and resets status

8. Benefits of This Approach
Feature	Description
Intuitive GUI	Visually appealing grid layout
Turn Handling	Automatically manages players’ turns
Win Detection	Accurately detects all possible win conditions
Draw Handling	Detects tied games automatically
Reset Option	Allows seamless replay without restarting the app

9. Source Code
python
Copy
Edit
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe - Multiplayer")
root.geometry("400x450")

current_player = "X"
buttons = []

def check_winner():
    combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in combos:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            winner = buttons[combo[0]]["text"]
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset()
            return
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset()

def on_click(i):
    global current_player
    if buttons[i]["text"] == "":
        buttons[i]["text"] = current_player
        check_winner()
        current_player = "O" if current_player == "X" else "X"
        status_label.config(text=f"Player {current_player}'s Turn")

def reset():
    global current_player
    for button in buttons:
        button["text"] = ""
    current_player = "X"
    status_label.config(text="Player X's Turn")

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    button = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2, command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

status_label = tk.Label(root, text="Player X's Turn", font=("Arial", 16))
status_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), command=reset)
reset_button.pack()

root.mainloop()
10. Output
A Tic Tac Toe game window appears

Two players can click alternately to play

Win or draw is detected and displayed

Reset button clears the grid

11. Conclusion
This mini-project demonstrates the creation of a functional GUI-based game using Python. It provides hands-on experience with:

Tkinter GUI development

Event handling

Game logic implementation

This project serves as an effective learning tool for students new to GUI development and event-driven programming.

12. References
Python Official Tkinter Documentation

GeeksforGeeks – Tic Tac Toe using Tkinter

TutorialsPoint – Python GUI

Real Python – Tkinter Guide

