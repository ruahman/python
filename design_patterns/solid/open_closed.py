"""
Open closed principle.

* when you add functionality, you add via extention, not modification
* open for extention but closed for modification
* it's better to extend a class then modify an implementation.
* when you need more criteria you extend a class.
"""

from enum import Enum


class Color(Enum):
    """Color to product."""

    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    """Size of product."""

    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    """Product."""

    def __init__(self, name, color, size):
        """Initialize name, color and size."""
        self.name = name
        self.color = color
        self.size = size

# Specification


class Specification:
    """
    Base class for seting up specification for filter.

    That way we don't need to keep on making a new filter method.
    """

    def is_satisfied(self, item):
        """Check if item satisfies condition."""
        pass

    def __and__(self, other):
        """Combine specifications."""
        return AndSpecification(self, other)


class Filter:
    """Base class for implenting filters."""

    def filter(self, items, spec):
        """Filter item according to spec."""
        pass


class ColorSpecification(Specification):
    """Specify according to color."""

    def __init__(self, color):
        """Initialize color."""
        self.color = color

    def is_satisfied(self, item):
        """Check if item satisfies color spec."""
        return item.color == self.color


class SizeSpecification(Specification):
    """Implement spec by size."""

    def __init__(self, size):
        """Initialize size to check."""
        self.size = size

    def is_satisfied(self, item):
        """Check to see if item satisfies size."""
        return item.size == self.size


class AndSpecification(Specification):
    """Combibines specifications."""

    def __init__(self, *args):
        """Get list of specifications."""
        self.args = args

    def is_satisfied(self, item):
        """Loop through list to see if all specs are satisfied."""
        return all(map(
            lambda spec: spec.is_satisfied(item),
            self.args
        ))


class BetterFilter(Filter):
    """Implementation of filter."""

    def filter(self, items, spec):
        """Filter items base on spec."""
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)
    items = [apple, tree, house]

    bf = BetterFilter()

    green = ColorSpecification(Color.GREEN)
    for item in bf.filter(items, green):
        print(f"{item.name}")

    large = SizeSpecification(Size.LARGE)
    for item in bf.filter(items, large):
        print(f"{item.name}")

    # largeAndBlue = AndSpecification(large, ColorSpecification(Color.BLUE))
    largeAndBlue = large & ColorSpecification(Color.BLUE)
    for item in bf.filter(items, largeAndBlue):
        print(f"{item.name}")
