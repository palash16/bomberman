from person import *


class Bomber(Person):
    """ This is Bomber class inherited from Person class, this class represents the bomberman in the game"""

    def __init__(self, x, y):
        self._shape = [['B' for i in range(4)] for j in range(2)]
        self._lives = 3
        self._position = [x, y]

    def getLives(self):
        return self._lives

    def setLives(self, num):
        self._lives = num
