from time import time


class Bomb:
    """ This is Bomb's class which contains features related to bomb such as Explosion etc. """

    def __init__(self, x, y):
        self._position = [x, y]
        self._time = 2
        self._realtime = time()
        self._shape = [['[', '1', '1', ']'], ['[', '1', '1', ']']]

    def getRtime(self):
        return self._realtime

    def setRtime(self, Rtime):
        self._realtime = Rtime

    def setTime(self, time):
        self._time = time
        self._shape = [['[',
                        chr(self._time + 47),
                        chr(self._time + 47), ']'],
                       ['[',
                        chr(self._time + 47),
                        chr(self._time + 47), ']']]

    def getTime(self):
        return self._time

    def setPostition(self, x, y):
        self._position = [x, y]

    def getPosition(self):
        return self._position

    def InsertBomb(self, array):
        [x, y] = self.getPosition()
        for p in range(4):
            array[y][x + p] = self._shape[0][p]
            array[y + 1][x + p] = self._shape[1][p]

    def RemoveBomb(self, array):
        [x, y] = self.getPosition()
        for p in range(4):
            array[y][x + p] = ' '
            array[y + 1][x + p] = ' '

    def display(self, x, y, array, ch):
        if (array[y][x] != 'X'):
            for p in range(4):
                array[y][x + p] = ch
                array[y + 1][x + p] = ch

    def Explosion(self, array, ch):
        [x, y] = self.getPosition()
        self.display(x + 4, y, array, ch)
        self.display(x - 4, y, array, ch)
        self.display(x, y - 2, array, ch)
        self.display(x, y + 2, array, ch)
        self.display(x, y, array, ch)
