# import ipdb
# from src.jw import pdf
import pytest
from jw.csv import get_items_from_csv
from jw.pdf import make_pdf_from_items


@pytest.mark.csv
@pytest.mark.parametrize("params", [
    (r'./data/csv/import/arecibo/arecibo-a.csv',
     r'./data/pdf/export/arecibo/arecibo-a.pdf',
     'Arecibo-A'),
    (r'./data/csv/import/arecibo/arecibo-b.csv',
     r'./data/pdf/export/arecibo/arecibo-b.pdf',
     'Arecibo-B'),
    (r'./data/csv/import/arecibo/arecibo-c.csv',
     r'./data/pdf/export/arecibo/arecibo-c.pdf',
     'Arecibo-C'),
    (r'./data/csv/import/arecibo/arecibo-d.csv',
     r'./data/pdf/export/arecibo/arecibo-d.pdf',
     'Arecibo-D'),
    (r'./data/csv/import/arecibo/arecibo-e.csv',
     r'./data/pdf/export/arecibo/arecibo-e.pdf',
     'Arecibo-E'),
    (r'./data/csv/import/arecibo/arecibo-f.csv',
     r'./data/pdf/export/arecibo/arecibo-f.pdf',
     'Arecibo-F'),
    (r'./data/csv/import/arecibo/arecibo-g.csv',
     r'./data/pdf/export/arecibo/arecibo-g.pdf',
     'Arecibo-G'),
    (r'./data/csv/import/arecibo/arecibo-h.csv',
     r'./data/pdf/export/arecibo/arecibo-h.pdf',
     'Arecibo-H'),
    (r'./data/csv/import/arecibo/arecibo-i.csv',
     r'./data/pdf/export/arecibo/arecibo-i.pdf',
     'Arecibo-I'),
    (r'./data/csv/import/arecibo/arecibo-j.csv',
     r'./data/pdf/export/arecibo/arecibo-j.pdf',
     'Arecibo-J'),
    (r'./data/csv/import/arecibo/arecibo-k.csv',
     r'./data/pdf/export/arecibo/arecibo-k.pdf',
     'Arecibo-K'),
    (r'./data/csv/import/arecibo/arecibo-l.csv',
     r'./data/pdf/export/arecibo/arecibo-l.pdf',
     'Arecibo-L'),
    (r'./data/csv/import/arecibo/arecibo-m.csv',
     r'./data/pdf/export/arecibo/arecibo-m.pdf',
     'Arecibo-M'),
    (r'./data/csv/import/arecibo/arecibo-n.csv',
     r'./data/pdf/export/arecibo/arecibo-n.pdf',
     'Arecibo-N'),
    (r'./data/csv/import/arecibo/arecibo-o.csv',
     r'./data/pdf/export/arecibo/arecibo-o.pdf',
     'Arecibo-O'),
    (r'./data/csv/import/arecibo/arecibo-p.csv',
     r'./data/pdf/export/arecibo/arecibo-p.pdf',
     'Arecibo-P'),
    (r'./data/csv/import/arecibo/arecibo-q.csv',
     r'./data/pdf/export/arecibo/arecibo-q.pdf',
     'Arecibo-Q'),
    (r'./data/csv/import/arecibo/arecibo-r.csv',
     r'./data/pdf/export/arecibo/arecibo-r.pdf',
     'Arecibo-R'),
    (r'./data/csv/import/arecibo/arecibo-s.csv',
     r'./data/pdf/export/arecibo/arecibo-s.pdf',
     'Arecibo-S'),
    (r'./data/csv/import/arecibo/arecibo-t.csv',
     r'./data/pdf/export/arecibo/arecibo-t.pdf',
     'Arecibo-T'),
    (r'./data/csv/import/arecibo/arecibo-v.csv',
     r'./data/pdf/export/arecibo/arecibo-v.pdf',
     'Arecibo-V'),
    (r'./data/csv/import/arecibo/arecibo-w.csv',
     r'./data/pdf/export/arecibo/arecibo-w.pdf',
     'Arecibo-W')
])
def test_pdf(params):
    (input, output, title) = params

    items = get_items_from_csv(input)

    print(input)
    print(output)
    print(title)
    print(len(items))

    make_pdf_from_items(items, title, output)


def test_foobar():
    print("this is just a test")
