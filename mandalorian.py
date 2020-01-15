from colorama import Fore, Back, Style
import numpy


class Din:
    '''This class defines the Mandalorian Din and helps him move around, 
    obtaining powerups, collection coins and checking collisions
    '''
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self._dinRight = numpy.array([ (" "," ", "O"),("(", "]", "\\"), (" ", "|", "|") ])
        self._dinLeft = numpy.array([ ("O", " ", " "), ("\\", "]","("), ("|", "|"," ") ])
        self.lives = 5
        self.allowedCollision = [" ", "o"]
        self.dead = 0
        self.killed = False

    def placeDin(self, grid):
        '''Place the Mandalorian: Din on the grid at given position of top left of the character'''
        grid[self.x:self.x + 3, self.y:self.y + 3] = self._dinRight
       
    def removeDin(self, grid):
        grid[self.x:self.x + 3, self.y:self.y + 3] = " "

    def showDin(self, grid):
        if self.direction == 1:
            grid[self.x:self.x + 3, self.y:self.y + 3] = self._dinRight
        else:
            grid[self.x:self.x + 3, self.y:self.y + 3] = self._dinLeft
