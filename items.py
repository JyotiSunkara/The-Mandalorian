from colorama import Fore, Back, Style
import numpy
import random
import os
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
 
    def placeItem(self, grid, x, y):
        pass

class Laser(Item):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__height = 0
        self.__width = 0 
        self._choice = 0   
        self._alive = 1    

    def placeItem(self, grid, x, y):
        self.__x = x
        self.__y = y
        self._choice = random.randint(0,3)
        if self._choice == 0:
            self._matrix = numpy.array([(Fore.RED + "0" +Fore.RESET , " ",Fore.RED + "0" +Fore.RESET ," ",Fore.RED + "0" +Fore.RESET ," ",Fore.RED + "0" +Fore.RESET ," ",Fore.RED + "0" +Fore.RESET ," ",Fore.RED + "0" +Fore.RESET ," ",Fore.RED + "0" +Fore.RESET )])
            self.__height = 1
            self.__width = 13

        elif self._choice == 1:
            self._matrix = numpy.array([(Fore.RED + "0" +Fore.RESET ,Fore.RED + "0" +Fore.RESET ,Fore.RED + "0" +Fore.RESET ,Fore.RED + "0" +Fore.RESET ,Fore.RED + "0" +Fore.RESET ,Fore.RED + "0" +Fore.RESET ,Fore.RED + "0" +Fore.RESET )]).transpose()
            self.__height = 7
            self.__width = 1

        else:
            self._matrix = numpy.array([(Fore.RED + "0" +Fore.RESET ," "," ", " ", " ", " ", " "),
                                        (" ",Fore.RED + "0" +Fore.RESET ," ", " ", " ", " ", " "),
                                        (" "," ",Fore.RED + "0" +Fore.RESET , " ", " ", " ", " "),
                                        (" "," "," ", Fore.RED + "0" +Fore.RESET , " ", " ", " "),
                                        (" "," "," ", " ", Fore.RED + "0" +Fore.RESET , " ", " "),
                                        (" "," "," ", " ", " ", Fore.RED + "0" +Fore.RESET , " "),
                                        (" "," "," ", " ", " ", " ", Fore.RED + "0" +Fore.RESET ),
            ])
            self.__height = 7
            self.__width = 7


        grid[x:x+self.__height, y:y+self.__width] = self._matrix
    
    def showItem(self, grid, x, y):
        if self._alive == 1:
            grid[x:x+self.__height, y:y+self.__width] = self._matrix
        
    def removeItem(self, grid):
        grid[self.__x:self.__x+self.__height, self.__y:self.__y+self.__width] = " "
    
    def setAlive(self, value):
        self._alive = value

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
       
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    

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
            self._matrix = numpy.array([(Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET),
                                        (Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET),
                                        (Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET," ",Fore.GREEN + "o" + Fore.RESET)])
            self.__height = 3
            self.__width = 9
        elif self._choice == 1:
            self._matrix = numpy.array([(" ",Fore.GREEN + "o" + Fore.RESET," "," "," ",Fore.GREEN + "o" + Fore.RESET," "),
                                        (Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET),
                                        (Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET),
                                        (" ",Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET," "),
                                        (" "," ",Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET," "," "),
                                        (" "," "," ",Fore.GREEN + "o" + Fore.RESET," "," "," ")
                                        ])
            self.__height = 6
            self.__width = 7
        elif self._choice == 2:
            self._matrix = numpy.array([(" "," "," ",Fore.GREEN + "o" + Fore.RESET," "," "," "),
                                        (" "," ",Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET," "," "),
                                        (" ",Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET," "),
                                        (Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET),
                                        (" ",Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET," "),
                                        (" "," ",Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET,Fore.GREEN + "o" + Fore.RESET," "," "),
                                        (" "," "," ",Fore.GREEN + "o" + Fore.RESET," "," "," "),
                                        ])
            self.__height = 7
            self.__width = 7
        
        grid[x:x + self.__height, y:y + self.__width] = self._matrix

class SpeedUp():
    
    def __init__(self, x, y):
        self.__height = 1
        self.__width = 10
        self._matrix = numpy.array([("<","i","a","m","s","p","e","e","d",">")])
        self._x = x
        self._y = y
        self._used = 0
    
    def placeItem(self, grid, x, y):
        self._used = 0
        self._x = x
        self._y = y        
        if self.gridFree(grid) == 1:
            grid[self._x:self._x + self.__height, self._y:self._y + self.__width] = self._matrix
    
    def gridFree(self, grid):
        for i in range(self._x, self._x + self.__height):
            for j in range(self._y, self._y + self.__width):
                if grid[i,j] == " ":
                    continue
                else:
                    return False
        return True

    def showItem(self, grid, mando):
        if self._used == 0:
            for i in range(self._x, self._x + self.__height):
                for j in range(self._y, self._y + self.__width):
                    if (grid[i,j] in mando.getRight() or grid[i,j] in mando.getRight()) and grid[i,j] != " ":
                        os.system("aplay -q ./music/Speed.wav &")
                        self._used = 1
                        self.removeItem(grid)
                        return 1
            if self.gridFree(grid) == True:
                grid[self._x:self._x + self.__height, self._y:self._y + self.__width] = self._matrix
        return 0

    def removeItem(self, grid):
        for i in range(self._x, self._x + self.__height):
            for j in range(self._y, self._y + self.__width):
                grid[i,j] = " "  

    def getMatrix(self):
        return self._matrix 

    def getGridX(self):
        return self._x
    
    def getGridY(self):
        return self._y

class Magnet():
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._matrix = numpy.array([(Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " "+ Back.RESET), 
                                    (Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " "+ Back.RESET), 
                                    (Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET, " ", " ", Back.RED + " " + Back.RESET,  Back.RED + " " + Back.RESET, Back.RED + " " + Back.RESET),
                                    (Back.LIGHTYELLOW_EX + " " + Back.RESET, Back.LIGHTYELLOW_EX + " " + Back.RESET, Back.LIGHTYELLOW_EX + " " + Back.RESET, " ", " ", Back.LIGHTYELLOW_EX + " " + Back.RESET,  Back.LIGHTYELLOW_EX + " " + Back.RESET, Back.LIGHTYELLOW_EX + " " + Back.RESET),
                                    ])
        self.__height = 4
        self.__width = 8
        self._placed = 0

    def placeItem(self, grid):
        if self.gridFree(grid, self._x, self._y) == True:
            grid[self._x:self._x + self.__height, self._y:self._y + self.__width] = self._matrix
            self._placed = 1
    
    def gridFree(self, grid, x, y):
        self._x = x
        self._y = y
        for i in range(self._x, self._x + self.__height):
            for j in range(self._y, self._y + self.__width):
                if grid[i,j] == " ":
                    continue
                else:
                    return False
        return True
        
    def removeItem(self, grid):
        if self._placed == 1:
            for i in range(self._x, self._x + self.__height):
                for j in range(self._y, self._y + self.__width):
                    grid[i,j] = " "  
            self._placed = 0

    def inRangeMando(self, grid, din):
        if abs(din.getX() - self._x) < 30 and abs(din.getY() - self._y) < 30:
            return True
        return False

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    
    def showItem(self, grid): 
        if self._placed == 1:             
            grid[self._x:self._x + self.__height, self._y:self._y + self.__width] = self._matrix
    
    def getPlaced(self):
        return self._placed

                




