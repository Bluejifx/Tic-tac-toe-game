from tkinter import *
from tkinter import messagebox
import random

def next_turn(row,column): # Initializes the next player's turn
    global player
    if buttons[row][column]['text'] == "" and check_winning() is False:

        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winning() is False:
                player = players[1]
                label.configure(text=players[1]+" turn")

            elif check_winning() is True:
                label.configure(text=players[0]+" wins")

            elif check_winning() == "Tie":
                label.configure(text="Tie!")

        else:
            buttons[row][column]['text'] = player

            if check_winning() is False:
                player = players[0]
                label.configure(text=players[0]+" turn")

            elif check_winning() is True:
                label.configure(text=players[1]+" wins")

            elif check_winning() == "Tie":
                label.configure(text="Tie!")



def check_winning(): # Checks if anyone has won

    # Checking the horizontal winning conditions
    for row in range(3):
        if buttons[row][0]['text'] ==  buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True
    for column in range(3):
        if buttons[0][column]['text'] ==  buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True

    elif buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        return True

    elif empty_spaces() is False:
        return "Tie"

    else:
        return False


def empty_spaces(): # Checks if there are an empty spaces
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game(): # Starts a new game

    global player
    player = random.choice(players)

    label.config(text=player+"'s turn")

    for row in range(3):
        for colum in range(3):
            buttons[row][colum].config(text="")



def quitting(): # Quits the game.
    asking = messagebox.askyesno("Quitting","Are you sure you want to exit the game?")
    if asking == True:
        window.destroy()
        quit()
    else:
        new_game()

window = Tk() # Creates the window
window.title("Tic-tac-toe") # Title
window.configure(bg='black')
players = ["X","O"] # Creates both players
player = random.choice(players) # Assigns a player
buttons = [[0,0,0], # Shows the buttons
           [0,0,0],
           [0,0,0]]


label = Label(text= player + "'s turn", font=('consolas',40)) # Creates text
label.pack(side= "top")

exit_button = Button(text="Exit", font=('consolas',20),command=quitting) # Creates the exit button
exit_button.pack(side= "bottom")

reset_button = Button(text="Restart", font=('consolas',20),command=new_game) # Creates the reset button
reset_button.pack(side= "bottom")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
     buttons[row][column] = Button(frame,text="",font=('consolas',20),width=10, height=4,
                                   command=lambda row=row, column=column: next_turn(row,column))
     buttons[row][column].grid(row=row,column=column)


mainloop()

