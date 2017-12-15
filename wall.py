class Wall:
    """ Wall class which contains the structure of each brick and applies the same to the main board"""
    def __init__(self, p, q):
        self._shape = [['X' for x in range(4)] for y in range(2)]
        self._position = [p, q]

    def setBPostition(self, x, y):
        self._position = [x, y]

    def getBPosition(self):
        return self._position

    def InsertWall(self, array):
        [x, y] = self.getBPosition()
        for p in range(4):
            array[y][x + p] = self._shape[0][p]
            array[y + 1][x + p] = self._shape[1][p]


class Brick(Wall):
    def __init__(self, p, q):
        self._shape = [['/' for x in range(4)] for y in range(2)]
        self._door = 0
        self._position = [p, q]

    def setDoor(self, x):
        self._door = x

    def getDoor(self):
        return self._door

