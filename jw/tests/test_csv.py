import ipdb
import jw.csv


def test_get_items_from_csv():
    # ipdb.set_trace()
    items = jw.csv.get_items_from_csv('./data/csv/quebradillas_1.csv')
    print(items)
    assert len(items) > 0


def test_create_csv():
    ipdb.set_trace()
    # items = jw.txt.extract_data('data/txt/arecibo-a.txt')
    # items = jw.txt.extract_data('data/txt/arecibo-b.txt')
    items = jw.txt.extract_data(
        'data/txt/quebradillas-c.txt', r'^QUEBRADILLAS\sTELEPHONE\sTERRITORY')

    # for item in items:
    #     print(item)
    # jw.csv.print_csv(items, 'data/csv/arecibo-a-import.csv', 'Arecibo')
    # jw.csv.print_csv(items, 'data/csv/arecibo-b.csv', 'arecibo-b')
    jw.csv.print_csv(items, 'data/csv/quebradillas-c.csv', 'quebradillas-c')
