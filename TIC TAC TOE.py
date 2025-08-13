from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player
        buttons[row][column]['fg'] = "#222222"

        result = check_winner()
        if result is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=player + " turn")
        elif result is True:
            label.config(text=player + " wins!")
        elif result == "Tie":
            label.config(text="It's a Tie!")


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            for i in range(3):
                buttons[row][i].config(bg="#88e188")
            return True

    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            for i in range(3):
                buttons[i][col].config(bg="#88e188")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        for i in range(3):
            buttons[i][i].config(bg="#88e188")
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#88e188")
        buttons[1][1].config(bg="#88e188")
        buttons[2][0].config(bg="#88e188")
        return True

    if not empty_spaces():
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="#ffdf7f")
        return "Tie"

    return False


def empty_spaces():
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return True
    return False


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#f0f0f0", fg="#222222")



window = Tk()
window.title("Tic-Tac-Toe")
window.configure(bg="#f8f8f8")
window.resizable(False, False)

players = ["X", "O"]
player = random.choice(players)

label = Label(window, text=player + " turn", font=("Helvetica", 32, "bold"), fg="#333", bg="#f8f8f8")
label.pack(pady=20)

frame = Frame(window, bg="#f8f8f8")
frame.pack()

buttons = [[0, 0, 0] for _ in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=("Helvetica", 36, "bold"), width=5, height=2,
                                   bg="#f0f0f0", fg="#222222",
                                   activebackground="#ddd",
                                   command=lambda row=row, col=col: next_turn(row, col))

        buttons[row][col].grid(row=row, column=col, padx=5, pady=5)

reset_button = Button(window, text="Play Again", font=("Helvetica", 20), bg="#4CAF50", fg="white",
                      activebackground="#45a049", padx=20, pady=10, command=new_game)
reset_button.pack(pady=20)

window.mainloop()