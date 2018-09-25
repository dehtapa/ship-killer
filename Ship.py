class Ship:
    def __init__(self, squares):
        self.squares = squares
        self.built = 0
        self.destroyed = 0

    def isBuilt(self):
        if self.built >= self.squares:
            return True
        else:
            return False

    def toBuild(self):
        return self.squares - self.built

    def isDestroyed(self):
        if self.destroyed >= self.squares:
            return True
        else:
            return False

    def build(self):
        print('build')
        self.built += 1

    def destroy(self):
        self.destroyed += 1
