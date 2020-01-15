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
        self.rows = rows
        self.columns = columns
        self.matrix = numpy.full((self.rows, self.columns), ' ', dtype='<U20')
    
    '''Creates entire grid'''
    # def create_grid(self):
        
    '''Prints the visible portion of the grid and moves it'''
    def printView(self, start):
        for i in range(self.rows):
            for j in range(start, start + 100):     # 150 columns are displayed at a time
                print(self.matrix[i, j], end = '')
            print()
         
    