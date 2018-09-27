class Table():
    def __init__(self, side):
        self.side = side
        self.matrix = {}
        self.create_matrix()

    def create_matrix(self):
        for x in range(1, self.side + 1):
            self.matrix[x] = {}
            for y in range(1, self.side + 1):
                self.matrix[x][y] = ''

    def update_matrix(self, row, column, value):
        self.matrix[row][column] = value
