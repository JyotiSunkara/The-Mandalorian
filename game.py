import signal
import os
import time
from colorama import init
init()

def move (y, x):
    print("\033[%d;%dH" % (y, x))

from mandalorian import Din
from scenery import Scenery
from grid import Grid
from alarmexception import AlarmException
from getch import _getChUnix as getChar

gridObj = Grid(30, 500)

mandalorianObj = Din(25, 20, 1)
mandalorianObj.placeDin(gridObj.matrix)

sceneryObj = Scenery()

sceneryObj.createGround(gridObj.matrix)
sceneryObj.createSky(gridObj.matrix)

T = time.time()


def moveDin():
    ''' Moves Din left, right'''
    def alarmhandler(signum, frame):
        ''' Input method '''
        raise AlarmException

    def user_input(timeout = 0.1):
        ''' Input method '''
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''           

    keyPress = user_input()

    if keyPress == 'd':
            mandalorianObj.removeDin(gridObj.matrix)
            mandalorianObj.x = mandalorianObj.x + 2
            mandalorianObj.direction = 1
            mandalorianObj.showDin(gridObj.matrix)


speedfactor = 1
start = 0

while True:

    while (start + 100) < 500:
        move(0,0)
        gridObj.printView(start)
        start = start + speedfactor
        time.sleep(0.1)

    moveDin()
