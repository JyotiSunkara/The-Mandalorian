from colorama import Fore, Back, Style
import numpy

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
        self._allowedCollision = [" ", "o"]
        self._dead = 0
        self._killed = False
        self._heightAir = 0
        self._airTime = 0
        self._shield = 0
        self._shieldMatrix = numpy.array([  (" ", " ", " ", " ", "=", " ", " ", " ", " "),              
                                            (" ", " ", " ", "=", " ", "=", " ", " ", " "),      
                                            (" ", " ", "=", " ", " ", " ", "=", " ", " "),    
                                            (" ", " ", "=", " ", " ", " ", "=", " ", " "),  
                                            (" ", " ", "=", " ", " ", " ", "=", " ", " "),  
                                            (" ", " ", " ", "=", " ", "=", " ", " ", " "),      
                                            (" ", " ", " ", " ", "=", " ", " ", " ", " "),
                                        ])
    
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

    def changeHeightAir(self, changeVal):
        self._heightAir = self._heightAir + changeVal

    def changeX(self, changeVal, grid, configObj, powerupSpeed):
        
        self._x = self._x + changeVal
        for i in range(self._x, self._x + 3):
            for j in range(self._y, self._y + 3):
                if grid[i,j] == "o":
                    configObj.incrementCoins()
                elif grid[i,j] == "0":
                    configObj.decrementLives()
                    configObj.restart()
                    return -1
        return 0

    
    def changeY(self, changeVal, grid, configObj, powerupSpeed):

        self._y = self._y + changeVal
        for i in range(self._x, self._x + 3):
            for j in range(self._y, self._y + 3):
                if grid[i,j] == "o":
                    configObj.incrementCoins()
                elif grid[i,j] == "0":
                    configObj.decrementLives()
                    configObj.restart()
                    return -1        
        return 0


    def incrementAirTime(self):
        self._airTime = self._airTime + 1

    def placeDin(self, grid, x, y, direction):
        '''Place the Mandalorian: Din on the grid at given position of top left of the character'''
        self._x = x
        self._y = y
        self._direction = direction
        grid[self._x:self._x+3, self._y:self._y+3] = self._dinRight
       
    def removeDin(self, grid):
        grid[self._x:self._x+3, self._y:self._y+3] = " "

    def showDin(self, grid):
        if self._shield == 1:
            grid[self._x: self._x -3, self._y: self._y: self._y - 3] = self._shield
        if self._direction == 1:
            grid[self._x:self._x+3, self._y:self._y+3] = self._dinRight
        else:
            grid[self._x:self._x+3, self._y:self._y+3] = self._dinLeft

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
        elif self._y + 5 == 499:
            return 0
        else:
            return 1
    
