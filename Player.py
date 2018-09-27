from Table import *
from Ship import *
import random


class Player:
    def __init__(self, master, id, name, table, robot, numberOfShips, rows):
        self.maxNumberOfShips = numberOfShips
        self.master = master
        self.rows = rows
        self.ships = {}
        self.currentShip = numberOfShips
        self.shipCoordinates = Table(rows)
        self.shots = Table(rows)
        self.id = id
        self.name = name
        self.table = table
        self.robot = robot
        self.score = 0
        self.wins = 0
        self.build_ships()
        self.destroyedShips = 0

    def build_ships(self):
        for x in range(1, self.maxNumberOfShips + 1):
            self.ships[x] = Ship(x)

    def get_shot(self, row, column):
        target = self.shipCoordinates.matrix[row][column]
        message = ''
        if str(target).isdigit() is True:
            self.table[row][column]["bg"] = "red"
            self.ships[target].destroy()
            if self.ships[target].isDestroyed():
                self.destroyedShips += 1
                return 'ship'
            return 'score'
        else:
            self.table[row][column]["bg"] = "grey"
            return 'fault'

    def place_ships(self, row, column):
        if self.check_field_valid():
            self.shipCoordinates.update_matrix(row, column, self.currentShip)
            print('placing ships')
            if self.id is 1:
                self.table[row][column]["bg"] = "green"
            self.ships[self.currentShip].build()
            if self.ships[self.currentShip].isBuilt() is True:
                texts = ['Na végre!', 'Elaludtál?!', 'Még ma sikerül leraknod?', 'Na mi van már?']
                self.currentShip -= 1
                if self.id is 1:
                    self.master.say(texts[self.currentShip])

            if self.currentShip <= 0:
                return 'next'
            else:
                return self.get_ship_message()

    def get_ship_message(self):
        #print('get message')
        # print(self.ships[self.currentShip].toBuild())
        contain = self.currentShip
        more = self.ships[self.currentShip].toBuild()
        return [
            'Number of blocks your ship must contains:',
            contain,
            'Remaining blocks you must place:',
            more
        ]

    def auto_fill(self):
        size = self.maxNumberOfShips
        for i in range(size):
            shipAlignment = random.randint(
                1, 2)  # horizontal = 1, veritcal = 2
            row = random.randint(1, 9)
            column = random.randint(1, 9)
            if shipAlignment is 1:
                while row + size > 10 or not self.ifAvailable(
                        row, column, size, shipAlignment):  # if out of bonds OR places are taken
                    row = random.randint(1, 9)
                    column = random.randint(1, 9)
                for j in range(0, size):
                    # use this method to place them next to eachoter - it makes
                    # them as one ship
                    self.place_ships(row + j, column)
            else:
                while column + size > 10 or not self.ifAvailable(
                        row, column, size, shipAlignment):  # if out of bonds OR places are taken
                    row = random.randint(1, 9)
                    column = random.randint(1, 9)
                for j in range(0, size):
                    self.place_ships(row, column + j)
            size -= 1

    def ifAvailable(self, row, column, size, alignment):
        # alignment; horizontal = 1, veritcal = 2
        available = False
        for i in range(0, size + 1):
            if alignment is 1:  # check horizontal
                if self.shipCoordinates.matrix[row + i][column] == '':
                    available = True
                else:
                    available = False
            else:  # check vertical
                if self.shipCoordinates.matrix[row][column + i] == '':
                    available = True
                else:
                    available = False
        return available

    # check surrounding blocks, return true if neighbours are empty
    def checkNeighbours(self, row, column):
        # available = False
        # row_limit = 9
        # if row_limit > 0:
        #   column_limit = 9
        #   for x in range(max(0,row-1),min(row+1,row_limit)):
        #     for y in range(column-1,min(column+1,column_limit)):
        #       if x != row or y != column:
        #         if self.shipCoordinates.matrix[x][y] == '' :
        #           available = False
        #         else:
        #           available = True
        # return
        pass

    def check_field_valid(self):
        print('validity check')
        return True