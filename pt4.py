from tkinter import *
import random
import time


class Main:
    def __init__(self, ships, rows):
        self.ships = ships
        self.rows = rows
        self.gameStatus = 0
        self.window = None
        self.table1 = None
        self.table2 = None
        self.player = None
        # Start process
        self.init_game()
        self.end_game()

    def init_game(self):
        # Draw main window
        self.window = Window(self, 1200, 900)
        # Draw tables
        self.table1 = Table(1, self, 0, 0)
        self.table2 = Table(2, self, 0, 40)
        # Create players
        self.player1 = Player('Player1')
        self.player2 = Player('Player2')
        self.skip_status()

    def skip_status(self):
        self.gameStatus += 1
        print(self.gameStatus)
        if self.gameStatus == 1:
            self.table1.set_building_messages(self.player1.name)
        elif self.gameStatus == 2:
            self.table2.set_building_messages(self.player2.name)
        elif self.gameStatus >= 3:
            self.window.message1.set('%s is shooting' % self.player1.name)
            self.window.message2.set('%s has ships (destroyed/all:)' % self.player1.name)
            self.window.message3.set('%s/%s' % self.table2.destroyedShips, self.numberOfShips)
            self.window.message4.set('%s has ships (destroyed/all:)' % self.player2.name)
            self.window.message5.set('%s/%s' % self.table2.destroyedShips, self.numberOfShips)

            if self.gameStatus % 2 == 1:  # Player1 is shooting
                self.window.message1.set('%s is shooting' % self.player1.name)
                self.table1.buttonFired(self.currentPlayer, row, column)  # Table.buttonFired
            if self.gameStatus % 2 == 0:  # Player2 is shooting
                self.window.message1.set('%s is shooting' % self.player2.name)
                self.table1.buttonFired(self.currentPlayer, row, column)  # Table.buttonFired
                row = random.randint(1, self.rows)
        column = random.randint(1, self.rows)

    def auto_build_ships(self):
        if self.gameStatus == 1:
            self.table1.auto_build_ships()
        if self.gameStatus == 2:
            self.table2.auto_build_ships()
            skip_status()

    def clear_ships(self):
        if self.gameStatus == 1:
            self.table1.clear_ships()
        if self.gameStatus == 2:
            self.table2.clear_ships()

    def end_game(self):
        self.window.root.mainloop()


class Player:
    def __init__(self, name):
        self.name = name


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


class Table():
    def __init__(self, id, master, shiftX, shiftY):
        self.id = id
        self.root = master.window.root
        self.window = master.window
        self.rows = master.rows
        self.master = master
        self.shiftX = shiftX
        self.shiftY = shiftY
        self.currentShip = master.ships
        self.coords = Matrix(master.rows)
        self.buttons = {}
        self.ships = {}
        # Start process
        self.draw_table_buttons()
        self.build_ships()

    def draw_table_buttons(self):
        for x in range(1, self.rows + 1):
            self.buttons[x] = {}
            for y in range(1, self.rows+1):
                self.buttons[x][y] = Button(master=self.root, bg="azure2", command=lambda row=x,
                                            column=y: self.button_fired(row, column))
                self.buttons[x][y].grid(row=self.shiftX + y, column=self.shiftY + x)

    def build_ships(self):
        for x in range(1, self.master.ships + 1):
            self.ships[x] = Ship(x)

    def place_ships(self, row, column):
        self.coords.update_matrix(row, column, self.currentShip)
        self.buttons[row][column]["bg"] = "green"
        self.ships[self.currentShip].build()
        if self.ships[self.currentShip].isBuilt() is True:
            self.currentShip -= 1

    def get_to_build(self):
        return self.ships[self.currentShip].toBuild()

    def button_fired(self, row, column):
        if (self.master.gameStatus == 1 or self.master.gameStatus == 2) and self.master.gameStatus == self.id:
            self.place_ships(row, column)
            self.checkShipsToPlace()

    def checkShipsToPlace(self):  # 
        if self.currentShip <= 0:
            self.master.skip_status()
        else:
            self.window.message3.set(self.currentShip)
            self.window.message5.set(self.get_to_build())

    def set_building_messages(self, name):
        self.window.message1.set('%s is placing her/his ships.' % name)
        self.window.message2.set('Number of blocks your ship must contains:')
        self.window.message3.set(self.currentShip)
        self.window.message4.set('Remaining blocks you must place:')
        self.window.message5.set(self.get_to_build())

    def auto_build_ships(self):
        for shipNumber in range(1, self.master.ships + 1):
            while True:
                firstRow = random.randint(1, self.rows)
                firstColumn = random.randint(1, self.rows)
                neighbours = self.get_all_neighbours(firstRow, firstColumn)
                if self.check_fields(neighbours, shipNumber, False) is True:
                    sideNeighbours = self.get_side_neighbours(firstRow, firstColumn)
                    cleanedSideNeighbours = self.check_fields(sideNeighbours, shipNumber, True)
                    if len(cleanedSideNeighbours) >= 2:
                        break
            self.place_ships(firstRow, firstColumn)
            print('place', firstRow, firstColumn)
            for unit in range(1, shipNumber):
                while True:
                    newField = random.sample(cleanedSideNeighbours, 1)
                    x = newField[0][0]
                    y = newField[0][1]
                    neighbours = self.get_all_neighbours(x, y)
                    if self.check_fields(neighbours, shipNumber, False) is True:
                        sideNeighbours = self.get_side_neighbours(x, y)
                        newCleanedSideNeighbours = self.check_fields(sideNeighbours, shipNumber, True)
                        if len(newCleanedSideNeighbours) >= 1:
                            break
                self.place_ships(x, y)
                print('place2', firstRow, firstColumn)
                cleanedSideNeighbours.remove([x, y])
                cleanedSideNeighbours += newCleanedSideNeighbours
        self.master.skip_status()

    def get_side_neighbours(self, x, y):
        fields = []
        if x > 1:
            fields.append([x-1, y])
        if y > 1:
            fields.append([x, y-1])
        if x < self.rows - 1:
            fields.append([x+1, y])
        if y < self.rows - 1:
            fields.append([x, y+1])
        return fields

    def get_all_neighbours(self, row, column):
        neighbours = []
        fromX = row-1 if row >= 2 else 1
        fromY = column-1 if column >= 2 else 1
        toX = row+2 if row <= self.rows - 1 else self.rows + 1
        toY = column+2 if column <= self.rows - 1 else self.rows + 1
        for x in range(fromX, toX):
            for y in range(fromY, toY):
                neighbours.append([x, y])
        return neighbours

    def check_fields(self, fieldList, shipNumber, pull):
        answer = True
        for field in fieldList:
            x = field[0]
            y = field[1]
            if self.coords.matrix[x][y] > 0 and self.coords.matrix[x][y] is not shipNumber:
                if pull is False:
                    return False
                fieldList.remove([x, y])
            if pull is False:
                return True
            else:
                return fieldList

    def clean_neighbours(self, neighbours):
        print('maci')

    def clear_ships(self):
        table = self.draw_table_buttons()
        self.currentShip = self.master.ships
        self.coords = Matrix(self.rows)
        self.buttons = {}
        self.ships = {}
        self.draw_table_buttons()
        self.build_ships()
        self.set_building_messages(self, 'Player 1.')


class Matrix():
    def __init__(self, rows):
        self.rows = rows
        self.matrix = {}
        self.create_matrix()

    def create_matrix(self):
        for x in range(1, self.rows + 1):
            self.matrix[x] = {}
            for y in range(1, self.rows+1):
                self.matrix[x][y] = 0

    def update_matrix(self, row, column, value):
        self.matrix[row][column] = value


class Ship:
    def __init__(self, units):
        self.units = units
        self.built = 0
        self.destroyed = 0

    def isBuilt(self):
        if self.built >= self.units:
            return True
        else:
            return False

    def toBuild(self):
        return self.units - self.built

    def isDestroyed(self):
        if self.destroyed >= self.units:
            return True
        else:
            return False

    def build(self):
        print('build')
        self.built += 1

    def destroy(self):
        self.destroyed += 1


Main(3, 10)
