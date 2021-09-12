""" Script to run jw scrapper. """

import jw

if __name__ == '__main__':
    jw.run('./data/html/quebradillas-1.html',
           './data/csv/quebradillas_1.csv',
           './data/pdf/quebradillas_1.pdf')

    jw.run('./data/html/quebradillas-2.html',
           './data/csv/quebradillas_2.csv',
           './data/pdf/quebradillas_2.pdf')
