from random import randint
import tkinter as tk

# list of options
t = ["Rock", "Paper", "Scissors"]

window = tk.Tk()
window.title("R_P_S")
window.geometry("300x300")


Msg1 = tk.Label(text="Rock Paper Scissors")
Msg1.place(x=20,y=20)


def rock():
    computer = t[randint(0,2)]
    player = "Rock"
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose !", computer, "covers", player)
        else:
            print("You win !", player, "smashes", computer)


def paper():
    computer = t[randint(0,2)]
    player ="Paper"
    if player == computer:
        print("Tie!")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose !", computer, "cut", player)
        else:
            print("You win !", player, "covers", computer)


def scissors():
    computer = t[randint(0,2)]
    player = "Scissors"
    if player == computer:
        print("Tie!")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win !", player, "cut", computer)


b1= tk.Button(window,text='Rock',command=rock)
b1.place(x=20,y=50)
b2= tk.Button(window,text='Paper',command=paper)
b2.place(x=20,y=80)
b3= tk.Button(window,text='Scissors',command=scissors)
b3.place(x=20,y=110)


window.mainloop()