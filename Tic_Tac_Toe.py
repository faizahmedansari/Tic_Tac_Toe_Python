import tkinter as tk
from tkinter import messagebox

# -------------------------
# Main Window
# -------------------------
root = tk.Tk()
root.title("🎮 Tic Tac Toe")
root.geometry("420x500")
root.config(bg="#1E1E2E")
root.resizable(False, False)

player = "X"
board = [""] * 9

title = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 24, "bold"),
    bg="#1E1E2E",
    fg="#FFD700"
)
title.pack(pady=15)

status = tk.Label(
    root,
    text="Player X Turn",
    font=("Arial", 15, "bold"),
    bg="#1E1E2E",
    fg="white"
)
status.pack()

frame = tk.Frame(root, bg="#1E1E2E")
frame.pack(pady=20)

buttons = []

# -------------------------
# Functions
# -------------------------
def check_winner():
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "":
            buttons[a]["bg"] = "#00FF7F"
            buttons[b]["bg"] = "#00FF7F"
            buttons[c]["bg"] = "#00FF7F"

            messagebox.showinfo("Winner", f"🎉 Player {board[a]} Wins!")
            reset_game()
            return

    if "" not in board:
        messagebox.showinfo("Draw", "🤝 Match Draw!")
        reset_game()

def click(index):
    global player

    if board[index] == "":
        board[index] = player

        color = "#00BFFF" if player == "X" else "#FF69B4"

        buttons[index].config(text=player, fg=color)

        player = "O" if player == "X" else "X"
        status.config(text=f"Player {player} Turn")

        check_winner()

def reset_game():
    global player
    player = "X"

    status.config(text="Player X Turn")

    for i in range(9):
        board[i] = ""
        buttons[i].config(text="", bg="#2D2D44")

# -------------------------
# Board
# -------------------------
for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Arial", 28, "bold"),
        width=5,
        height=2,
        bg="#2D2D44",
        fg="white",
        activebackground="#505070",
        command=lambda i=i: click(i)
    )

    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# -------------------------
# Restart Button
# -------------------------
restart = tk.Button(
    root,
    text="🔄 Restart Game",
    font=("Arial", 14, "bold"),
    bg="#FF9800",
    fg="white",
    padx=15,
    pady=8,
    command=reset_game
)
restart.pack(pady=20)

root.mainloop()