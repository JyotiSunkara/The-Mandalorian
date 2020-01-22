from colorama import Fore, Back, Style

import random
import numpy

from grid import Grid

'''This class puts the ground and sky boundaries and walls onto the grid'''
class Scenery:
    def __init__(self):
        self._sky = Back.LIGHTMAGENTA_EX + " " + Back.RESET 
        self._ground = Back.LIGHTMAGENTA_EX + " " + Back.RESET


    def createGround(self, grid):
        grid[28:30, 0:500] = self._ground
        
    def createSky(self, grid):
        grid[0, 0:500] = self._sky
        
