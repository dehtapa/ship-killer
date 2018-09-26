from tkinter import *


class Window:
    def __init__(self, master, width, height):
        self.width = width
        self.height = height
        self.rows = master.rows
        self.master = master
        self.root = None
        # init window
        self.draw_main_window()

        self.message1 = StringVar(value="")
        self.message2 = StringVar(value="")
        self.message3 = StringVar(value="")
        self.message4 = StringVar(value="")
        self.message5 = StringVar(value="")
        self.message6 = StringVar(value="")
        self.message7 = StringVar(value="")
        self.buttonCreateShips = None
        self.buttonClearShips = None
        # Start process
        self.init_messages()
        self.init_buttons()

    def draw_main_window(self):
        print("KJHKJ")
        self.root = Tk()
        self.root.geometry("%sx%s" % (self.width, self.height))

    def init_messages(self):
        Label(self.root, textvariable=self.message1, fg="blue", font=("Helvetica", 16)).grid(row=0, column=20)
        Label(self.root, textvariable=self.message2).grid(row=2, column=20)
        Label(self.root, textvariable=self.message3, fg="blue", font=("Helvetica", 12)).grid(row=3, column=20)
        Label(self.root, textvariable=self.message4).grid(row=4, column=20)
        Label(self.root, textvariable=self.message5, fg="blue", font=("Helvetica", 12)).grid(row=5, column=20)
        Label(self.root, textvariable=self.message6).grid(row=6, column=20)
        Label(self.root, textvariable=self.message7, fg="red", font=("Helvetica", 16)).grid(row=7, column=20)

    def init_buttons(self):
        self.buttonCreateShips = Button(self.root, text="Create ships automatically", command=self.master.auto_build_ships)
        self.buttonCreateShips.grid(row=9, column=20)
        self.buttonClearShips = Button(self.root, text="Clear ships", command=self.master.clear_ships)
        self.buttonClearShips.grid(row=11, column=20)