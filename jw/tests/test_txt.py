import ipdb
import jw.txt
import jw.csv


def test_extract_data():
    ipdb.set_trace()
    items = jw.txt.extract_data('data/txt/arecibo-a.txt')
    jw.csv.print_csv(items, 'data/csv/arecibo-a.csv', 4)
