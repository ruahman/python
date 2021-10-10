"""
You should be able to use a drived class anywhere the base class is used.

* when you drive a class make sure you don't break anything.
* where ever they are using your base class they should use the newly
  created drived class.
* drived classes should not break area where base class is being used.
"""


class Rectangle:
    """Rectangle object with width, height properties."""

    def __init__(self, width, height):
        """Initialize width and height."""
        self._width = width
        self._height = height

    @property
    def area(self):
        """Retrun area."""
        return self._width * self._height

    @property
    def width(self):
        """Get width."""
        return self._width

    @width.setter
    def width(self, value):
        """Set width."""
        self._width = value

    @property
    def height(self):
        """Get width."""
        return self._height

    @height.setter
    def height(self, value):
        """Set height."""
        self._height = value

    def __str__(self):
        """Show width, height, area."""
        return f"""width: {self._width},
                   height: {self._height},
                   area: {self.area}"""


class Square(Rectangle):
    """Drived from rectangle."""

    def __init__(self, size):
        """Initialize both width and height to same."""
        Rectangle.__init__(self, size, size)

    # volates liskov, break areas of code where base class is used
    @Rectangle.width.setter
    def width(self, value):
        """Set width and height."""
        self._width = value
        self._height = value

    # violoates liskov, break areas of code where base class is used
    @Rectangle.height.setter
    def height(self, value):
        """Set both width and height."""
        self._width = value
        self._height = value


def set_dimentions(rc, width, height):
    """Set the dimentions then look at area."""
    rc.width = width
    rc.height = height
    print(rc.area)


if __name__ == '__main__':
    rc = Rectangle(5, 7)
    set_dimentions(rc, 10, 10)

    # this breaks be cause we did not respect liskov principle
    sq = Square(100)
    set_dimentions(sq, 2, 3)
