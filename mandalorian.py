from colorama import Fore, Back, Style
import numpy
import os

powerMatrix = numpy.array([("<","i","a","m","s","p","e","e","d",">")])
class Din:
    '''This class defines the Mandalorian Din and helps him move around, 
    obtaining powerups, collection coins and checking collisions
    '''
    def __init__(self, x, y, direction):
        self._x = x
        self._y = y
        self._direction = direction
        self._dinRight = numpy.array([ (" "," ",  "O"), 
                                       ("(", "]", "\\"), 
                                       (" ", "|", "|") ])
        self._dinLeft = numpy.array([ ("O", " ", " "), ("/", "[",")"), ("|", "|"," ") ])
        self._lives = 5
        self._killed = False
        self._heightAir = 0
        self._airTime = 0
        self._dragonMode = 0
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y

    def getAirHeight(self):
        return self._heightAir
    
    def getAirTime(self):
        return self._airTime

    def getRight(self):
        return self._dinRight

    def getLeft(self):
        return self._dinLeft

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y
      
    def setDirection(self, direction):
        self._direction = direction
    
    def setAirTime(self, airTime):
        self._airTime = airTime

    def setShield(self, value):
        self._shield = value

    def changeHeightAir(self, changeVal):
        self._heightAir = self._heightAir + changeVal

    def changeX(self, changeVal, grid, configObj, powerupSpeed, shield):
        
        self._x = self._x + changeVal
        if self._dragonMode == 0:
            if shield.getShield() == False:
                for i in range(self._x, self._x + 3):
                    for j in range(self._y, self._y + 3):
                        if grid[i,j] == Fore.GREEN + "o" + Fore.RESET:
                            configObj.incrementCoins()
                        elif grid[i,j] == Fore.RED + "0" +Fore.RESET:
                            configObj.decrementLives()
                            configObj.restart()
                            return -1
            else:
                for i in range(self._x, self._x + 3):
                    for j in range(self._y - 2, self._y + 5):
                        if grid[i,j] == Fore.GREEN + "o" + Fore.RESET:
                            configObj.incrementCoins()

        return 0

    
    def changeY(self, changeVal, grid, configObj, powerupSpeed, shield):

        self._y = self._y + changeVal
        if self._dragonMode == 0:
            if shield.getShield() == False:
                for i in range(self._x, self._x + 3):
                    for j in range(self._y, self._y + 3):
                        if grid[i,j] == Fore.GREEN + "o" + Fore.RESET:
                            configObj.incrementCoins()
                        elif grid[i,j] == Fore.RED + "0" +Fore.RESET:
                            configObj.decrementLives()
                            configObj.restart()
                            return -1   
            else:
                for i in range(self._x, self._x + 3):
                    for j in range(self._y - 2, self._y + 5):
                        if grid[i,j] == Fore.GREEN + "o" + Fore.RESET:
                            configObj.incrementCoins()
        return 0


    def incrementAirTime(self):
        self._airTime = self._airTime + 1

    def placeDin(self, grid, x, y, direction):
        '''Place the Mandalorian: Din on the grid at given position of top left of the character'''
        self._x = x
        self._y = y
        if self._dragonMode == 0:
            self._direction = direction
            grid[self._x:self._x+3, self._y:self._y+3] = self._dinRight
       
    def removeDin(self, grid):
        grid[self._x:self._x+3, self._y:self._y+3] = " "

    def showDin(self, grid):
        if self._direction == 1:
            grid[self._x:self._x+3, self._y:self._y+3] = self._dinRight
        else:
            grid[self._x:self._x+3, self._y:self._y+3] = self._dinLeft
    
    def getMatrix(self):
        if self._direction == 1:
            return self._dinRight
        else:
            return self._dinLeft

    def upupandaway(self):
        if self._x == 1:
            return 0
        else:
            return 1

    def limbolow(self, distance):
        if self._x == 25:
            self._airTime = 0
            return 0
        elif (self._x + distance) > 25:
            return -1
        else:
            return 1
    
    def bayehaathkakhel(self, start):
        if self._y - 2 < start:
            return 0
        else:
            return 1
    
    def daye(self, start):
        if self._y + 5 > (start + 100):
            return 0
        elif self._y + 5 > 456:
            return 0
        else:
            return 1
    
class Shield():
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._enable = False
        self._matrix = numpy.array([(Back.CYAN + " " + Back.RESET,Back.CYAN + " " + Back.RESET, " ", " ", " ", Back.CYAN + " " + Back.RESET, Back.CYAN + " " + Back.RESET ),    
                                    (Back.CYAN + " " + Back.RESET, Back.CYAN + " " + Back.RESET, " ", " ", " ", Back.CYAN + " " + Back.RESET, Back.CYAN + " " + Back.RESET),  
                                    (Back.CYAN + " " + Back.RESET, Back.CYAN + " " + Back.RESET, " ", " ", " ", Back.CYAN + " " + Back.RESET, Back.CYAN + " " + Back.RESET)  
                                   ])
        self._height = 3
        self._width = 7
        self._endTime = 0
        self._shieldWait = 0
        
    def showShield(self, grid, dinX, dinY):
        if self._enable == True:
            self._x = dinX 
            self._y = dinY - 2
            grid[self._x:self._x + self._height, self._y:self._y + self._width] = self._matrix

    def removeShield(self, grid):
        if self._enable == True:
            grid[self._x:self._x + self._height, self._y:self._y + self._width] = " "

    def setEnd(self, value):
        self._endTime = value
        
    def getEnd(self):
        return self._endTime

    def enableShield(self):
        self._enable = True

    def disableShield(self):
        self._enable = False
    
    def getShield(self):
        return self._enable

    def getWait(self):
        return self._shieldWait
    
    def changeWait(self, value):
        self._shieldWait = self._shieldWait + value
    
    def setWait(self, value):
        self._shieldWait = value

class Bullet():
    def __init__(self, x, y):
        self._xInit = x + 1
        self._yInit = y
        self._x = x + 1
        self._y = y
        self._bulletMatrix = numpy.array([(Fore.MAGENTA + "o" + Fore.RESET, Fore.LIGHTRED_EX + ">" + Fore.RESET)])
        self._alive = 1
        self._placed = 0

    def showBullet(self, grid):
        if self._alive == 1:
            for i in range(self._x, self._x +1):
                for j in range(self._y, self._y + 2):
                    if grid[i,j] == Fore.GREEN + "o" + Fore.RESET:
                        return
             
            grid[self._x:self._x + 1, self._y:self._y + 2] = self._bulletMatrix  
            self._placed = 1

    def removeBullet(self, grid):
        if self._placed == 1:
            grid[self._x:self._x + 1, self._y:self._y + 2] = " "
    
    def changeY(self, grid, speedfactor, laserObj, dragonObj, configObj):
        if self._alive == 1:
            if self._y > self._yInit + 50:
                self.removeBullet(grid)
                self._alive = 0
                return
            elif self._y + speedfactor > 498:
                return
            else:
                self._y = self._y + speedfactor
                self._placed = 0

                for laser in laserObj:
                    if self._y in range(laser.getY(), laser.getY() + laser.getWidth()):
                        if self._x in range(laser.getX(), laser.getX() + laser.getHeight()):
                            if Fore.RED + "0" +Fore.RESET in grid[self._x: self._x + 1, self._y: self._y + 2]:
                                laser.removeItem(grid)
                                laser.setAlive(0)
                                os.system("aplay -q ./music/LaserDead.wav &")
                if self._y in range(dragonObj.getY(), dragonObj.getY() + dragonObj.getWidth()):
                    if self._x in range(dragonObj.getX(), dragonObj.getX() + dragonObj.getHeight()):
                        if " " not in grid[self._x: self._x + 1, self._y: self._y + 2]:
                            configObj.enemyLoss()
                            self.removeBullet(grid)
                            self._alive = 0

    def getPlaced(self):
        return self._placed
