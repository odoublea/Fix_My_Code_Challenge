#!/usr/bin/python3
""" Square class module """

class Square():
    """ A Square class constructor"""
    
    def __init__(self, *args, **kwargs):
        """ Initialize Square"""
        for key, value in kwargs.items():
            setattr(self, key, value)
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def height(self, height):
        self.__height = height
                    
    def area_of_my_Square(self):
        """ Area of the Square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Perimeter of the Square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of the Square """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_Square())
    print(s.PermiterOfMySquare())
