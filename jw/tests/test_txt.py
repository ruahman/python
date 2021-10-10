import ipdb
import jw.txt
import jw.csv


def test_extract_data():
    ipdb.set_trace()
    # items = jw.txt.extract_data('data/txt/arecibo-a.txt')
    # items = jw.txt.extract_data('data/txt/arecibo-b.txt')
    # QUEBRADILLAS TELEPHONE	TERRITORY	C
    items = jw.txt.extract_data(
        'data/txt/quebradillas-c.txt', r'^QUEBRADILLAS\sTELEPHONE\sTERRITORY')

    # for item in items:
    #     print(item)
    # jw.csv.print_csv(items, 'data/csv/arecibo-a-import.csv', 'Arecibo')
    # jw.csv.print_csv(items, 'data/csv/arecibo-b.csv', 'arecibo-b')
    jw.csv.print_csv(items, 'data/csv/quebradillas-c.csv', 'quebradillas-c')
