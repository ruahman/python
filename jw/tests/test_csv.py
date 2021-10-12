import pytest
import ipdb
import jw.txt
import jw.csv
from jw import Phone


@pytest.mark.skip
def test_get_items_from_csv():
    # ipdb.set_trace()
    items = jw.csv.get_items_from_csv('./data/csv/quebradillas_1.csv')
    print(items)
    assert len(items) > 0


@pytest.mark.csv
@pytest.mark.parametrize("territory", [
    (r'./data/txt/import/arecibo-a.txt', []),
    (r'./data/txt/import/arecibo-b.txt', []),
    (r'./data/txt/import/arecibo-c.txt', []),
])
def test_extract_phone(territory):
    phones = jw.txt.extract_phone(
        territory[0],
        territory[1])

    assert len(phones) > 1

    for phone in phones:
        assert isinstance(phone, Phone)

    print(f"phones size: {len(phones)}")


@pytest.mark.csv
@pytest.mark.parametrize("territory", [
    ('arecibo-a', []),
    # ('arecibo-b', []),
    # ('arecibo-c', []),
])
def test_create_csv(territory):
    phones = jw.txt.extract_phone(
        fr"./data/txt/import/{territory[0]}.txt",
        territory[1])

    ipdb.set_trace()
    assert len(phones) > 1

    for phone in phones:
        assert isinstance(phone, Phone)

    # jw.csv.print_csv(items, 'data/csv/quebradillas-c.csv', 'quebradillas-c')
    # for phone in phones:
    #     print(phone)

    # jw.csv.print_csv(items, 'data/csv/quebradillas-c.csv', 'quebradillas-c')
