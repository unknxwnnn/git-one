import tkinter
from tkinter import StringVar, ACTIVE, NORMAL
import random

root = tkinter.Tk()
root.title('Simon Memory Game')
root.iconbitmap('simon.ico')
root.geometry('400x400')
root.resizable(0, 0)

game_font1 = ('Arial', 12)
game_font2 = ('Arial', 8)
white = "#c6cbcd"
white_light = "#fbfcfc"
magenta = "#90189e"
magenta_light = "#f802f9"
cyan = "#078384"
cyan_light = "#00fafa"
yellow = "#9ba00f"
yellow_light = "#f7f801"
root_color = "#2eb4c6"
game_color = "#f6f7f8"
root.config(bg=root_color)

time = 500
score = 0
game_sequence = []
player_sequence = []


def pick_sequence():
    """Pick the next value in sequence. Do not allow for repeated values."""
    while True:
        value = random.randint(1, 4)
        if len(game_sequence) == 0:
            game_sequence.append(value)
            break

        elif value != game_sequence[-1]:
            game_sequence.append(value)
            break

    play_sequence()


def play_sequence():
    """Play the entire sequence for a given round by animating buttons"""
    change_label("Playing!")

    delay = 0
    for value in game_sequence:
        if value == 1:
            root.after(delay, lambda: animate(white_button))
        elif value == 2:
            root.after(delay, lambda: animate(magenta_button))
        elif value == 3:
            root.after(delay, lambda: animate(cyan_button))
        elif value == 4:
            root.after(delay, lambda: animate(yellow_button))

        delay += time


def animate(button):
    """Animate a given button by changing its color"""
    button.config(state=ACTIVE)
    root.after(time, lambda: button.config(state=NORMAL))


def change_label(message):
    """Update the start button text to let the player know their status."""
    start_button.config(text=message)


def set_difficulty():
    """Use radio buttons to set difficulty. Difficulty affects time between button 'flashes'"""
    global time

    if difficulty.get() == 'Easy':
        time = 1000
    elif difficulty.get() == 'Medium':
        time = 500
    else:
        time = 200


def test():
    pick_sequence()
    print(game_sequence)


info_frame = tkinter.Frame(root, bg=root_color)
game_frame = tkinter.LabelFrame(root, bg=game_color)
info_frame.pack(pady=(10, 20))
game_frame.pack()

start_button = tkinter.Button(info_frame, text="New Game", font=game_font1, bg=game_color, command=test)
score_label = tkinter.Label(info_frame, text="Score: " + str(score), font=game_font1, bg=root_color)
start_button.grid(row=0, column=0, padx=20, ipadx=30)
score_label.grid(row=0, column=1)

white_button = tkinter.Button(game_frame, bg=white, activebackground=white_light, borderwidth=3)
magenta_button = tkinter.Button(game_frame, bg=magenta, activebackground=magenta_light, borderwidth=3)
cyan_button = tkinter.Button(game_frame, bg=cyan, activebackground=cyan_light, borderwidth=3)
yellow_button = tkinter.Button(game_frame, bg=yellow, activebackground=yellow_light, borderwidth=3)

white_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)
magenta_button.grid(row=0, column=2, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)
cyan_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)
yellow_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)

difficulty = StringVar()
difficulty.set('Medium')
tkinter.Label(game_frame, text="Difficulty:", font=game_font2, bg=game_color).grid(row=2, column=0)
tkinter.Radiobutton(game_frame, text="Easy", variable=difficulty, value="Easy", font=game_font2, bg=game_color, command = set_difficulty).grid(
    row=2, column=1)
tkinter.Radiobutton(game_frame, text="Medium", variable=difficulty, value="Medium", font=game_font2,
                    bg=game_color, command = set_difficulty).grid(row=2, column=2)
tkinter.Radiobutton(game_frame, text="Hard", variable=difficulty, value="Hard", font=game_font2, bg=game_color, command=set_difficulty()).grid(
    row=2, column=3)

root.mainloop()
