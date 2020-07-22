from colorama import Fore, Back, Style
import numpy
import random
import os
dragon=[list("_<>=======()                            "),
        list("(/ \___   /|\\\\          ()==========<>_ "),
        list("       \_/ | \\\\        //|\   ______/ \)"),
        list("         \_|  \\\\      // | \_/          "),
        list("           \|\/|\_   //  /\/            "),
        list("            (oo)\ \_//  /               "),
        list("           //_/\_\/ /  |                "), 
        list("          @@/  |=\  \  |                "),
        list("                \_=\_\ |                "),
        list("                 \==\ \|\_              "),
        list("                 (\==\(  )\             "),
        list("             (((~) __(_/   |            "),
        list("                 (((~) \  /             "),
        list("                 ______/ /              "),
        list("                /_______/               ")]

class Dragon():
    def __init__(self):
        self._x = 0
        self._y = 0
        self._height = len(dragon)
        self._width = len(dragon[0])
        self._matrix = [] 
        self._alive = True
        
    def placeItem(self, grid, x, y):
        self._x = x
        self._y = y
        
        for i in range(self._x, self._x + len(dragon)):
            for j in range(self._y, self._y + len(dragon[0])):
                randomCol = random.randint(0,1)
                if randomCol == 1:
                    grid[i][j] = Fore.RED + dragon[i - self._x][j - self._y] + Fore.RESET
                else:
                    grid[i][j] = Fore.GREEN + dragon[i - self._x][j - self._y] + Fore.RESET
    
    def showItem(self, grid):
         for i in range(self._x, self._x + len(dragon)):
            for j in range(self._y, self._y + len(dragon[0])):
                randomCol = random.randint(0,1)
                if randomCol == 1:
                    grid[i][j] = Fore.RED + dragon[i - self._x][j - self._y] + Fore.RESET
                else:
                    grid[i][j] = Fore.GREEN + dragon[i - self._x][j - self._y] + Fore.RESET
    

    def changeY(self, grid, din):
        if din.getX() < 29 - len(dragon):
            self._x = din.getX()
    
    def removeItem(self, grid):
         for i in range(self._x, self._x + len(dragon)):
            for j in range(self._y, self._y + len(dragon[0])):
                grid[i][j] = " "

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getHeight(self):
        return self._height
    
    def getWidth(self):
        return self._width

class IceBall():
    def __init__(self):
        self._x = 0
        self._y = 459
        self._ball = numpy.array([("*",Fore.BLUE + "^"+Fore.RESET, "*"),
                                  (Fore.BLUE + "<" + Fore.RESET," ",Fore.BLUE + ">" + Fore.RESET),
                                  ("*",Fore.BLUE + "V" + Fore.RESET, "*")
        ])
        self._alive = 1
        self._placed = 0
        self._yInit = 459

    def placeItem(self, grid, x, y):
        if self._placed == 0:
            self._x = x 
            self._y = y - 3 
            if self._alive == 1:
                grid[self._x: self._x + 3, self._y: self._y + 3] = self._ball
                self._placed = 1
                os.system("aplay -q ./music/Ice.wav &")

        else:
            if self._alive == 1:
                grid[self._x: self._x + 3, self._y: self._y + 3] = self._ball

     
    def changeY(self,grid, din, config, shieldObj):
        if self._alive == 1:
            if self._y - 1 < self._yInit - 40:
                self._alive = 0
                self.removeItem(grid)
                return
            else:
                self._y = self._y - 1
                for i in range(self._x, self._x + 3):
                    for j in range(self._y, self._y + 3):
                        if grid[i, j] in din.getMatrix() and grid[i, j] != " ":
                            if shieldObj.getShield() == 0:
                                config.decrementLives()
                                self._alive = 0
    def removeItem(self,grid):
        if self._alive == 1:
            grid[self._x: self._x + 3, self._y: self._y + 3] = " "

    def showItem(self, grid):
        if self._alive == 1:
            for i in range(self._x, self._x + 3):
                for j in range(self._y, self._y + 3):
                    if grid[i,j] == Fore.GREEN + "o"+ Fore.RESET:
                        return
             
            grid[self._x:self._x + 3, self._y:self._y + 3] = self._ball  
            self._placed = 1
    
    def getPlaced(self):
        return self._placed

       	