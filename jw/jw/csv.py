""" Handles csv logic. """

import csv
import re


def print_csv(items, path, territory_id):
    """ Print content to a csv file. """
    phone_regex = re.compile(r'(\d{3})(\d{3})(\d{4})')
    with open(path, mode='w') as f:
        fieldNames = ['First Name', 'Last Name',
                      'Address', 'Phone', 'Territory ID']
        writer = csv.DictWriter(f, fieldnames=fieldNames)
        writer.writeheader()
        for item in items:
            writer.writerow({
                'First Name': item.first,
                'Last Name': item.last,
                'Address': item.address.replace('\xa0', ''),
                'Phone': phone_regex.sub(r'\1-\2-\3', item.phone),
                'Territory ID': territory_id
            })


def get_items_from_csv(path):
    """ Get items from csv file. """
    from . import Phone

    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        items = []
        for row in reader:
            items.append(
                Phone(row['First Name'], row['Last Name'],
                      row['Address'], row['Phone'])
            )
        return items
