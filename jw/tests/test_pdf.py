import ipdb
import jw.pdf
import jw.csv


def test_pdf():
    # ipdb.set_trace()
    items = jw.csv.get_items_from_csv('./data/csv/quebradillas_1.csv')
    jw.pdf.make_pdf(items, './data/pdf/quebradillas_group_a_1.pdf',
                    "Quebradillas Group A1")

    items = jw.csv.get_items_from_csv('./data/csv/quebradillas_2.csv')
    jw.pdf.make_pdf(items, './data/pdf/quebradillas_group_a_2.pdf',
                    "Quebradillas Group A2")
