#!/usr/bin/python3
""" Fix Square class module """


class square():
    """ Square class declaration """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Constructor function
        args
        kwargs
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Calculate Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Calculate Permiter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Main function Call, if its running in terminal"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
