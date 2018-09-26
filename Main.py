from Player import *
from Ship import *
from Table import *
from Window import *
from Game import *


class Main:
    window = None
    player1 = None
    player2 = None

    def __init__(self, numberOfShips, rows):
        self.numberOfShips = numberOfShips
        self.rows = rows
        self.game = Game()
        # Start process
        self.init_game()
        self.end_game()
        
    def init_game(self):
        print("AKJHSDJKH")
        # Draw main window
        self.window = Window(self, 1200, 900)
        
        # Draw tables
        self.table1 = Table(1, self, 0, 0)
        self.table2 = Table(2, self, 0, 40)
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

    def end_game(self):
        self.window.root.mainloop()

game = Main(4, 5)