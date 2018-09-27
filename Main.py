from Player import *
from Ship import *
from Table import *
from Window import *
import tkinter as tk


class Game:
    turn = 1
    window = None
    table1 = None
    table2 = None
    player1 = None
    player2 = None

    def __init__(self, root, numberOfShips, rows):
        self.root = root
        self.numberOfShips = numberOfShips
        self.rows = rows
        # Start process
        self.init_game()
        
    def init_game(self):
        pass
        # Draw main window
        # self.window = Window(self)        
        # Draw tables
        #self.table1 = Table(1, self, 0, 0)
        #self.table2 = Table(2, self, 0, 40)
        # Create players
        #self.player1 = Player('Player1')
        #self.player2 = Player('Player2')
        #self.skip_status()

    def auto_build_ships(self):
        pass

    def skip_status(self):
        pass
    
    def clear_ships(self):
        pass


def main(numberOfShips, rows, width, height): #run mianloop 
    root = tk.Tk()
    root.geometry("%sx%s" % (width, height))
    app = Game(root, numberOfShips, rows)
    root.mainloop()


if __name__ == '__main__':
    main(4, 10, 1200, 900)
