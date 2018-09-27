from tkinter import *


class Window:
    buttonCreateShips = None
    buttonClearShips = None

    def __init__(self, master):
        self.master = master
        self.message1 = StringVar(value="")
        self.message2 = StringVar(value="")
        self.message3 = StringVar(value="")
        self.message4 = StringVar(value="")
        self.message5 = StringVar(value="")
        self.message6 = StringVar(value="")
        self.message7 = StringVar(value="")
        # Start process
        self.init_messages()
        self.init_buttons()
        self.init_image()
        # self.run_animate()

    def init_messages(self):
        Label(self.master.root, textvariable=self.message1, fg="blue", font=("Helvetica", 16)).grid(row=0, column=20)
        Label(self.master.root, textvariable=self.message2).grid(row=2, column=20)
        Label(self.master.root, textvariable=self.message3, fg="blue", font=("Helvetica", 12)).grid(row=3, column=20)
        Label(self.master.root, textvariable=self.message4).grid(row=4, column=20)
        Label(self.master.root, textvariable=self.message5, fg="blue", font=("Helvetica", 12)).grid(row=5, column=20)
        Label(self.master.root, textvariable=self.message6).grid(row=6, column=20)
        Label(self.master.root, textvariable=self.message7, fg="red", font=("Helvetica", 16)).grid(row=7, column=20)

    def init_buttons(self):
        self.buttonCreateShips = Button(self.master.root, text="Create ships automatically",
                                        command=self.master.auto_fill_both)
        self.buttonCreateShips.grid(row=9, column=20)
        self.buttonClearShips = Button(self.master.root, text="Clear ships", command=self.master.clear_ships)
        self.buttonClearShips.grid(row=11, column=20)
        self.buttonCheat = Button(self.master.root, text="Cheat", command=self.master.cheatActivate)
        self.buttonCheat.grid(row=12, column=20)
        self.buttonComputerCheat = Button(self.master.root, text="Computer cheat", command=self.master.computerCheat)
        
    def init_image(self):
        self.img = Label(self.master.root)
        gif1 = PhotoImage(file='/home/toybox/codecool/python-projects/4th-TW-week/ship-killer/giphy.gif',
                          format='gif -index %s' % 0)
        self.img.image = gif1
        self.img.configure(image=gif1)
        self.img.grid(row=13, column=20, columnspan=2, sticky=NW)
        self.counter = 0

    def run_animate(self, ind):
        self.counter += 1
        gif1 = PhotoImage(file='/home/toybox/codecool/python-projects/4th-TW-week/ship-killer/giphy.gif',
                          format='gif -index %s' % ind)
        ind += 1
        self.img.image = gif1
        self.img.configure(image=gif1)
        if self.counter < 12:
            self.master.root.after(
                200, lambda: self.run_animate(ind))
        else:
            self.counter = 0
            gif1 = PhotoImage(
                file='/home/toybox/codecool/python-projects/4th-TW-week/ship-killer/giphy.gif', format='gif -index %s' % 0)
            self.img.image = gif1
            self.img.configure(image=gif1)

    def change_image(self, ind):
        print(ind)
        gif1 = PhotoImage(file='/home/toybox/codecool/python-projects/4th-TW-week/ship-killer/giphy.gif',
                          format='gif -index %s' % ind)
        self.img.image = gif1
        self.img.configure(image=gif1)
