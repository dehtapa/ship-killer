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
