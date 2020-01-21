import signal
import os
import time
import numpy
import random
from colorama import init
init()

def move (y, x):
    print("\033[%d;%dH" % (y, x))

from mandalorian import Din, Shield, Bullet
from scenery import Scenery
from grid import Grid
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from items import Item, Laser, Coins, SpeedUp, Magnet
from configure import Configure


gridObj = Grid(30, 500)

mandalorianObj = Din(25, 10, 1)
mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
shieldObj = Shield(0, 0)

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

magnetObj = Magnet(5,60)


def speedUps():
    for i in range(2):
        speedupObj[i].placeItem(gridObj.getMatrix(), random.randint(5,20), random.randint(100,300))
    if magnetObj.gridFree(gridObj.getMatrix(), random.randint(5,10), random.randint(100,400)):
        magnetObj.placeItem(gridObj.getMatrix())

def removespeedUps():
    for i in range(2):
        speedupObj[i].removeItem(gridObj.getMatrix())   
    magnetObj.removeItem(gridObj.getMatrix())
     
inRange = False
bulletObj = []

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

speedUps()




T = time.time()

configObj = Configure()

speedfactor = 1
configObj.setStart(0)
gravity = 0.5
remainingTime = 0

def incrementSpeed():
    global speedfactor
    speedfactor = speedfactor + 1

def resetSpeed():
    global speedfactor
    speedfactor = 1


def moveDin():

    global remainingTime
    global placed
    global inRange

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
	
    if mandalorianObj.getAirHeight() > 0 and inRange == False:
        mandalorianObj.incrementAirTime()
    
    if shieldObj.getEnd() == configObj.getTime():
        shieldObj.removeShield(gridObj.getMatrix())
        shieldObj.disableShield()
        shieldObj.setWait(configObj.getTime() - 60)
        reprintLasers()
        
        mandalorianObj.showDin(gridObj.getMatrix())
        remainingTime = configObj.getTime() - shieldObj.getWait()

    if shieldObj.getWait() == configObj.getTime():
        shieldObj.setWait(0)
        remainingTime = 0
    
    keyPress = user_input()

    if keyPress == 'd':
        if mandalorianObj.daye(configObj.getStart()):
            mandalorianObj.removeDin(gridObj.getMatrix())
            shieldObj.removeShield(gridObj.getMatrix())
            if mandalorianObj.changeY(speedfactor + 1, gridObj.getMatrix(), configObj, speedupObj, shieldObj) == -1:
                configObj.setStart(0)
                for laser in laserObj:
                    laser.setAlive(1)
                resetSpeed()
                mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                removespeedUps()
                reprintCoins()
                reprintLasers()
                speedUps()
                return
            mandalorianObj.setDirection(1)
            shieldObj.showShield(gridObj.getMatrix(), mandalorianObj.getX(), mandalorianObj.getY())
            reprintLasers()
            
            mandalorianObj.showDin(gridObj.getMatrix())
            

    if keyPress == 'a':
        if mandalorianObj.bayehaathkakhel(configObj.getStart()):
            mandalorianObj.removeDin(gridObj.getMatrix())
            shieldObj.removeShield(gridObj.getMatrix())
            if mandalorianObj.changeY(-2, gridObj.getMatrix(), configObj, speedupObj, shieldObj) == -1:
                configObj.setStart(0)
                for laser in laserObj:
                    laser.setAlive(1)
                resetSpeed()
                mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                removespeedUps()
                reprintCoins()
                reprintLasers()
                speedUps()
                return
            mandalorianObj.setDirection(0)
            shieldObj.showShield(gridObj.getMatrix(), mandalorianObj.getX(), mandalorianObj.getY())
            reprintLasers()
            
            mandalorianObj.showDin(gridObj.getMatrix())
            

    
    if keyPress == 'w':
        if mandalorianObj.upupandaway():
            mandalorianObj.removeDin(gridObj.getMatrix())
            shieldObj.removeShield(gridObj.getMatrix())
            mandalorianObj.setAirTime(0) 
            if mandalorianObj.changeX(-1, gridObj.getMatrix(), configObj, speedupObj, shieldObj) == -1:
                configObj.setStart(0)
                for laser in laserObj:
                    laser.setAlive(1)
                resetSpeed()
                mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                removespeedUps()
                reprintCoins()
                reprintLasers()
                speedUps()
                return
            mandalorianObj.changeHeightAir(1)
            shieldObj.showShield(gridObj.getMatrix(), mandalorianObj.getX(), mandalorianObj.getY())
            reprintLasers()
            
            mandalorianObj.showDin(gridObj.getMatrix())
            

    
    if keyPress == 'q':
        quit()
    
    if keyPress == 's':
        bulletObj.append(Bullet(mandalorianObj.getX() - 2, mandalorianObj.getY() + 1))
        
    if keyPress == " ":
        if shieldObj.getWait() == 0:
            shieldObj.enableShield()
            shieldObj.setEnd(configObj.getTime() - 10)
            shieldObj.showShield(gridObj.getMatrix(), mandalorianObj.getX(), mandalorianObj.getY())
            reprintLasers()
            
            mandalorianObj.showDin(gridObj.getMatrix())

    if magnetObj.inRangeMando(gridObj.getMatrix(), mandalorianObj) == True and magnetObj.getPlaced() == 1:
        inRange = True
        moveX = 0
        moveY = 0
        if mandalorianObj.getX() > magnetObj.getX() and mandalorianObj.upupandaway():
            moveX = -1
            mandalorianObj.setAirTime(0) 
            mandalorianObj.changeHeightAir(1)
        elif mandalorianObj.getX() > magnetObj.getX() and mandalorianObj.getX() + 1 < 30:
            moveX = 1
        if mandalorianObj.getY() > magnetObj.getY() and mandalorianObj.bayehaathkakhel(configObj.getStart()):
            moveY = -1
        elif mandalorianObj.getY() < magnetObj.getY() and mandalorianObj.daye(configObj.getStart()):
            moveY = 1

        mandalorianObj.removeDin(gridObj.getMatrix())
        shieldObj.removeShield(gridObj.getMatrix())
        if mandalorianObj.changeX(moveX, gridObj.getMatrix(), configObj, speedupObj, shieldObj) == -1:
                configObj.setStart(0)
                for laser in laserObj:
                    laser.setAlive(1)
                resetSpeed()
                mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                removespeedUps()
                reprintCoins()
                reprintLasers()
                speedUps()
                return
        if mandalorianObj.changeY(moveY, gridObj.getMatrix(), configObj, speedupObj, shieldObj) == -1:
                configObj.setStart(0)
                for laser in laserObj:
                    laser.setAlive(1)
                resetSpeed()
                mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                removespeedUps()
                reprintCoins()
                reprintLasers()
                speedUps()
                return
        shieldObj.showShield(gridObj.getMatrix(), mandalorianObj.getX(), mandalorianObj.getY())
        reprintLasers()
        
        mandalorianObj.showDin(gridObj.getMatrix())
    else:
        inRange = False
        



while True: 
    
    move(2,0)
    configObj.setTime(150 - (round(time.time()) - round(T)))
    print("Time Remaining:", configObj.getTime(), end = '\t \t')
    print("Lives:", configObj.getLives(), end = '\t \t')
    print("Coins:", configObj.getCoins(), end = '\t \t')
    print ("Enemy Lives:", configObj.getEnemyLives(), end = '\t \t')
    if shieldObj.getWait() != 0:
        remainingTime = configObj.getTime() - shieldObj.getWait()
    print("Shield Wait Time:", remainingTime)

    if (configObj.getStart() + 100) < 500:
        if configObj.getStart() + speedfactor + 100 < 500:
            configObj.changeStart(speedfactor)
    
    move(5,0)
    for k in range(2):
        if speedupObj[k].showItem(gridObj.getMatrix(), mandalorianObj) == 1:
            incrementSpeed()

    
    gridObj.printView(configObj.getStart())
    moveDin()
    magnetObj.showItem(gridObj.getMatrix())
    reprintLasers()

    for bullet in bulletObj:
        if bullet.getPlaced()  == 1:
            bullet.removeBullet(gridObj.getMatrix())
        for i in range(5):
            bullet.changeY(gridObj.getMatrix(), 1, laserObj)
        placed = bullet.showBullet(gridObj.getMatrix())


    '''Gravity'''
    if mandalorianObj.getAirHeight() > 0 and inRange == False: 
        distance = int (0.5 * gravity * (mandalorianObj.getAirTime()))
        if mandalorianObj.limbolow(distance) == 1:
            mandalorianObj.changeHeightAir(-distance)
            mandalorianObj.removeDin(gridObj.getMatrix())
            shieldObj.removeShield(gridObj.getMatrix())
            for i in range(distance):
                if mandalorianObj.changeX(1, gridObj.getMatrix(), configObj, speedupObj, shieldObj) == -1:
                    configObj.setStart(0)
                    for laser in laserObj:
                        laser.setAlive(1)
                    resetSpeed()
                    mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                    removespeedUps()
                    reprintCoins()
                    reprintLasers()
                    speedUps()
                    continue
            mandalorianObj.changeX(-distance, gridObj.getMatrix(), configObj, speedupObj, shieldObj)
            if mandalorianObj.changeX(distance, gridObj.getMatrix(), configObj, speedupObj, shieldObj) == -1:
                configObj.setStart(0)
                for laser in laserObj:
                    laser.setAlive(1)
                resetSpeed()
                mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                removespeedUps()
                reprintCoins()
                reprintLasers()
                speedUps()
                continue
            shieldObj.showShield(gridObj.getMatrix(), mandalorianObj.getX(), mandalorianObj.getY())
            reprintLasers()
            
            mandalorianObj.showDin(gridObj.getMatrix())
            

        elif mandalorianObj.limbolow(distance) == -1:
            while mandalorianObj.getX() < 25:
                mandalorianObj.changeHeightAir(-1)
                mandalorianObj.removeDin(gridObj.getMatrix())
                shieldObj.removeShield(gridObj.getMatrix())
                if mandalorianObj.changeX(1, gridObj.getMatrix(), configObj, speedupObj, shieldObj) == -1:
                    configObj.setStart(0)
                    for laser in laserObj:
                        laser.setAlive(1)
                    resetSpeed()
                    mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
                    removespeedUps()
                    reprintCoins()
                    reprintLasers()
                    speedUps()
                    continue
                shieldObj.showShield(gridObj.getMatrix(), mandalorianObj.getX(), mandalorianObj.getY())
                reprintLasers()
                
                mandalorianObj.showDin(gridObj.getMatrix())
                


    if (mandalorianObj.getY() - 1) < configObj.getStart():
        mandalorianObj.removeDin(gridObj.getMatrix())
        shieldObj.removeShield(gridObj.getMatrix())
        if mandalorianObj.changeY(speedfactor, gridObj.getMatrix(), configObj, speedupObj, shieldObj) == -1:
            configObj.setStart(0)
            for laser in laserObj:
                laser.setAlive(1)
            resetSpeed()
            mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
            removespeedUps()
            reprintCoins()
            reprintLasers()
            speedUps()
            continue
        shieldObj.showShield(gridObj.getMatrix(), mandalorianObj.getX(), mandalorianObj.getY())
        reprintLasers()
        
        mandalorianObj.showDin(gridObj.getMatrix())
        


    if (mandalorianObj.getY() + 1) > (configObj.getStart() + 100):
        mandalorianObj.removeDin(gridObj.getMatrix())
        shieldObj.removeShield(gridObj.getMatrix())
        if mandalorianObj.changeY(-1, gridObj.getMatrix(), configObj, speedupObj, shieldObj) == -1:
            configObj.setStart(0)
            for laser in laserObj:
                laser.setAlive(1)
            resetSpeed()
            mandalorianObj.placeDin(gridObj.getMatrix(), 25, 10, 1)
            removespeedUps()
            reprintCoins()
            reprintLasers()
            speedUps()
            continue
        shieldObj.showShield(gridObj.getMatrix(), mandalorianObj.getX(), mandalorianObj.getY())
        reprintLasers()
        
        mandalorianObj.showDin(gridObj.getMatrix())
        

    
    if configObj.getLives() == 0 or configObj.getTime() == 0:
        os.system('clear')
        print("Game Over!")
        quit()