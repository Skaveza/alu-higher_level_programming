#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class defines the blueprint for a Square object """
    def __init__(self, size, x=0, y=0, id=None):
        """ This func initializes a Square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The string representation of a Square object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Returns the size [width / height] of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size [width / height] of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of a Square object attributes"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                else:
                    setattr(self, key, value)


if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    s1.update(10)
    print(s1)
    s1.update(1, 2)
    print(s1)
    s1.update(1, 2, 3)
    print(s1)
    s1.update(1, 2, 3, 4)
    print(s1)
    s1.update(x=12)
    print(s1)
    s1.update(size=7, y=1)
    print(s1)
    s1.update(size=7, id=89, y=1)
    print(s1)

