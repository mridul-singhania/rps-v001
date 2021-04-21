from tkinter import *
import random


root = Tk()
root.title("Rock Paper Scissors")
root.configure(bg="snow")
root.resizable(False, False)
root.iconbitmap(r"gallery/File_Icon.ico")


ro = PhotoImage(file="gallery/Rock.png")
pa = PhotoImage(file="gallery/Paper.png")
sc = PhotoImage(file="gallery/Scissors.png")
vs = PhotoImage(file="gallery/VS.png")


won = "Player Won!"
lost = "Computer Won!"
tie = "It's a Tie!"

plChoice = StringVar()
comChoice = StringVar()
comPoints = IntVar()
plPoints = IntVar()
result = StringVar()

options = ["Rock", "Paper", "Scissors"]


def rock():
    plChoice_lbl["image"] = ro
    choice = random.choice(options)
    comChoice.set(choice)
    if choice == "Rock":
        comChoice_lbl["image"] = ro
        result.set(tie)
    elif choice == "Paper":
        result.set(lost)
        comPoints.set(comPoints.get()+1)
        comChoice_lbl["image"] = pa
    else:
        result.set(won)
        comChoice_lbl["image"] = sc
        plPoints.set(plPoints.get() + 1)


def paper():
    plChoice_lbl["image"] = pa
    choice = random.choice(options)
    comChoice.set(choice)
    if choice == "Rock":
        comChoice_lbl["image"] = ro
        plPoints.set(plPoints.get() + 1)
        result.set(won)
    elif choice == "Paper":
        result.set(tie)
        comChoice_lbl["image"] = pa
    else:
        result.set(lost)
        comChoice_lbl["image"] = sc
        comPoints.set(comPoints.get() + 1)


def scissors():
    plChoice_lbl["image"] = sc
    choice = random.choice(options)
    comChoice.set(choice)
    if choice == "Rock":
        comChoice_lbl["image"] = ro
        comPoints.set(comPoints.get() + 1)
        result.set(lost)
    elif choice == "Paper":
        comChoice_lbl["image"] = pa
        result.set(won)
        plPoints.set(plPoints.get() + 1)
    else:
        result.set(tie)
        comChoice.set(sc)


player_points_lbl = Label(root, text="Player Points", font="Arial 10 bold", fg="black", bg="snow")
player_points_lbl.grid(row=0, column=0)
emt_lbl = Label(
    root, text="<--------------------------------------------->", font="Arial 10 bold", bg="snow", fg="snow"
)
emt_lbl.grid(row=0, column=1)
computer_points_lbl = Label(root, text="Computer Points", font="Arial 10 bold", fg="black", bg="snow")
computer_points_lbl.grid(row=0, column=2)
player_points = Label(root, textvariable=plPoints, font="Arial 12 bold", bg="black", fg="snow")
player_points.grid(row=1, column=0)
computer_points = Label(root, textvariable=comPoints, font="Arial 12 bold", bg="black", fg="snow")
computer_points.grid(row=1, column=2)

PlayerOptions = Label(root, text="Player Options", font="Arial 15 bold", bg="snow", fg="black")
PlayerOptions.grid(row=2, column=1)


rock_btn = Button(root, image=ro, bg="snow", fg="black", command=rock, cursor="hand2", bd=0)
rock_btn.grid(row=3, column=0, padx=10, pady=10)
paper_btn = Button(root, image=pa, bg="snow", fg="black", command=paper, cursor="hand2", bd=0)
paper_btn.grid(row=3, column=1, padx=10, pady=10)
scissors_btn = Button(root, image=sc, bg="snow", fg="black", command=scissors, cursor="hand2", bd=0)
scissors_btn.grid(row=3, column=2, padx=10, pady=10)


rock_txt = Label(root, text="Rock", font="Arial 10 bold", bg="snow", fg="black")
paper_txt = Label(root, text="Paper", font="Arial 10 bold", bg="snow", fg="black")
scissors_txt = Label(root, text="Scissors", font="Arial 10 bold", bg="snow", fg="black")
rock_txt.grid(row=4, column=0)
paper_txt.grid(row=4, column=1)
scissors_txt.grid(row=4, column=2)


plChoice_txt_lbl = Label(root, text="Player Choice", bg="snow", fg="black", font="Arial 15 bold")
plChoice_txt_lbl.grid(row=5, column=0, pady=10)
comChoice_txt_lbl = Label(root, text="Computer Choice", font="Arial 15 bold", bg="snow", fg="black")
comChoice_txt_lbl.grid(row=5, column=2, pady=10)
plChoice_lbl = Label(root, font="Arial 13 bold", fg="black", bg="snow")
plChoice_lbl.grid(row=6, column=0)
comChoice_lbl = Label(root, font="Arial 13 bold", fg="black", bg="snow")
comChoice_lbl.grid(row=6, column=2)
VS_lbl = Label(root, image=vs, bg="snow")
VS_lbl.grid(row=6, column=1)


result_lbl = Label(root, textvariable=result, font="Arial 13 bold", bg="snow", fg="black")
result_lbl.grid(row=7, column=1)


mainloop()
