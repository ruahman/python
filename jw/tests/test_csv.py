import ipdb
import jw.csv


def test_get_items_from_csv():
    # ipdb.set_trace()
    items = jw.csv.get_items_from_csv('./data/csv/quebradillas_1.csv')
    print(items)
    assert len(items) > 0
