"""
single responsibility principle.

    *  the class should have only one single primary responsibility
       and not take on many responsibilities
    *  there should be only one reason to change a class
    *  don't have the class do too much
    *  don't overload the classes responsibilities
    *  don't make a GOD class, tries to do everything
"""


class Journal:
    """Just have journal add journal entries nothing else."""

    def __init__(self):
        """Init entries."""
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        """Add journal entry."""
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        """Remove journal entry."""
        del self.entries[pos]

    def __str__(self):
        """Show string rep of journal."""
        return '\n'.join(self.entries)

    # dont give your class additonal responsibilities
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


# assign the handling of persistence to a seperate class
class PersistenceManager:
    """Take out the job of saving journals to this class."""

    @staticmethod
    def save_to_file(journal, filename):
        """Save journal to file."""
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


# this just focus on journal entries
j = Journal()
j.add_entry("I cried today")
j.add_entry("I wwas happy today")
print(j)

# this focust on persisting
file = r'./test.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as f:
    print(f.read())
