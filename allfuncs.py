from __future__ import print_function
import signal, copy, sys, time, os
from wall import *
from bomber import *
from person import *
from enemy import *
from bomb import *
from random import randint
from time import time
from termcolor import colored


class allfuncs:
    """ This class contains all functions necessary for gameplay """
    def MakeWall(self, board, numEnemies, numBricks, boardx, boardy, enemies):
        q = 0
        for y in range(21):
            p = 0
            for x in range(21):
                if (q == 0 or q == boardy - 2 or p == 0 or p == boardx - 4
                        or (q % 4 == 0 and p % 8 == 0)):
                    w = Wall(p, q)
                    w.InsertWall(board)
                p += 4
            q += 2
        count = 0

        while (count < numBricks):
            bx, by = randint(0, 19), randint(0, 19)
            bx, by = 4 * bx, 2 * by
            if (board[by][bx] == ' ' and bx != 4 and by != 2):
                b = Brick(bx, by)
                b.InsertWall(board)
                if (count == 1):
                    b.setDoor(1)
                count += 1

        count = 0
        while (count < numEnemies):
            bx, by = randint(0, 19), randint(0, 19)
            bx, by = 4 * bx, 2 * by
            if (board[by][bx] == ' ' and bx != 4 and by != 2):
                enemies.append(Enemy(bx, by))
                enemies[count].InsertPerson(board)
                count += 1

    def PrintGame(self, board, bomber, Score, Level):
        print(colored("Your Current Score: ", 'blue', attrs=['bold']), Score)
        print(colored("Lives Left: ", 'red', attrs=['bold']),
              bomber.getLives())
        print(colored("Level :", 'cyan', attrs=['bold']), Level)
        bomber.InsertPerson(board)
        for y in range(42):
            for x in range(84):
                if (board[y][x] == 'E'):
                    print(colored(board[y][x], 'red'), end='')
                elif (board[y][x] == 'B'):
                    print(
                        colored(board[y][x], 'yellow', attrs=['bold']), end='')
                elif (board[y][x] == '1'):
                    print(colored(board[y][x], 'red'), end='')
                elif (board[y][x] == '0'):
                    print(colored(board[y][x], 'green'), end='')
                elif (board[y][x] == 'e'):
                    print(colored(board[y][x], 'magenta'), end='')
                elif (board[y][x] == '/'):
                    print(colored(board[y][x], 'cyan'), end='')
                elif (board[y][x] == ']' or board[y][x] == '['):
                    print(colored(board[y][x], 'blue'), end='')
                else:
                    print(board[y][x], end='')
            print('')

    def checkBomber(self, board, bmb, bomber, Score):
        [p, q] = bmb.getPosition()
        [x, y] = bomber.getPosition()

        if ([x, y] == [p, q] or [p + 4, q] == [x, y] or [p - 4, q] == [x, y]
                or [p, q + 2] == [x, y] or [p, q - 2] == [x, y]):
            bomber.setLives(bomber.getLives() - 1)
            bomber.setPosition(4, 2)
            if (bomber.getLives() == 0):
                print(colored("Game Over", 'red'))
                print(colored("Your Score:", 'yellow'), Score)
                sys.exit(0)
        return Score

    def checkWall(self, board, bmb, Score):
        [p, q] = bmb.getPosition()
        if (board[q + 2][p] == '/'):
            Score = Score + 20
        if (board[q - 2][p] == '/'):
            Score = Score + 20
        if (board[q][p + 4] == '/'):
            Score = Score + 20
        if (board[q][p - 4] == '/'):
            Score = Score + 20
        return Score

    def checkEnemy(self, board, bmb, numEnemies, enemies, Score):
        for enemy in enemies:
            [x, y] = enemy.getPosition()
            [p, q] = bmb.getPosition()
            if ([x, y] == [p, q] or [p + 4, q] == [x, y]
                    or [p - 4, q] == [x, y] or [p, q + 2] == [x, y]
                    or [p, q - 2] == [x, y]):
                enemy.RemovePerson(board)
                enemies.remove(enemy)
                numEnemies -= 1
                Score += 100
        return [enemies, numEnemies, Score]

    def LevelUp(self, board, bomber, numEnemies, numBricks, boardx, boardy,
                enemies):
        bomber.RemovePerson(board)
        bomber.setPosition(4, 2)
        self.MakeWall(board, numEnemies, numBricks, boardx, boardy, enemies)
