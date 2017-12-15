from __future__ import print_function
import signal, copy, sys, time, os
from wall import *
from bomber import *
from person import *
from enemy import *
from getchunix import *
from bomb import *
from random import randint
from time import time
from termcolor import colored
from allfuncs import *

Level = 1
bmb = 0
boardx = 84
boardy = 42
board = [[' ' for x in range(boardx)] for y in range(boardy)]
bomber = Bomber(4, 2)
BombStatus = 0
numEnemies = 4
enemies = []
Score = 0
numBricks = 20
gameplay = allfuncs()

getch = GetchUnix()


def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print()
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


def moveEnemies(board):
    for i in range(numEnemies):
        enemies[i].RemovePerson(board)
        enemies[i].RandomMove(board)
        enemies[i].InsertPerson(board)


CreateTime = time()
gameplay.MakeWall(board, numEnemies, numBricks, boardx, boardy, enemies)
gameplay.PrintGame(board, bomber, Score, Level)

while (1):
    curr = time()
    mv = input_to()
    if (curr - CreateTime >= 0.5):
        moveEnemies(board)
        CreateTime = curr

    if (BombStatus == 2 and curr - bmb.getRtime() >= 0.5):
        Score = gameplay.checkBomber(board, bmb, bomber, Score)
        bmb.Explosion(board, ' ')
        BombStatus = 0

    if (BombStatus == 1 and curr - bmb.getRtime() >= 0.5):
        bmb.setRtime(curr)
        bmb.setTime(bmb.getTime() - 1)
        if (bmb.getTime() == 0):
            bmb.RemoveBomb(board)
            Score = gameplay.checkWall(board, bmb, Score)
            bmb.Explosion(board, 'e')
            BombStatus = 2
            [enemies, numEnemies, Score] = gameplay.checkEnemy(
                board, bmb, numEnemies, enemies, Score)
        else:
            bmb.InsertBomb(board)

    if (mv == 'q'):
        print(colored("You Quitted the Game", 'red'))
        print(colored("Your Score: ", 'yellow'), Score)
        sys.exit(0)

    if (mv == 'd'):
        bomber.RemovePerson(board)
        bomber.moveRight(board)

    if (mv == 'a'):
        bomber.RemovePerson(board)
        bomber.moveLeft(board)

    if (mv == 's'):
        bomber.RemovePerson(board)
        bomber.moveDown(board)

    if (mv == 'w'):
        bomber.RemovePerson(board)
        bomber.moveUp(board)

    if (mv == 'b'):
        if (BombStatus == 0):
            [p, q] = bomber.getPosition()
            bmb = Bomb(p, q)
            bmb.InsertBomb(board)
            BombStatus = 1

    os.system("tput reset")
    gameplay.PrintGame(board, bomber, Score, Level)

    for enemy in enemies:
        if (enemy.getPosition() == bomber.getPosition()):
            bomber.setLives(bomber.getLives() - 1)
            bomber.setPosition(4, 2)
            if (bomber.getLives() == 0):
                bomber.RemovePerson(board)
                # PrintGame(board)
                print(colored("Game Over", 'red'))
                print(colored("Your Score:", 'yellow'), Score)
                sys.exit(0)
            # PrintGame(board)

    if (numEnemies == 0 and Level == 1):
        print(colored("Level 1 Complete", 'green'))
        numEnemies, Level, numBricks = 5, 2, 25
        gameplay.LevelUp(board, bomber, numEnemies, numBricks, boardx, boardy,
                         enemies)

    elif (numEnemies == 0 and Level == 2):
        print(colored("Level 2 Complete", 'green'))
        numEnemies, Level, numBricks = 6, 3, 30
        gameplay.LevelUp(board, bomber, numEnemies, numBricks, boardx, boardy,
                         enemies)

    if (numEnemies == 0 and Level == 3):
        print(colored("You Won", 'green'))
        print(colored("Your Score is :", 'yellow'), Score)
        sys.exit(0)

    # PrintGame(board)
