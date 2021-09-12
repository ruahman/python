import re
import ipdb
from jw import get_url, get_file, get_phone_numbers, get_dom, print_csv


def test_get_url():

    url = "https://wallhaven.cc/"
    r = get_url(url)

    assert r is not None

    url = "https://www.telephonedirectories.us/Puerto_Rico/Quebradillas/ZIP/00678"  # noqa: E501
    r = get_url(url)

    assert r is None


def test_get_file():

    path = r"/mnt/c/Users/dego_/Projects/python/jw/data/html/quebradillas-1.html"  # noqa: E501
    r = get_file(path)

    assert r is not None

    path = r"C:\not\a\real\path.html"
    r = get_file(path)

    assert r is None


def test_get_dom():

    path = r"/mnt/c/Users/dego_/Projects/python/jw/data/html/quebradillas-1.html"  # noqa: E501
    r = get_file(path)

    soup = get_dom(r)

    title = soup.find('title')

    assert title.text == '▷ Telephone Directory of Quebradillas, PR. 00678'

    # ipdb.set_trace()
    allHrefs = soup.find_all('a')
    phoneNumbers = soup.find_all('a', href=re.compile(r'Phone/787'))

    print(len(allHrefs))
    print(len(phoneNumbers))
    assert len(phoneNumbers) > 10
    assert len(phoneNumbers) < len(allHrefs)


def test_get_phone_numbers():

    path = r"/mnt/c/Users/dego_/Projects/python/jw/data/quebradillas-1.html"  # noqa: E501
    r = get_file(path)

    dom = get_dom(r)

    # ipdb.set_trace()
    r = get_phone_numbers(dom)

    assert len(r) > 3

    for p in r:
        assert len(p.first.strip()) > 0
        # assert len(p.last.strip()) > 0
        # assert len(p.address.strip()) > 0
        assert len(p.phone.strip()) > 0


def test_print_csv():

    path = r"/mnt/c/Users/dego_/Projects/python/jw/data/quebradillas-1.html"  # noqa: E501
    r = get_file(path)

    dom = get_dom(r)

    items = get_phone_numbers(dom)

    ipdb.set_trace()
    print_csv(items, 'data/quebradillas_1.csv')
