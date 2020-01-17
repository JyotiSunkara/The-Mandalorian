from colorama import Fore, Back, Style
import numpy

class Item:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y
        self.__matrix = numpy.empty([breadth, height])
    
    def changeY(self, changeVal):
        self.__y = self.__y + changeVal

    def changeX(self, changeVal):
        self.__x = self.__x + changeVal
    
    def getX(self):
        return __x
    
    def getY(self):
        return __y
    
    
class Bullet(Item):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.matrix = numpy.array(["*"])

    
        