import pytest
import ipdb
import jw.txt
# import jw.csv
from jw.csv import create_csv
from jw import Phone


@pytest.mark.skip
def test_get_items_from_csv():
    # ipdb.set_trace()
    items = jw.csv.get_items_from_csv('./data/csv/quebradillas_1.csv')
    print(items)
    assert len(items) > 0


@pytest.mark.csv
@pytest.mark.parametrize("territory", [
    (r'./data/txt/import/arecibo/arecibo-a.txt'),
    (r'./data/txt/import/arecibo/arecibo-b.txt'),
    (r'./data/txt/import/arecibo/arecibo-c.txt'),
    (r'./data/txt/import/arecibo/arecibo-d.txt'),
    (r'./data/txt/import/arecibo/arecibo-e.txt'),
    (r'./data/txt/import/arecibo/arecibo-f.txt'),
    (r'./data/txt/import/arecibo/arecibo-g.txt'),
    (r'./data/txt/import/arecibo/arecibo-h.txt'),
    (r'./data/txt/import/arecibo/arecibo-i.txt'),
    (r'./data/txt/import/arecibo/arecibo-j.txt'),
    (r'./data/txt/import/arecibo/arecibo-k.txt'),
    (r'./data/txt/import/arecibo/arecibo-l.txt'),
    (r'./data/txt/import/arecibo/arecibo-m.txt'),
    (r'./data/txt/import/arecibo/arecibo-n.txt'),
    (r'./data/txt/import/arecibo/arecibo-o.txt'),
    (r'./data/txt/import/arecibo/arecibo-p.txt'),
    (r'./data/txt/import/arecibo/arecibo-q.txt'),
    (r'./data/txt/import/arecibo/arecibo-r.txt'),
    (r'./data/txt/import/arecibo/arecibo-s.txt'),
    (r'./data/txt/import/arecibo/arecibo-t.txt'),
    (r'./data/txt/import/arecibo/arecibo-v.txt'),
    (r'./data/txt/import/arecibo/arecibo-w.txt'),
    (r'./data/txt/import/arecibo/arecibo-z.txt'),
    (r'./data/txt/import/hatillo/hatillo-a.txt'),
    (r'./data/txt/import/hatillo/hatillo-b.txt'),
    (r'./data/txt/import/hatillo/hatillo-c.txt'),
    (r'./data/txt/import/hatillo/hatillo-d.txt'),
    (r'./data/txt/import/hatillo/hatillo-e.txt'),
    (r'./data/txt/import/hatillo/hatillo-f.txt'),
    (r'./data/txt/import/hatillo/hatillo-g.txt'),
    (r'./data/txt/import/hatillo/hatillo-h.txt'),
    (r'./data/txt/import/hatillo/hatillo-i.txt'),
    (r'./data/txt/import/hatillo/hatillo-j.txt'),
    (r'./data/txt/import/hatillo/hatillo-k.txt'),
    (r'./data/txt/import/hatillo/hatillo-l.txt'),
    (r'./data/txt/import/hatillo/hatillo-m.txt'),
    (r'./data/txt/import/hatillo/hatillo-n.txt'),
    (r'./data/txt/import/hatillo/hatillo-o.txt'),
    (r'./data/txt/import/hatillo/hatillo-p.txt'),
    (r'./data/txt/import/hatillo/hatillo-r.txt'),
    (r'./data/txt/import/hatillo/hatillo-s.txt'),
    (r'./data/txt/import/hatillo/hatillo-t.txt'),
    (r'./data/txt/import/hatillo/hatillo-u.txt'),
    (r'./data/txt/import/hatillo/hatillo-w.txt'),
    (r'./data/txt/import/hatillo/hatillo-x.txt'),
    (r'./data/txt/import/hatillo/hatillo-z.txt'),
    (r'./data/txt/import/camuy/camuy-a.txt'),
    (r'./data/txt/import/camuy/camuy-b.txt'),
    (r'./data/txt/import/camuy/camuy-c.txt'),
    (r'./data/txt/import/camuy/camuy-d.txt'),
    (r'./data/txt/import/camuy/camuy-e.txt'),
    (r'./data/txt/import/camuy/camuy-f.txt'),
    (r'./data/txt/import/camuy/camuy-g.txt'),
    (r'./data/txt/import/camuy/camuy-h.txt'),
    (r'./data/txt/import/camuy/camuy-i.txt'),
    (r'./data/txt/import/camuy/camuy-j.txt'),
    (r'./data/txt/import/camuy/camuy-k.txt'),
    (r'./data/txt/import/camuy/camuy-m.txt'),
    (r'./data/txt/import/camuy/camuy-n.txt'),
    # (r'./data/txt/import/camuy/camuy-o.txt'),
    (r'./data/txt/import/camuy/camuy-p.txt'),
    (r'./data/txt/import/camuy/camuy-q.txt'),
    (r'./data/txt/import/camuy/camuy-r.txt'),
    (r'./data/txt/import/camuy/camuy-s.txt'),
    (r'./data/txt/import/camuy/camuy-r.txt'),
    (r'./data/txt/import/camuy/camuy-u.txt'),
    (r'./data/txt/import/camuy/camuy-v.txt'),
    (r'./data/txt/import/camuy/camuy-w.txt'),
    (r'./data/txt/import/camuy/camuy-x.txt'),
    (r'./data/txt/import/camuy/camuy-y.txt'),
    (r'./data/txt/import/camuy/camuy-z.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-a.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-b.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-c.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-d.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-e.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-f.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-g.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-h.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-i.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-j.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-k.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-l.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-m.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-n.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-o.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-p.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-r.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-s.txt'),
    (r'./data/txt/import/quebradillas/quebradillas-z.txt'),
])
def test_extract_phone(territory):
    phones = jw.txt.extract_phone(
        territory)

    assert len(phones) > 0

    for phone in phones:
        assert isinstance(phone, Phone)
        # print(phone)

    print(territory)
    print(f"phones size: {len(phones)}")


@pytest.mark.csv
@pytest.mark.parametrize("params", [
    (r'./data/txt/import/arecibo-a.txt',
     r'./data/csv/export/arecibo-a.csv',
     'arecibo-a'),
    (r'./data/txt/import/arecibo-b.txt',
     r'./data/csv/export/arecibo-b.csv',
     'arecibo-b'),
    (r'./data/txt/import/arecibo-c.txt',
     r'./data/csv/export/arecibo-c.csv',
     'arecibo-c'),
    (r'./data/txt/import/arecibo-d.txt',
     r'./data/csv/export/arecibo-d.csv',
     'arecibo-d'),
    (r'./data/txt/import/arecibo-e.txt',
     r'./data/csv/export/arecibo-e.csv',
     'arecibo-e'),
    (r'./data/txt/import/arecibo-f.txt',
     r'./data/csv/export/arecibo-f.csv',
     'arecibo-f'),
    (r'./data/txt/import/arecibo-g.txt',
     r'./data/csv/export/arecibo-g.csv',
     'arecibo-g'),
    (r'./data/txt/import/arecibo-h.txt',
     r'./data/csv/export/arecibo-h.csv',
     'arecibo-h'),
    (r'./data/txt/import/arecibo-i.txt',
     r'./data/csv/export/arecibo-i.csv',
     'arecibo-i'),
    (r'./data/txt/import/arecibo-j.txt',
     r'./data/csv/export/arecibo-j.csv',
     'arecibo-j'),
    (r'./data/txt/import/arecibo-k.txt',
     r'./data/csv/export/arecibo-k.csv',
     'arecibo-k'),
    (r'./data/txt/import/arecibo-l.txt',
     r'./data/csv/export/arecibo-l.csv',
     'arecibo-l'),
    (r'./data/txt/import/arecibo-m.txt',
     r'./data/csv/export/arecibo-m.csv',
     'arecibo-m'),
    (r'./data/txt/import/arecibo-n.txt',
     r'./data/csv/export/arecibo-n.csv',
     'arecibo-n'),
    (r'./data/txt/import/arecibo-o.txt',
     r'./data/csv/export/arecibo-o.csv',
     'arecibo-o'),
    (r'./data/txt/import/arecibo-p.txt',
     r'./data/csv/export/arecibo-p.csv',
     'arecibo-p'),
    (r'./data/txt/import/arecibo-q.txt',
     r'./data/csv/export/arecibo-q.csv',
     'arecibo-q'),
    (r'./data/txt/import/arecibo-r.txt',
     r'./data/csv/export/arecibo-r.csv',
     'arecibo-r'),
    (r'./data/txt/import/arecibo-s.txt',
     r'./data/csv/export/arecibo-s.csv',
     'arecibo-s'),
    (r'./data/txt/import/arecibo-t.txt',
     r'./data/csv/export/arecibo-t.csv',
     'arecibo-t'),
    (r'./data/txt/import/arecibo-v.txt',
     r'./data/csv/export/arecibo-v.csv',
     'arecibo-v'),
    (r'./data/txt/import/arecibo-w.txt',
     r'./data/csv/export/arecibo-w.csv',
     'arecibo-w'),
    (r'./data/txt/import/arecibo-z.txt',
     r'./data/csv/export/arecibo-z.csv',
     'arecibo-z'),
])
def test_create_csv(params):
    (txt, path, territory) = params
    phones = jw.txt.extract_phone(txt)

    assert len(phones) > 1

    for phone in phones:
        assert isinstance(phone, Phone)

    print(territory)
    print(f"phones size: {len(phones)}")

    create_csv(phones, path, territory)
