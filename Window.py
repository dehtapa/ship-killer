from tkinter import *


class Window:
    def __init__(self, x, y):
        self.root = Tk()
        self.root.title("Shipkiller")
        self.root.geometry("%sx%s" % (x, y))