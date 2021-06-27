"""
single responsibility principle
    *  the class should have only one single responsibility
    *  there should be only one reason to change a class
    *  don't have the class do too much
"""


class Journal:
    """
    just have journal add journal entries nothing else
    """
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        """
        add journal entrie
        """
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

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
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


# this just focus on journal entries
j = Journal()
j.add_entry("I cried today")
j.add_entry("I wwas happy today")
# print(j)

# this focust on persisting
file = r'./test.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as f:
    print(f.read())
