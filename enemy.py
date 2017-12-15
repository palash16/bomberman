from person import *
from random import randint


class Enemy(Person):
    """ Enemies class inherited from Person class contains functions like random movement etc."""

    def __init__(self, x, y):
        self._shape = [['E' for i in range(4)] for j in range(2)]
        self._position = [x, y]

    def RandomChoice(self, board, num):
        if (num == 0):
            return self.moveUp(board)
        if (num == 1):
            return self.moveDown(board)
        if (num == 2):
            return self.moveLeft(board)
        if (num == 3):
            return self.moveRight(board)

    def RandomMove(self, board):
        temp = 0
        stor = []
        # while(temp!=1):
        rand = randint(0, 3)
        # stor.append(rand)
        self.RandomChoice(board, rand)
        # if(self.RandomChoice(board,rand) == 1 and rand not in stor):

    # temp = 1
