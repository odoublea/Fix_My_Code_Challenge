#!/usr/bin/python3
"""The Square Module"""

class square():
    """A square class"""
    
    def __init__(self, width):
        """Initialize class constructor"""
        try:
            self.width = width
        except Exception as e:
            raise TypeError("width must be an integer")

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        return (self.width * 4)

    def __str__(self):
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
