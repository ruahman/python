""" Script to run jw scrapper. """

import jw

if __name__ == '__main__':
    jw.run('./data/quebradillas-1.html', 'data/quebradillas_1.csv')
    jw.run('./data/quebradillas-2.html', 'data/quebradillas_2.csv')
