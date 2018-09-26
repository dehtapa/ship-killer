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
        pass

    def place_ships(self, row, column):
        pass

    def get_to_build(self):
        pass

    def button_fired(self, row, column):
        pass

    def checkShipsToPlace(self):  #
        pass

    def set_building_messages(self, name):
        pass

    def auto_build_ships(self):
        pass

    def get_side_neighbours(self, x, y):
        pass

    def get_all_neighbours(self, row, column):
        pass

    def check_fields(self, fieldList, shipNumber, pull):
        pass

    def clean_neighbours(self, neighbours):
        pass

    def clear_ships(self):
        pass
