import ipdb
import jw.pdf
import jw.csv


def test_pdf():
    # ipdb.set_trace()
    items = jw.csv.get_items_from_csv('./data/csv/quebradillas_1.csv')
    jw.pdf.make_pdf(items, './data/pdf/test.pdf')

    items = jw.csv.get_items_from_csv('./data/csv/quebradillas_2.csv')
    jw.pdf.make_pdf(items, './data/pdf/test2.pdf')
