"""
Webscrapper for teritorry.

This is a web scrapper for getting phone numbers for territory.
"""

__version__ = '0.1.0'

import re
import requests
from bs4 import BeautifulSoup


def get_url(url):
    """ Get content from url. """
    r = requests.get(url)

    if r.status_code == 200:
        return r.content

    return None


def get_file(filePath):
    """ Get content from file. """
    try:
        with open(filePath, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        pass

    return None


def get_dom(content):
    """ Create dom object from html. """
    soup = BeautifulSoup(content, "html.parser")
    return soup


def get_phone_numbers(dom):
    """ Get the phone numbers from dom object. """
    from collections import namedtuple
    Phone = namedtuple('Phone', ['first', 'last', 'address', 'phone'])

    items = dom.find_all('a', href=re.compile(r'^/Phone/787'))

    res = []
    for item in items:
        name = item.find('span').find('em').text.split(' ')
        address = item.find('span').find('i').text
        number = item.find('b').text
        res.append(Phone(name[0], " ".join(name[1:]), address, number))

    return res


def print_csv(items, path):
    """ Print content to a csv file. """
    import csv

    with open(path, mode='w') as f:
        fieldNames = ['first', 'last', 'address', 'phone']
        writer = csv.DictWriter(f, fieldnames=fieldNames)
        writer.writeheader()
        for item in items:
            writer.writerow({
                'first': item.first,
                'last': item.last,
                'address': item.address.replace('\xa0', ''),
                'phone': item.phone
            })


def run(path, name):
    """ Run jw scrapper. """
    content = ""
    if re.match(r"^https?|^www", path):
        content = get_url(path)
    else:
        content = get_file(path)

    dom = get_dom(content)
    phones = get_phone_numbers(dom)

    print_csv(phones, name)
