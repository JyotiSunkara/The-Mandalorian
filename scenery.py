from colorama import Fore

import random
import numpy

from grid import Grid

'''This class puts the ground and sky boundaries onto the grid'''
class Scenery:
    def __init__(self):
        self.sky = Fore.BLUE + "_" + Fore.RESET
        self.ground = Fore.YELLOW + "_" + Fore.RESET

    def createGround(self, grid):
        grid[28, 0:500] = self.ground
        
    def createSky(self, grid):
            grid[0, 0:500] = self.sky
        
