"""
Dependency Inversion principle.

* Work with abstractions/interfaces not implementations.
* work with interfaces not implementations
* do not depend on the internal implementation of the class,
  instread work with an interface that class provides you.
"""
from enum import Enum
from abc import abstractmethod


class Relationship(Enum):
    """Relationships between persons."""

    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    """Person object."""

    def __init__(self, name):
        """Set name."""
        self.name = name


class RelationshipsBrowser:
    """Interface for browsing relationships."""

    @abstractmethod
    def find_all_children_of(self, name):
        """Abstract method for traversing relationships."""
        pass


class Relationships(RelationshipsBrowser):
    """Keeps track of relations between persons."""

    def __init__(self):
        """Initialize relations."""
        self.relations = []

    def add_parent_and_child(self, parent, child):
        """Add a relationship."""
        self.relations.append(
            (parent, Relationship.PARENT, child)
        ),
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        """Interface for relationships."""
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2]


class Research:
    """Research class."""

    # def __init__(self, relationships):
    #     # are interacting with the implementation of the class,
    #     # rather than using an interface
    #     # relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f"John has a child called {r[2].name}")

    def __init__(self, browser):
        """Travers throw object."""
        # use an interface to interact with relationships
        for p in browser.find_all_children_of('John'):
            print(p.name)


if __name__ == '__main__':
    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    research = Research(relationships)
