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
from items import Item, Bullet

gridObj = Grid(30, 500)

mandalorianObj = Din(25, 20, 1)
mandalorianObj.placeDin(gridObj.getMatrix())

sceneryObj = Scenery()

sceneryObj.createGround(gridObj.getMatrix())
sceneryObj.createSky(gridObj.getMatrix())

T = time.time()

speedfactor = 1
start = 0
gravity = 0.5

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
	
    if mandalorianObj.getAirHeight() > 0:
        mandalorianObj.incrementAirTime()

    keyPress = user_input()

    if keyPress == 'd':
        if mandalorianObj.daye(start):
            mandalorianObj.removeDin(gridObj.getMatrix())
            mandalorianObj.changeY(2)
            mandalorianObj.setDirection(1)
            mandalorianObj.showDin(gridObj.getMatrix())

    if keyPress == 'a':
        if mandalorianObj.bayehaathkakhel(start):
            mandalorianObj.removeDin(gridObj.getMatrix())
            mandalorianObj.changeY(-2)
            mandalorianObj.setDirection(0)
            mandalorianObj.showDin(gridObj.getMatrix())
    
    if keyPress == 'w':
        if mandalorianObj.upupandaway():
            mandalorianObj.removeDin(gridObj.getMatrix())
            mandalorianObj.setAirTime(0) 
            mandalorianObj.changeX(-1)
            mandalorianObj.changeHeightAir(1)
            mandalorianObj.showDin(gridObj.getMatrix())
    
    if keyPress == 'q':
        quit()
    
    if keyPress == 's':
        bulletObj = Bullet(mandalorianObj.getX(), mandalorianObj.getY())
        
        

while True: 
    moveDin()

    if (start + 100) < 500:
        start = start + speedfactor
    
    move(0,0)
    gridObj.printView(start)
    
    if mandalorianObj.getAirHeight() > 0: 
        distance = int (0.5 * gravity * (mandalorianObj.getAirTime()))
        if mandalorianObj.limbolow(distance) == 1:
            mandalorianObj.changeHeightAir(-distance)
            mandalorianObj.removeDin(gridObj.getMatrix())
            mandalorianObj.changeX(distance)
            mandalorianObj.showDin(gridObj.getMatrix())
        elif mandalorianObj.limbolow(distance) == -1:
            while mandalorianObj.getX() < 25:
                mandalorianObj.changeHeightAir(-1)
                mandalorianObj.removeDin(gridObj.getMatrix())
                mandalorianObj.changeX(1)
                mandalorianObj.showDin(gridObj.getMatrix())

    if (mandalorianObj.getY() - 1) < start:
        mandalorianObj.removeDin(gridObj.getMatrix())
        mandalorianObj.changeY(1)
        mandalorianObj.showDin(gridObj.getMatrix())

    if (mandalorianObj.getY() + 6) > (start + 100):
        mandalorianObj.removeDin(gridObj.getMatrix())
        mandalorianObj.changeY(-1)
        mandalorianObj.showDin(gridObj.getMatrix())
    
