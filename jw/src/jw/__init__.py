"""
Webscrapper for teritorry.

This is a web scrapper for getting phone numbers for territory.
"""

__version__ = '0.1.0'

import re
import requests
# from .dom import get_dom
from .csv import get_items_from_csv
from .pdf import make_pdf_from_items

from collections import namedtuple
Phone = namedtuple('Phone', ['first', 'last', 'address', 'phone', 'notes'])


def get_url(url):
    """Get content from url."""
    r = requests.get(url)

    if r.status_code == 200:
        return r.content

    return None


def get_file(filePath):
    """Get content from file."""
    try:
        with open(filePath, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        pass

    return None


def get_phone_numbers(dom):
    """Get the phone numbers from dom object."""
    items = dom.find_all('a', href=re.compile(r'^/Phone/787'))

    res = []
    for item in items:
        name = item.find('span').find('em').text.split(' ')
        address = item.find('span').find('i').text
        number = item.find('b').text
        res.append(Phone(name[0], " ".join(name[1:]), address, number))

    return res


def pdf(csv_path, title, pdf_path):
    """Create PDF from CSV file."""
    items = get_items_from_csv(csv_path)
    make_pdf_from_items(items, title, pdf_path)
    # print(items)


def csv():
    """Generate csvs'."""
    pass
