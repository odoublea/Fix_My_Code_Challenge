#!/usr/bin/python3
""" Square class module """

class Square():
    """ A Square class constructor"""
    
    def __init__(self, *args, **kwargs):
        """ Initialize Square"""
        try:
            if len(args) == 1:
                self.width = self.height = args[0]

            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)
        except:
            pass

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
