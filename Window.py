from tkinter import *


class Window:
    buttonCreateShips = None
    buttonClearShips = None

    def __init__(self, master):
        self.master = master
        message1 = StringVar(value="")
        message2 = StringVar(value="")
        message3 = StringVar(value="")
        message4 = StringVar(value="")
        message5 = StringVar(value="")
        message6 = StringVar(value="")
        message7 = StringVar(value="")
        # Start process
        self.init_messages()
        self.init_buttons()

    def init_messages(self):
        Label(self.master.root, textvariable=self.message1, fg="blue", font=("Helvetica", 16)).grid(row=0, column=20)
        Label(self.master.root, textvariable=self.message2).grid(row=2, column=20)
        Label(self.master.root, textvariable=self.message3, fg="blue", font=("Helvetica", 12)).grid(row=3, column=20)
        Label(self.master.root, textvariable=self.message4).grid(row=4, column=20)
        Label(self.master.root, textvariable=self.message5, fg="blue", font=("Helvetica", 12)).grid(row=5, column=20)
        Label(self.master.root, textvariable=self.message6).grid(row=6, column=20)
        Label(self.master.root, textvariable=self.message7, fg="red", font=("Helvetica", 16)).grid(row=7, column=20)

    def init_buttons(self):
        self.buttonCreateShips = Button(self.master.root, text="Create ships automatically", command=self.master.auto_build_ships)
        self.buttonCreateShips.grid(row=9, column=20)
        self.buttonClearShips = Button(self.master.root, text="Clear ships", command=self.master.clear_ships)
        self.buttonClearShips.grid(row=11, column=20)

