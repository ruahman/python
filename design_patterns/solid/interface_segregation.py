"""
Interface segregation principle.

* you don't want to stick too many elements into an interface.
* don't make the cost of implementing the interface high.
* seperate out / segregate into other interfaces so that the cost
  of implementing the interface is lower
"""
from abc import abstractmethod


class Machine:
    """Implement a machine that print, fax and scans."""

    def print(self, document):
        """Not implemented."""
        raise NotImplementedError

    def fax(self, document):
        """Not implemented."""
        raise NotImplementedError

    def scan(self, document):
        """Not implemented."""
        raise NotImplementedError


class Printer:
    """Printer interface."""

    @abstractmethod
    def print(self, document):
        """Abstract method for print document."""
        pass


class Scanner:
    """Scanner interface."""

    @abstractmethod
    def scan(self, document):
        """Abstract method for scan."""
        pass


class MyPrinter(Printer):
    """Implementation of printer."""

    def print(self, document):
        """Print document."""
        print(document)


class Photocopier(Printer, Scanner):
    """Implementation of both printer and scanner."""

    def print(self, document):
        """Print document."""
        print(f"print: {document}")

    def scan(self, document):
        """Scan document."""
        print(f"scan: {document}")


if __name__ == '__main__':
    pc = Photocopier()
    pc.print("test print")
    pc.scan("test scan")
