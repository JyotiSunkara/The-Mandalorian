from colorama import Fore, Back, Style
import numpy
import random

class Item:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__height = 0
        self.__width = 0

    def changeY(self, changeVal):
        self.__y = self.__y + changeVal

    def changeX(self, changeVal):
        self.__x = self.__x + changeVal
    
    def getX(self):
        return __x
    
    def getY(self):
        return __y
    
    def placeItem(self, grid, x, y):
        pass
    
    
class Bullet(Item):
    def __init__(self, height, width, x, y):
        self.__x = x
        self.__y = y
        self._alive = 1
        
        self._matrix = numpy.array(["o>"])

class Laser(Item):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__height = 0
        self.__width = 0 
        self._choice = 0       

    def placeItem(self, grid, x, y):
        self.__x = x
        self.__y = y
        self._choice = random.randint(0,3)
        if self._choice == 0:
            self._matrix = numpy.array([("0"," ","0"," ","0"," ","0"," ","0"," ","0"," ","0")])
            self.__height = 1
            self.__width = 13

        elif self._choice == 1:
            self._matrix = numpy.array([("0","0","0","0","0","0","0")]).transpose()
            self.__height = 7
            self.__width = 1

        else:
            self._matrix = numpy.array([("0"," "," ", " ", " ", " ", " "),
                                        (" ","0"," ", " ", " ", " ", " "),
                                        (" "," ","0", " ", " ", " ", " "),
                                        (" "," "," ", "0", " ", " ", " "),
                                        (" "," "," ", " ", "0", " ", " "),
                                        (" "," "," ", " ", " ", "0", " "),
                                        (" "," "," ", " ", " ", " ", "0"),
            ])
            self.__height = 7
            self.__width = 7


        grid[x:x+self.__height, y:y+self.__width] = self._matrix
    
    def showItem(self, grid, x, y):
        grid[x:x+self.__height, y:y+self.__width] = self._matrix
    

class Coins(Item):

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__height = 0
        self.__width = 0 
        self._choice = 0

    def showItem(self, grid, x, y):
        grid[x:x+self.__height, y:y+self.__width] = self._matrix
    
    def placeItem(self, grid, x, y):
        self.__x = x
        self.__y = y
        self._choice = random.randint(0,2)
        if self._choice == 0:
            self._matrix = numpy.array([("o"," ","o"," ","o"," ","o"," ","o"),
                                        ("o"," ","o"," ","o"," ","o"," ","o"),
                                        ("o"," ","o"," ","o"," ","o"," ","o")])
            self.__height = 3
            self.__width = 9
        elif self._choice == 1:
            self._matrix = numpy.array([(" ","o"," "," "," ","o"," "),
                                        ("o","o","o","o","o","o","o"),
                                        ("o","o","o","o","o","o","o"),
                                        (" ","o","o","o","o","o"," "),
                                        (" "," ","o","o","o"," "," "),
                                        (" "," "," ","o"," "," "," ")
                                        ])
            self.__height = 6
            self.__width = 7
        elif self._choice == 2:
            self._matrix = numpy.array([(" "," "," ","o"," "," "," "),
                                        (" "," ","o","o","o"," "," "),
                                        (" ","o","o","o","o","o"," "),
                                        ("o","o","o","o","o","o","o"),
                                        (" ","o","o","o","o","o"," "),
                                        (" "," ","o","o","o"," "," "),
                                        (" "," "," ","o"," "," "," "),
                                        ])
            self.__height = 7
            self.__width = 7
        
        grid[x:x + self.__height, y:y + self.__width] = self._matrix

class SpeedUp():
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.__height = 1
        self.__width = 10
        self._matrix = numpy.array([("<","i","a","m","s","p","e","e","d",">")])
        self._gridX = 0
        self._gridY = 0
        self._used = 0
    
    def placeItem(self, grid, x, y):
        self._used = 0
        self._gridX = x
        self._gridY = y        
        if self.gridFree(grid) == 1:
            grid[self._gridX:self._gridX + self.__height, self._gridY:self._gridY + self.__width] = self._matrix
    
    def gridFree(self, grid):
        for i in range(self._gridX, self._gridX + self.__height):
            for j in range(self._gridY, self._gridY + self.__width):
                if grid[i,j] == " ":
                    continue
                else:
                    return False
        return True

    def showItem(self, grid, mando):
        if self._used == 0:
            for i in range(self._gridX, self._gridX + self.__height):
                for j in range(self._gridY, self._gridY + self.__width):
                    if (grid[i,j] in mando.getRight() or grid[i,j] in mando.getRight()) and grid[i,j] != " ":
                        self._used = 1
                        self.removeItem(grid)
                        return 1
            if self.gridFree(grid) == True:
                grid[self._gridX:self._gridX + self.__height, self._gridY:self._gridY + self.__width] = self._matrix
        return 0

    def removeItem(self, grid):
        for i in range(self._gridX, self._gridX + self.__height):
            for j in range(self._gridY, self._gridY + self.__width):
                grid[i,j] = " "  

    def getMatrix(self):
        return self._matrix 

    def getGridX(self):
        return self._gridX
    
    def getGridY(self):
        return self._gridY