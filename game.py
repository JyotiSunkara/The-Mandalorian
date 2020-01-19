import signal
import os
import time
import numpy
import random
from colorama import init
init()

def move (y, x):
    print("\033[%d;%dH" % (y, x))

from mandalorian import Din
from scenery import Scenery
from grid import Grid
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from items import Item, Bullet, Laser, Coins, SpeedUp
from configure import Configure


gridObj = Grid(30, 500)

mandalorianObj = Din(25, 10, 1)
mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)

sceneryObj = Scenery()

sceneryObj.createGround(gridObj.getMatrix())
sceneryObj.createSky(gridObj.getMatrix())

laserObj = []
coinObj = []
for i in range(16):
    laserObj.append(Laser(0,0))
    coinObj.append(Coins(0,0))

speedupObj = []
speedupObj.append(SpeedUp(0,0))
speedupObj.append(SpeedUp(0,0))

def addSpeedUps():
    for i in range(2):
        speedupObj[i].placeItem(gridObj.getMatrix(), random.randint(5,20), random.randint(100,300))

def removeSpeedUps():
    for i in range(2):
        speedupObj[i].removeItem(gridObj.getMatrix())    


def reprintLasers():
    laserObj[0].showItem(gridObj.getMatrix(),5,30)
    laserObj[1].showItem(gridObj.getMatrix(),10,60)
    laserObj[2].showItem(gridObj.getMatrix(),20,75)
    laserObj[3].showItem(gridObj.getMatrix(),2, 90)
    laserObj[4].showItem(gridObj.getMatrix(),20,120)
    laserObj[5].showItem(gridObj.getMatrix(),10,150)
    laserObj[6].showItem(gridObj.getMatrix(),15,180)
    laserObj[7].showItem(gridObj.getMatrix(),20,210)
    laserObj[8].showItem(gridObj.getMatrix(),5,240)
    laserObj[9].showItem(gridObj.getMatrix(),10,270)
    laserObj[10].showItem(gridObj.getMatrix(),20,300)
    laserObj[11].showItem(gridObj.getMatrix(),5,330)
    laserObj[12].showItem(gridObj.getMatrix(),15,360)
    laserObj[13].showItem(gridObj.getMatrix(),2,390)
    laserObj[14].showItem(gridObj.getMatrix(),20,390)
    laserObj[15].showItem(gridObj.getMatrix(),20,420)

def reprintCoins():
    coinObj[0].showItem(gridObj.getMatrix(), 16,30)
    coinObj[1].showItem(gridObj.getMatrix(), 4,45)
    coinObj[2].showItem(gridObj.getMatrix(), 20,90)
    coinObj[3].showItem(gridObj.getMatrix(), 4,105)
    coinObj[4].showItem(gridObj.getMatrix(), 8,135)
    coinObj[5].showItem(gridObj.getMatrix(), 12,165)
    coinObj[6].showItem(gridObj.getMatrix(), 4,195)
    coinObj[7].showItem(gridObj.getMatrix(), 8,225)
    coinObj[8].showItem(gridObj.getMatrix(), 20,255)
    coinObj[9].showItem(gridObj.getMatrix(), 4,285)
    coinObj[10].showItem(gridObj.getMatrix(), 12,315)
    coinObj[11].showItem(gridObj.getMatrix(), 20,345)
    coinObj[12].showItem(gridObj.getMatrix(), 8,375)
    coinObj[13].showItem(gridObj.getMatrix(), 4,405)
    coinObj[14].showItem(gridObj.getMatrix(), 20,405)
    coinObj[15].showItem(gridObj.getMatrix(), 16,440)


laserObj[0].placeItem(gridObj.getMatrix(),5,30)
laserObj[1].placeItem(gridObj.getMatrix(),10,60)
laserObj[2].placeItem(gridObj.getMatrix(),20,75)
laserObj[3].placeItem(gridObj.getMatrix(),2, 90)
laserObj[4].placeItem(gridObj.getMatrix(),20,120)
laserObj[5].placeItem(gridObj.getMatrix(),10,150)
laserObj[6].placeItem(gridObj.getMatrix(),15,180)
laserObj[7].placeItem(gridObj.getMatrix(),20,210)
laserObj[8].placeItem(gridObj.getMatrix(),5,240)
laserObj[9].placeItem(gridObj.getMatrix(),10,270)
laserObj[10].placeItem(gridObj.getMatrix(),20,300)
laserObj[11].placeItem(gridObj.getMatrix(),5,330)
laserObj[12].placeItem(gridObj.getMatrix(),15,360)
laserObj[13].placeItem(gridObj.getMatrix(),2,390)
laserObj[14].placeItem(gridObj.getMatrix(),20,390)
laserObj[15].placeItem(gridObj.getMatrix(),20,420)

coinObj[0].placeItem(gridObj.getMatrix(), 16,30)
coinObj[1].placeItem(gridObj.getMatrix(), 4,45)
coinObj[2].placeItem(gridObj.getMatrix(), 20,90)
coinObj[3].placeItem(gridObj.getMatrix(), 4,105)
coinObj[4].placeItem(gridObj.getMatrix(), 8,135)
coinObj[5].placeItem(gridObj.getMatrix(), 12,165)
coinObj[6].placeItem(gridObj.getMatrix(), 4,195)
coinObj[7].placeItem(gridObj.getMatrix(), 8,225)
coinObj[8].placeItem(gridObj.getMatrix(), 20,255)
coinObj[9].placeItem(gridObj.getMatrix(), 4,285)
coinObj[10].placeItem(gridObj.getMatrix(), 12,315)
coinObj[11].placeItem(gridObj.getMatrix(), 20,345)
coinObj[12].placeItem(gridObj.getMatrix(), 8,375)
coinObj[13].placeItem(gridObj.getMatrix(), 4,405)
coinObj[14].placeItem(gridObj.getMatrix(), 20,405)
coinObj[15].placeItem(gridObj.getMatrix(), 16,440)

addSpeedUps()

T = time.time()

configObj = Configure()


speedfactor = 1
configObj.setStart(0)
gravity = 0.5

def incrementSpeed():
    global speedfactor
    speedfactor = speedfactor + 1

def resetSpeed():
    global speedfactor
    speedfactor = 1


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
        if mandalorianObj.daye(configObj.getStart()):
            mandalorianObj.removeDin(gridObj.getMatrix())
            if mandalorianObj.changeY(speedfactor + 1, gridObj.getMatrix(), configObj, speedupObj) == -1:
                configObj.setStart(0)
                resetSpeed()
                mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                removeSpeedUps()
                reprintCoins()
                reprintLasers()
                addSpeedUps()
                return
            mandalorianObj.setDirection(1)
            mandalorianObj.showDin(gridObj.getMatrix())

    if keyPress == 'a':
        if mandalorianObj.bayehaathkakhel(configObj.getStart()):
            mandalorianObj.removeDin(gridObj.getMatrix())
            if mandalorianObj.changeY(-2, gridObj.getMatrix(), configObj, speedupObj) == -1:
                configObj.setStart(0)
                resetSpeed()
                mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                removeSpeedUps()
                reprintCoins()
                reprintLasers()
                addSpeedUps()
                return
            mandalorianObj.setDirection(0)
            mandalorianObj.showDin(gridObj.getMatrix())
    
    if keyPress == 'w':
        if mandalorianObj.upupandaway():
            mandalorianObj.removeDin(gridObj.getMatrix())
            mandalorianObj.setAirTime(0) 
            if mandalorianObj.changeX(-1, gridObj.getMatrix(), configObj, speedupObj) == -1:
                configObj.setStart(0)
                resetSpeed()
                mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                removeSpeedUps()
                reprintCoins()
                reprintLasers()
                addSpeedUps()
                return
            mandalorianObj.changeHeightAir(1)
            mandalorianObj.showDin(gridObj.getMatrix())
    
    if keyPress == 'q':
        quit()
    
    if keyPress == 's':
        bulletObj = Bullet(mandalorianObj.getX(), mandalorianObj.getY())

    if keyPress == " ":
        pass
           
while True: 
    
    move(2,0)
    print("Time Remaining:", end = '\t \t')
    print("Lives:", configObj.getLives(), end = '\t \t')
    print("Coins:", configObj.getCoins(), end = '\t \t')
    print ("Enemy Lives:", end = '\t \t')
    print("Shield:")

    if (configObj.getStart() + 100) < 500:
        configObj.changeStart(speedfactor)
    
    move(5,0)
    for k in range(2):
        if speedupObj[k].showItem(gridObj.getMatrix(), mandalorianObj) == 1:
            incrementSpeed()

    gridObj.printView(configObj.getStart())
    moveDin()
    
    '''Gravity'''
    if mandalorianObj.getAirHeight() > 0: 
        distance = int (0.5 * gravity * (mandalorianObj.getAirTime()))
        if mandalorianObj.limbolow(distance) == 1:
            mandalorianObj.changeHeightAir(-distance)
            mandalorianObj.removeDin(gridObj.getMatrix())
            for i in range(distance):
                if mandalorianObj.changeX(1, gridObj.getMatrix(), configObj, speedupObj) == -1:
                    configObj.setStart(0)
                    resetSpeed()
                    mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                    removeSpeedUps()
                    reprintCoins()
                    reprintLasers()
                    addSpeedUps()
                    continue
            mandalorianObj.changeX(-distance, gridObj.getMatrix(), configObj, speedupObj)
            if mandalorianObj.changeX(distance, gridObj.getMatrix(), configObj, speedupObj) == -1:
                configObj.setStart(0)
                resetSpeed()
                mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                removeSpeedUps()
                reprintCoins()
                reprintLasers()
                addSpeedUps()
                continue
            mandalorianObj.showDin(gridObj.getMatrix())
        elif mandalorianObj.limbolow(distance) == -1:
            while mandalorianObj.getX() < 25:
                mandalorianObj.changeHeightAir(-1)
                mandalorianObj.removeDin(gridObj.getMatrix())
                if mandalorianObj.changeX(1, gridObj.getMatrix(), configObj, speedupObj) == -1:
                    configObj.setStart(0)
                    resetSpeed()
                    mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                    removeSpeedUps()
                    reprintCoins()
                    reprintLasers()
                    addSpeedUps()
                    continue
                mandalorianObj.showDin(gridObj.getMatrix())

    if (mandalorianObj.getY() - 1) < configObj.getStart():
        mandalorianObj.removeDin(gridObj.getMatrix())
        if mandalorianObj.changeY(speedfactor, gridObj.getMatrix(), configObj, speedupObj) == -1:
            configObj.setStart(0)
            resetSpeed()
            mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
            removeSpeedUps()
            reprintCoins()
            reprintLasers()
            addSpeedUps()
            continue
        mandalorianObj.showDin(gridObj.getMatrix())

    if (mandalorianObj.getY() + 1) > (configObj.getStart() + 100):
        mandalorianObj.removeDin(gridObj.getMatrix())
        if mandalorianObj.changeY(-1, gridObj.getMatrix(), configObj, speedupObj) == -1:
            configObj.setStart(0)
            resetSpeed()
            mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
            removeSpeedUps()
            reprintCoins()
            reprintLasers()
            addSpeedUps()
            continue
        mandalorianObj.showDin(gridObj.getMatrix())