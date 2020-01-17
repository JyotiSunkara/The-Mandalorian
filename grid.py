import numpy
import time
import signal
import os

from colorama import init
init()

def move (y, x):
    print("\033[%d;%dH" % (y, x))

'''The grid onto which all the characters, obstacles and powerups will be mapped'''
class Grid:

    '''Intialize values'''
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._matrix = numpy.full((self._rows, self._columns), ' ', dtype='<U20')
    
    '''Creates entire grid'''
    # def create_grid(self):

    def getRows(self):
        return self._rows
    
    def getColumns(self):
        return self._columns

    def getMatrix(self):
        return self._matrix
        
    '''Prints the visible portion of the grid and moves it'''
    def printView(self, start):
        for i in range(self._rows):
            for j in range(start, start + 100):     # 100 columns are displayed at a time
                print(self._matrix[i, j], end = '')
            print()

  
         
    