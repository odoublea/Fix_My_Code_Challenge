#!/usr/bin/python3
""" Square class module """

class Square():
    """ A Square class constructor"""
    
    def __init__(self, width=0, height=0):
        """ Initialize Square"""
        self.width = width
        self.height = height
        # for key, value in kwargs.items():
        #     setattr(self, key, value)
                    
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
