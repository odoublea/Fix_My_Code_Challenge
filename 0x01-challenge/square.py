#!/usr/bin/python3
"""A module for the Square class"""

class Square():
    """ Square class """
    
    def __init__(self, width):
        """ Initialize the square class """
        self.width = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of the square"""
        return (self.width * 4)

    def __str__(self):
        """ String representation of the square"""
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
