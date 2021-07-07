from random import randint
import tkinter as tk

# list of options
t = ["Rock", "Paper", "Scissors"]

window = tk.Tk()
window.title("RPS")
window.geometry("300x300")


Msg1 = tk.Label(text="Rock Paper Scissors")
Msg1.place(x=20,y=20)


def rock():
    computer = t[randint(0,2)]
    player = "Rock"

    if player == computer:

        l1=tk.Label(text="Tie !!")
        l1.place(x=80,y=150)

    elif player == "Rock":

        if computer == "Paper":
            l2=tk.Label(text="Lost !")
            l2.place(x=80,y=150)

        else:
             l3=tk.Label(text="Won !")
             l3.place(x=80,y=150)
             


def paper():
    computer = t[randint(0,2)]
    player ="Paper"

    if player == computer:

        l4=tk.Label(text="Tie !!")
        l4.place(x=80,y=150)

    elif player == "Paper":

        if computer == "Scissors":
            l5=tk.Label(text="Lost !")
            l5.place(x=80,y=150)

        else:
             l6=tk.Label(text="Won !")
             l6.place(x=80,y=150)


def scissors():
    computer = t[randint(0,2)]
    player = "Scissors"

    if player == computer:

        l7=tk.Label(text="Tie !!!")
        l7.place(x=80,y=150)

    elif player == "Scissors":

        if computer == "Rock":
            l8=tk.Label(text="Lost !")
            l8.place(x=80,y=150)

        else:
             l9=tk.Label(text="Won !")
             l9.place(x=80,y=150)


b1= tk.Button(window,text='Rock',command=rock)
b1.place(x=20,y=50)
b2= tk.Button(window,text='Paper',command=paper)
b2.place(x=20,y=80)
b3= tk.Button(window,text='Scissors',command=scissors)
b3.place(x=20,y=110)


window.mainloop()
