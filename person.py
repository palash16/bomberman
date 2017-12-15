class Person:
    """ Person class which is inherited by Bomber and Enemy contains functions related to movement etc."""

    def __init__(self, x, y):
        self._position = [x, y]

    def setPosition(self, x, y):
        self._position = [x, y]

    def getPosition(self):
        return self._position

    def InsertPerson(self, array):
        [x, y] = self.getPosition()
        if (array[y][x] != ' ' and array[y][x] != 'B'):
            return 0
        for p in range(4):
            array[y][x + p] = self._shape[0][p]
            array[y + 1][x + p] = self._shape[1][p]

    def RemovePerson(self, array):
        [x, y] = self.getPosition()
        if (array[y + 1][x] == '['):
            return 0
        for p in range(4):
            array[y][x + p] = ' '
            array[y + 1][x + p] = ' '

    def moveRight(self, array):
        [x, y] = self.getPosition()
        if (array[y][x + 4] != ' ' and array[y][x + 4] != '['
                and array[y][x + 4] != 'E' and array[y][x + 4] != 'B'):
            return 0
        else:
            self.setPosition(x + 4, y)
            return 1

    def moveLeft(self, array):
        [x, y] = self.getPosition()
        if (array[y][x - 4] != ' ' and array[y][x - 4] != '['
                and array[y][x - 4] != 'E' and array[y][x - 4] != 'B'):
            return 0
        else:
            self.setPosition(x - 4, y)
            return 1

    def moveUp(self, array):
        [x, y] = self.getPosition()
        if (array[y - 2][x] != ' ' and array[y - 2][x] != '['
                and array[y - 2][x] != 'E' and array[y - 2][x] != 'B'):
            return 0
        else:
            self.setPosition(x, y - 2)
            return 1

    def moveDown(self, array):
        [x, y] = self.getPosition()
        if (array[y + 2][x] != ' ' and array[y + 2][x] != '['
                and array[y + 2][x] != 'E' and array[y + 2][x] != 'B'):
            return 0
        else:
            self.setPosition(x, y + 2)
            return 1
