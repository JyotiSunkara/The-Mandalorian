from colorama import Fore

import random
import numpy

from grid import Grid

'''This class puts the ground and sky boundaries and walls onto the grid'''
class Scenery:
    def __init__(self):
        self._sky = Fore.BLUE + "_" + Fore.RESET
        self._ground = Fore.LIGHTMAGENTA_EX + "_" + Fore.RESET


    def createGround(self, grid):
        grid[28, 0:500] = self._ground
        
    def createSky(self, grid):
        grid[0, 0:500] = self._sky
        
